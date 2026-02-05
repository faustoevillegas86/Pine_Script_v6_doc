#!/usr/bin/env python3
"""
Apps Script Documentation Content Extractor.

Extracts the main content of Apps Script documentation pages from a URL list
and writes a single markdown file with a section index.
"""

import asyncio
import re
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
URLS_FILE = OUTPUT_DIR / "apps_script_urls.md"
OUTPUT_FILE = OUTPUT_DIR / "apps_script_content.md"

MAIN_SELECTORS = ("article", ".devsite-article", ".devsite-article-body")
NAV_SELECTORS = (
    "nav",
    "aside",
    ".devsite-article-nav",
    ".devsite-article-nav-right",
    ".devsite-article-nav-left",
    ".devsite-article-navigation",
    ".devsite-toc",
    ".devsite-book-nav",
    ".devsite-side-nav",
    ".devsite-nav",
    ".devsite-breadcrumbs",
    ".devsite-article-meta",
    ".devsite-article-actions",
    ".devsite-article-footer",
    ".devsite-article-recommendations",
    ".devsite-feedback",
)


def parse_urls(markdown: str) -> list[dict]:
    urls_to_crawl: list[dict] = []
    current_section = "General"

    for line in markdown.splitlines():
        if line.startswith("## ") and not line.startswith("## Table"):
            current_section = line[3:].strip()
        elif line.startswith("- ["):
            match = re.match(r"- \[([^\]]+)\]\(([^\)]+)\)", line)
            if match:
                name = match.group(1).strip()
                url = match.group(2).strip()
                if url.startswith("http"):
                    urls_to_crawl.append(
                        {
                            "name": name,
                            "url": url,
                            "section": current_section,
                        }
                    )

    return urls_to_crawl


def find_main_container(soup: BeautifulSoup):
    for selector in MAIN_SELECTORS:
        container = soup.select_one(selector)
        if container:
            return container
    return soup.body or soup


def clean_main_container(container):
    for selector in NAV_SELECTORS:
        for element in container.select(selector):
            element.decompose()

    for element in container.find_all(string=True):
        if element.strip().lower() in {"en esta página", "on this page"}:
            parent = element.parent
            if parent:
                parent.decompose()


def extract_text_blocks(container) -> str:
    blocks: list[str] = []

    for element in container.find_all(
        ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li"],
        recursive=True,
    ):
        if element.name == "p" and element.find_parent("li"):
            continue
        if element.name == "li" and element.find_parent("li"):
            continue

        text = " ".join(element.stripped_strings)
        if not text:
            continue

        if element.name.startswith("h"):
            level = int(element.name[1])
            blocks.append(f"{'#' * level} {text}")
        elif element.name == "li":
            blocks.append(f"- {text}")
        else:
            blocks.append(text)

    cleaned = "\n\n".join(blocks)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


async def fetch_page_html(page, url: str) -> str:
    await page.goto(url, wait_until="networkidle", timeout=90000)
    await asyncio.sleep(2)
    return await page.content()


async def extract_apps_script_content() -> dict:
    print("\n[Apps Script] Extracting content with Playwright...")

    if not URLS_FILE.exists():
        print("[Apps Script] Error: apps_script_urls.md not found.")
        return {}

    urls_to_crawl = parse_urls(URLS_FILE.read_text(encoding="utf-8"))
    print(f"[Apps Script] Found {len(urls_to_crawl)} URLs to crawl")

    sections: dict[str, list[dict]] = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for i, item in enumerate(urls_to_crawl):
            try:
                print(
                    f"  [{i+1}/{len(urls_to_crawl)}] {item['name'][:35]}...",
                    end=" ",
                    flush=True,
                )
                html = await fetch_page_html(page, item["url"])

                soup = BeautifulSoup(html, "lxml")
                main_container = find_main_container(soup)
                clean_main_container(main_container)
                page_content = extract_text_blocks(main_container)

                section = item["section"]
                sections.setdefault(section, []).append(
                    {
                        "name": item["name"],
                        "url": item["url"],
                        "content": page_content,
                    }
                )

                print("[OK]")
            except Exception as exc:
                print(f"[FAIL] {str(exc)[:40]}")

            await asyncio.sleep(0.5)

        await browser.close()

    total = sum(len(v) for v in sections.values())
    print(f"[Apps Script] Extracted {total} pages in {len(sections)} sections")
    return sections


def generate_content_document(sections: dict, output_file: Path):
    doc = "# Apps Script Documentation - Content\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

    doc += "## Table of Contents\n\n"
    total = 0
    for section in sections.keys():
        items = sections[section]
        count = len(items)
        total += count
        section_anchor = section.lower().replace(" ", "-")
        doc += f"- [{section}](#{section_anchor}) ({count})\n"

    doc += f"\n**Total: {total} items**\n\n"
    doc += "---\n\n"

    for section in sections.keys():
        items = sections[section]
        doc += f"## {section}\n\n"

        for item in items:
            doc += f"### {item['name']}\n\n"
            doc += item["content"] + "\n\n"
            doc += "---\n\n"

    output_file.write_text(doc, encoding="utf-8")
    size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"[OK] Saved: {output_file.name} ({total} items, {size_mb:.2f} MB)")


async def main():
    print("=" * 60)
    print("APPS SCRIPT - CONTENT EXTRACTOR")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    sections = await extract_apps_script_content()
    if sections:
        generate_content_document(sections, OUTPUT_FILE)

    print("\n" + "=" * 60)
    print("[OK] Content extraction complete!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
