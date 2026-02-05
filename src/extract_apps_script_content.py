#!/usr/bin/env python3
"""
Google Apps Script (ES-419) - Content Extractor
Extracts content only from the main article area (green box),
excluding the "En esta página" sidebar (red box).
"""

import asyncio
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup, NavigableString
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

URLS_FILE = OUTPUT_DIR / "apps_script_urls.md"


def get_main_container(soup: BeautifulSoup):
    selectors = ["main", "article", ".devsite-article", ".devsite-article-body"]
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            return node
    return soup.body


def remove_sidebar_content(main):
    if not main:
        return
    for selector in [
        ".devsite-on-this-page",
        ".devsite-toc",
        ".devsite-nav",
        ".devsite-breadcrumb-nav",
        "nav",
        "aside",
    ]:
        for node in main.select(selector):
            node.decompose()


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split()).strip()


def extract_markdown_from_main(main) -> str:
    if not main:
        return ""
    lines = []
    for elem in main.find_all(
        ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "pre", "code"],
        recursive=True,
    ):
        if elem.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(elem.name[1])
            heading_text = normalize_whitespace(elem.get_text(" ", strip=True))
            if heading_text:
                lines.append(f"{'#' * level} {heading_text}")
        elif elem.name == "pre":
            code_text = elem.get_text("\n", strip=False)
            if code_text.strip():
                lines.append("```")
                lines.append(code_text.rstrip())
                lines.append("```")
        elif elem.name == "code":
            if elem.parent and elem.parent.name == "pre":
                continue
            code_text = elem.get_text(" ", strip=True)
            if code_text:
                lines.append(f"`{code_text}`")
        elif elem.name == "li":
            text = normalize_whitespace(elem.get_text(" ", strip=True))
            if text:
                lines.append(f"- {text}")
        else:
            text = normalize_whitespace(elem.get_text(" ", strip=True))
            if text:
                lines.append(text)

    cleaned = []
    last_blank = False
    for line in lines:
        if not line:
            if not last_blank:
                cleaned.append("")
            last_blank = True
            continue
        cleaned.append(line)
        last_blank = False

    return "\n".join(cleaned).strip()


def parse_urls_from_markdown(urls_file: Path):
    urls = []
    current_section = "General"
    if not urls_file.exists():
        return urls
    for line in urls_file.read_text(encoding="utf-8").splitlines():
        if line.startswith("## ") and not line.startswith("## Table"):
            current_section = line[3:].strip()
        elif line.startswith("- ["):
            if "](" in line and line.endswith(")"):
                name = line.split("[", 1)[1].split("]", 1)[0]
                url = line.split("(", 1)[1].rsplit(")", 1)[0]
                urls.append({"section": current_section, "name": name, "url": url})
    return urls


async def extract_page_content(page, url: str):
    await page.goto(url, wait_until="domcontentloaded", timeout=90000)
    await asyncio.sleep(3)
    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")
    main = get_main_container(soup)
    remove_sidebar_content(main)
    return extract_markdown_from_main(main)


def generate_content_document(sections: dict, output_file: Path):
    doc = "# Google Apps Script (ES-419) - Complete Content\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    doc += "## Table of Contents\n\n"
    total = 0
    for section, items in sections.items():
        count = len(items)
        total += count
        anchor = section.lower().replace(" ", "-")
        doc += f"- [{section}](#{anchor}) ({count})\n"
    doc += f"\n**Total: {total} items**\n\n"
    doc += "---\n\n"

    for section, items in sections.items():
        doc += f"## {section}\n\n"
        for item in items:
            doc += f"### {item['name']}\n\n"
            doc += item["content"].strip() + "\n\n"
            doc += "---\n\n"

    output_file.write_text(doc, encoding="utf-8")
    size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"[OK] Saved: {output_file.name} ({total} items, {size_mb:.2f} MB)")


async def main():
    print("=" * 60)
    print("GOOGLE APPS SCRIPT - CONTENT EXTRACTOR")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    urls_to_crawl = parse_urls_from_markdown(URLS_FILE)
    if not urls_to_crawl:
        print("[ERROR] apps_script_urls.md not found or empty. Run extract_apps_script_urls.py first.")
        return

    sections = {}
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for index, item in enumerate(urls_to_crawl, start=1):
            try:
                print(f"  [{index}/{len(urls_to_crawl)}] {item['name'][:40]}...", end=" ", flush=True)
                content = await extract_page_content(page, item["url"])
                section = item["section"]
                sections.setdefault(section, []).append(
                    {
                        "name": item["name"],
                        "url": item["url"],
                        "content": content,
                    }
                )
                print("[OK]")
            except Exception as exc:
                print(f"[FAIL] {str(exc)[:50]}")
            await asyncio.sleep(0.5)

        await browser.close()

    generate_content_document(sections, OUTPUT_DIR / "apps_script_content.md")

    print("\n" + "=" * 60)
    print("[OK] Content extraction complete!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
