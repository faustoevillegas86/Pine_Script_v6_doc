#!/usr/bin/env python3
"""
Google Apps Script (ES-419) - Content Extractor
Extracts content only from the main article area (green box),
excluding the "En esta página" sidebar (red box).
"""

import asyncio
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

from markdown_helpers import (
    anchor_for_item,
    html_to_markdown,
    rewrite_internal_links,
    slugify,
)

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


def extract_markdown_from_main(main, base_url: str = "") -> str:
    return html_to_markdown(main, base_url=base_url)


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
                if not url.startswith("http"):
                    continue
                urls.append({"section": current_section, "name": name, "url": url})
    return urls


async def extract_page_content(page, url: str):
    await page.goto(url, wait_until="domcontentloaded", timeout=90000)
    await asyncio.sleep(3)
    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")
    main = get_main_container(soup)
    remove_sidebar_content(main)
    return extract_markdown_from_main(main, base_url=url)


def generate_content_document(sections: dict, output_file: Path):
    doc = "# Google Apps Script (ES-419) - Complete Content\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    doc += "## Table of Contents\n\n"
    total = 0
    for section, items in sections.items():
        count = len(items)
        total += count
        anchor = slugify(section)
        doc += f"- [{section}](#{anchor}) ({count})\n"
        for item in items:
            item_anchor = anchor_for_item(item, output_file.name, item.get("name", ""))
            doc += f"  - [{item['name']}](#{item_anchor})\n"
    doc += f"\n**Total: {total} items**\n\n"
    doc += "---\n\n"

    for section, items in sections.items():
        doc += f"## {section}\n\n"
        for item in items:
            item_anchor = anchor_for_item(item, output_file.name, item.get("name", ""))
            content = rewrite_internal_links(item["content"].strip(), output_file.name)
            doc += f'<a id="{item_anchor}"></a>\n\n'
            doc += f"### {item['name']}\n\n"
            doc += content + "\n\n"
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
