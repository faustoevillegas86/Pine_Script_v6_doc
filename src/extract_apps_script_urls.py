#!/usr/bin/env python3
"""
Google Apps Script (ES-419) - URL Extractor
Extracts section/subsection URLs from the main content area (green box),
excluding the "En esta página" sidebar (red box).

Sources:
- https://developers.google.com/apps-script?hl=es-419
- https://developers.google.com/apps-script/overview?hl=es-419
- https://developers.google.com/apps-script/reference?hl=es-419
- https://developers.google.com/apps-script/samples?hl=es-419
"""

import asyncio
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

APPS_SCRIPT_PAGES = [
    "https://developers.google.com/apps-script?hl=es-419",
    "https://developers.google.com/apps-script/overview?hl=es-419",
    "https://developers.google.com/apps-script/reference?hl=es-419",
    "https://developers.google.com/apps-script/samples?hl=es-419",
]

ALLOWED_PREFIXES = (
    "https://developers.google.com/apps-script",
    "https://developers.google.com/apps-script/",
    "https://developers.google.com/apps-script/reference",
    "https://developers.google.com/apps-script/samples",
)


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


def is_allowed_url(url: str) -> bool:
    if not url:
        return False
    if url.startswith("#"):
        return False
    if url.startswith("http"):
        return url.startswith(ALLOWED_PREFIXES)
    return url.startswith("/apps-script")


def extract_page_title(main, soup, url: str) -> str:
    if main:
        h1 = main.find("h1")
        if h1 and h1.get_text(strip=True):
            return h1.get_text(strip=True)
    title = soup.title.get_text(strip=True) if soup.title else url
    return title or url


async def extract_page_urls(page, url: str):
    await page.goto(url, wait_until="domcontentloaded", timeout=90000)
    await asyncio.sleep(3)
    html = await page.content()
    soup = BeautifulSoup(html, "html.parser")
    main = get_main_container(soup)
    remove_sidebar_content(main)
    title = extract_page_title(main, soup, url)

    seen = set()
    items = []
    if not main:
        return title, items

    for link in main.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link.get("href", "").strip()
        if not text or not href:
            continue
        if not is_allowed_url(href):
            continue
        full_url = urljoin(url, href)
        if full_url in seen:
            continue
        seen.add(full_url)
        items.append({"name": text, "url": full_url})

    return title, items


def generate_url_document(sections: dict, output_file: Path):
    doc = "# Google Apps Script (ES-419) - URL Index\n\n"
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
            doc += f"- [{item['name']}]({item['url']})\n"
        doc += "\n"

    output_file.write_text(doc, encoding="utf-8")
    print(f"[OK] Saved: {output_file.name} ({total} URLs)")


async def main():
    print("=" * 60)
    print("GOOGLE APPS SCRIPT - URL EXTRACTOR")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    sections = {}

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        for url in APPS_SCRIPT_PAGES:
            try:
                title, items = await extract_page_urls(page, url)
                sections[title] = items
                print(f"[OK] {title}: {len(items)} URLs")
            except Exception as exc:
                print(f"[FAIL] {url}: {exc}")

        await browser.close()

    generate_url_document(sections, OUTPUT_DIR / "apps_script_urls.md")

    print("\n" + "=" * 60)
    print("[OK] URL extraction complete!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
