#!/usr/bin/env python3
"""Shared Markdown conversion and internal-link helpers."""

from __future__ import annotations

import re
from urllib.parse import unquote, urljoin, urlparse

from bs4 import NavigableString


DOCS_CONTENT_FILE = "docs_content.md"
REFERENCE_CONTENT_FILE = "reference_content.md"
APPS_SCRIPT_CONTENT_FILE = "apps_script_content.md"


def slugify(value: str) -> str:
    """Return a stable, lowercase anchor token."""
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "section"


def anchor_token_from_fragment(fragment: str) -> str:
    """Convert a URL fragment to a unique, readable anchor token."""
    parts = []
    current = []
    for char in unquote(fragment).lower():
        if char.isalnum():
            current.append(char)
            continue
        if current:
            parts.append("".join(current))
            current = []
        if char in {"_", ".", " "}:
            continue
        parts.append(format(ord(char), "x"))
    if current:
        parts.append("".join(current))
    return "-".join(parts) or "section"


def strip_heading_link_targets(markdown: str) -> str:
    """Turn linked headings into plain headings while keeping heading text."""
    return re.sub(
        r"^(#{1,6}\s*)\[([^\]]+)\]\([^\)]+\)",
        r"\1\2",
        markdown,
        flags=re.MULTILINE,
    )


def reference_anchor_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    if "pine-script-reference" not in parsed.path and "pine-script-reference" not in url:
        return None
    if not parsed.fragment:
        return None
    return reference_anchor_from_fragment(parsed.fragment)


def reference_anchor_from_fragment(fragment: str) -> str | None:
    if not re.match(r"^(?:an|const|fun|kw|op|type|var)_", unquote(fragment)):
        return None
    return f"ref-{anchor_token_from_fragment(fragment)}"


def reference_anchor_from_shorthand(fragment: str, link_text: str) -> str | None:
    if not fragment or reference_anchor_from_fragment(fragment):
        return None
    prefix = "fun" if "(" in link_text and ")" in link_text else "var"
    return f"ref-{prefix}-{anchor_token_from_fragment(fragment)}"


def docs_anchor_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    marker = "/pine-script-docs/"
    if marker not in parsed.path:
        return None
    path = parsed.path.split(marker, 1)[1].strip("/") or "welcome"
    return f"docs-{slugify(path.replace('/', '-'))}"


def apps_script_anchor_from_url(url: str) -> str | None:
    parsed = urlparse(url)
    marker = "/apps-script/"
    if marker not in parsed.path:
        return None
    path = parsed.path.split(marker, 1)[1].strip("/") or "overview"
    return f"apps-{slugify(path.replace('/', '-'))}"


def internal_target_for_url(url: str) -> tuple[str, str] | None:
    """Return target combined Markdown file and anchor for known internal URLs."""
    anchor = reference_anchor_from_url(url)
    if anchor:
        return REFERENCE_CONTENT_FILE, anchor

    anchor = docs_anchor_from_url(url)
    if anchor:
        return DOCS_CONTENT_FILE, anchor

    anchor = apps_script_anchor_from_url(url)
    if anchor:
        return APPS_SCRIPT_CONTENT_FILE, anchor

    return None


def anchor_for_item(item: dict, document_file: str, fallback: str = "") -> str:
    """Return the explicit anchor used for an item in a combined document."""
    url = item.get("url", "")
    if url:
        target = internal_target_for_url(url)
        if target:
            return target[1]

    if document_file == REFERENCE_CONTENT_FILE and item.get("id"):
        return f"ref-{anchor_token_from_fragment(item['id'])}"

    prefixes = {
        DOCS_CONTENT_FILE: "docs",
        REFERENCE_CONTENT_FILE: "ref",
        APPS_SCRIPT_CONTENT_FILE: "apps",
    }
    prefix = prefixes.get(document_file, "doc")
    return f"{prefix}-{slugify(fallback or item.get('name', 'section'))}"


def is_reference_term(text: str) -> bool:
    stripped = text.strip("`").strip()
    return bool(re.fullmatch(r"[A-Za-z_][\w.<>]*(?:\(\))?", stripped))


def rewrite_internal_links(
    markdown: str,
    current_document: str,
    *,
    format_reference_code: bool = False,
) -> str:
    """Rewrite known internal links to combined-document anchors.

    Fenced code blocks are left untouched.
    """

    rewritten = []
    in_fenced_code = False
    for line in markdown.split("\n"):
        if line.strip().startswith("```"):
            in_fenced_code = not in_fenced_code
            rewritten.append(line)
            continue
        if in_fenced_code:
            rewritten.append(line)
            continue
        rewritten.append(
            rewrite_markdown_links_in_line(line, current_document, format_reference_code)
        )
    return "\n".join(rewritten)


def rewrite_markdown_links_in_line(
    line: str,
    current_document: str,
    format_reference_code: bool,
) -> str:
    output = []
    index = 0
    while index < len(line):
        if line.startswith("![", index):
            parsed_image = parse_markdown_link(line, index + 1)
            if parsed_image:
                _, _, end = parsed_image
                output.append(line[index:end])
                index = end
                continue

        if line[index] == "[":
            parsed = parse_markdown_link(line, index)
            if parsed:
                text, url, end = parsed
                output.append(
                    markdown_link_for_target(
                        text,
                        url,
                        current_document,
                        format_reference_code,
                    )
                )
                index = end
                continue

        output.append(line[index])
        index += 1
    return "".join(output)


def parse_markdown_link(line: str, start: int) -> tuple[str, str, int] | None:
    if start >= len(line) or line[start] != "[":
        return None

    bracket_depth = 0
    index = start
    while index < len(line):
        char = line[index]
        if char == "\\":
            index += 2
            continue
        if char == "[":
            bracket_depth += 1
        elif char == "]":
            bracket_depth -= 1
            if bracket_depth == 0:
                break
        index += 1

    if bracket_depth != 0 or index + 1 >= len(line) or line[index + 1] != "(":
        return None

    text = line[start + 1:index]
    url_start = index + 2
    paren_depth = 1
    index = url_start
    while index < len(line):
        char = line[index]
        if char == "\\":
            index += 2
            continue
        if char == "(":
            paren_depth += 1
        elif char == ")":
            paren_depth -= 1
            if paren_depth == 0:
                return text, line[url_start:index], index + 1
        index += 1

    return None


def markdown_link_for_target(
    text: str,
    url: str,
    current_document: str,
    format_reference_code: bool,
    *,
    text_prefix: str = "",
    text_suffix: str = "",
) -> str:
    target = internal_target_for_url(url)
    if not target and current_document == REFERENCE_CONTENT_FILE:
        parsed = urlparse(url)
        if not parsed.scheme and not parsed.netloc and not parsed.path and parsed.fragment:
            anchor = reference_anchor_from_fragment(parsed.fragment)
            if anchor:
                target = REFERENCE_CONTENT_FILE, anchor
    if not target and "pine-script-reference" in url:
        parsed = urlparse(url)
        anchor = reference_anchor_from_shorthand(parsed.fragment, text)
        if anchor:
            target = REFERENCE_CONTENT_FILE, anchor
    if not target:
        link_text = f"{text_prefix}{text}{text_suffix}"
        return f"[{link_text}]({url})"

    target_document, anchor = target
    href = f"#{anchor}" if target_document == current_document else f"./{target_document}#{anchor}"
    link_text = text
    if (
        format_reference_code
        and target_document == REFERENCE_CONTENT_FILE
        and is_reference_term(text)
    ):
        link_text = f"`{text.strip('`').strip()}`"
    return f"[{text_prefix}{link_text}{text_suffix}]({href})"


def normalize_inline(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def code_text_from_node(node) -> str:
    parts = []
    for child in node.children:
        if isinstance(child, NavigableString):
            parts.append(str(child))
        elif getattr(child, "name", None) == "br":
            parts.append("\n")
        elif hasattr(child, "children"):
            parts.append(code_text_from_node(child))
        else:
            parts.append(child.get_text("", strip=False))
    return "".join(parts)


def detect_code_language(node) -> str:
    candidates = [node]
    inner_code = node.find("code") if getattr(node, "name", None) == "pre" else None
    if inner_code:
        candidates.append(inner_code)
    for candidate in candidates:
        for class_name in candidate.get("class", []):
            if class_name.startswith("language-"):
                return class_name.split("language-", 1)[1]
            if class_name in {"pine", "javascript", "python", "html", "css"}:
                return class_name
    return ""


def inline_markdown(node, base_url: str = "") -> str:
    if isinstance(node, NavigableString):
        return str(node)

    name = getattr(node, "name", None)
    if name == "br":
        return "\n"
    if name in {"script", "style", "nav", "aside"}:
        return ""
    if name == "code" and not (node.parent and node.parent.name == "pre"):
        return f"`{node.get_text('', strip=False)}`"
    if name in {"strong", "b"}:
        return f"**{normalize_inline(children_inline_markdown(node, base_url))}**"
    if name in {"em", "i"}:
        return f"*{normalize_inline(children_inline_markdown(node, base_url))}*"
    if name in {"s", "del", "strike"}:
        return f"~~{normalize_inline(children_inline_markdown(node, base_url))}~~"
    if name == "u":
        return f"<u>{normalize_inline(children_inline_markdown(node, base_url))}</u>"
    if name == "a":
        href = node.get("href", "")
        text = normalize_inline(children_inline_markdown(node, base_url)) or href
        if not href:
            return text
        return f"[{text}]({urljoin(base_url, href)})"
    if name == "img":
        src = node.get("src", "")
        if not src:
            return ""
        alt = node.get("alt", "image") or "image"
        return f"![{alt}]({urljoin(base_url, src)})"
    return children_inline_markdown(node, base_url)


def children_inline_markdown(node, base_url: str = "") -> str:
    return "".join(inline_markdown(child, base_url) for child in node.children)


def block_markdown(node, base_url: str = "", indent: int = 0) -> str:
    if isinstance(node, NavigableString):
        return normalize_inline(str(node))

    name = getattr(node, "name", None)
    if name in {"script", "style", "nav", "aside"}:
        return ""
    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        text = normalize_inline(children_inline_markdown(node, base_url))
        return f"{'#' * level} {text}" if text else ""
    if name == "p":
        return normalize_inline(children_inline_markdown(node, base_url))
    if name == "pre":
        inner = node.find("code") or node
        code = code_text_from_node(inner).rstrip("\n")
        if not code.strip():
            return ""
        language = detect_code_language(node)
        return f"```{language}\n{code}\n```"
    if name == "code":
        return normalize_inline(inline_markdown(node, base_url))
    if name in {"ul", "ol"}:
        return list_markdown(node, base_url, indent, ordered=name == "ol")
    if name == "blockquote":
        inner = html_to_markdown(node, base_url)
        return "\n".join(f"> {line}" if line else ">" for line in inner.split("\n"))
    if name == "table":
        return table_markdown(node, base_url)
    if name == "img":
        return inline_markdown(node, base_url)
    if name == "li":
        return normalize_inline(children_inline_markdown(node, base_url))

    child_blocks = [block_markdown(child, base_url, indent) for child in node.children]
    return "\n\n".join(part for part in child_blocks if part)


def list_markdown(node, base_url: str, indent: int, *, ordered: bool) -> str:
    lines = []
    index = 1
    for item in node.find_all("li", recursive=False):
        inline_parts = []
        nested_lists = []
        for child in item.children:
            if getattr(child, "name", None) in {"ul", "ol"}:
                nested_lists.append(block_markdown(child, base_url, indent + 1))
            else:
                inline_parts.append(inline_markdown(child, base_url))
        marker = f"{index}." if ordered else "-"
        text = normalize_inline("".join(inline_parts))
        lines.append(f"{'  ' * indent}{marker} {text}".rstrip())
        lines.extend(nested_lists)
        index += 1
    return "\n".join(lines)


def table_markdown(node, base_url: str) -> str:
    rows = []
    for row in node.find_all("tr"):
        cells = row.find_all(["th", "td"], recursive=False)
        if cells:
            rows.append(
                [
                    normalize_inline(children_inline_markdown(cell, base_url)).replace("|", "\\|")
                    for cell in cells
                ]
            )
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    header = padded[0]
    separator = ["---"] * width
    body = padded[1:]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in body)
    return "\n".join(lines)


def html_to_markdown(node, base_url: str = "") -> str:
    if not node:
        return ""
    if isinstance(node, NavigableString):
        return normalize_inline(str(node))
    parts = [block_markdown(child, base_url) for child in node.children]
    markdown = "\n\n".join(part for part in parts if part)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip()
