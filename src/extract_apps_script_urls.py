#!/usr/bin/env python3
"""
Apps Script - URL Extractor
Extracts URLs from Google Apps Script documentation pages and generates
an indexed document.
"""

import asyncio
from collections import OrderedDict
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

TARGET_URLS = [
    "https://developers.google.com/apps-script?hl=es-419",
    "https://developers.google.com/apps-script/overview?hl=es-419",
    "https://developers.google.com/apps-script/reference?hl=es-419",
    "https://developers.google.com/apps-script/samples?hl=es-419",
]

MAIN_CONTENT_SELECTORS = [
    ".devsite-article-body",
    ".devsite-article",
    "article",
    "main",
]

EXCLUDED_SELECTORS = [
    ".devsite-on-this-page",
    ".devsite-toc",
    ".devsite-nav",
]


async def load_page_html(page, url):
    """Load page with Playwright and return HTML content."""
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=90000)
        await asyncio.sleep(4)
        return await page.content()
    except Exception as exc:
        print(f"[Error] Failed to load {url}: {exc}")
        return ""


def find_main_container(soup):
    """Locate the main content container in a DevSite page."""
    for selector in MAIN_CONTENT_SELECTORS:
        container = soup.select_one(selector)
        if container:
            return container
    return soup.body or soup


def remove_excluded_blocks(container):
    """Remove navigation, TOC, and related blocks from the container."""
    for selector in EXCLUDED_SELECTORS:
        for element in container.select(selector):
            element.decompose()

    for element in container.find_all(["nav", "aside", "div", "section"]):
        text = element.get_text(" ", strip=True)
        if "En esta página" in text:
            element.decompose()


def normalize_link(href, base_url):
    """Normalize URLs and filter out unsupported schemes."""
    if not href:
        return ""
    if href.startswith("javascript:") or href.startswith("mailto:"):
        return ""
    return urljoin(base_url, href)


def extract_links_from_container(container, base_url):
    """Extract links grouped by section headings."""
    sections = OrderedDict()
    current_h2 = ""
    current_section = "General"

    def ensure_section(name):
        if name not in sections:
            sections[name] = []

    ensure_section(current_section)

    for element in container.descendants:
        if not hasattr(element, "name"):
            continue

        if element.name in {"h1", "h2", "h3", "h4"}:
            heading_text = element.get_text(" ", strip=True)
            if not heading_text:
                continue
            if element.name == "h2":
                current_h2 = heading_text
                current_section = heading_text
            elif element.name in {"h3", "h4"}:
                current_section = f"{current_h2} / {heading_text}" if current_h2 else heading_text
            else:
                current_section = heading_text
            ensure_section(current_section)
            continue

        if element.name == "a":
            href = element.get("href", "")
            url = normalize_link(href, base_url)
            if not url:
                continue
            link_text = element.get_text(" ", strip=True)
            if not link_text:
                link_text = element.get("aria-label", "") or url
            ensure_section(current_section)
            if not any(item["url"] == url for item in sections[current_section]):
                sections[current_section].append({
                    "name": link_text,
                    "url": url,
                })

    return sections


def merge_sections(target, source):
    """Merge section dictionaries preserving order and avoiding duplicates."""
    for section, items in source.items():
        if section not in target:
            target[section] = []
        existing_urls = {item["url"] for item in target[section]}
        for item in items:
            if item["url"] not in existing_urls:
                target[section].append(item)
                existing_urls.add(item["url"])


def generate_url_document(sections, source_name, output_file):
    """Generate markdown document with URL index."""
    doc = f"# {source_name} - URL Index\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"

    doc += "## Table of Contents\n\n"
    total = 0
    for section in sections.keys():
        count = len(sections[section])
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
    print("APPS SCRIPT - URL EXTRACTOR")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        aggregated_sections = OrderedDict()

        for url in TARGET_URLS:
            print(f"\n[Apps Script] Extracting URLs from {url}")
            html = await load_page_html(page, url)
            if not html:
                continue
            soup = BeautifulSoup(html, "html.parser")
            container = find_main_container(soup)
            remove_excluded_blocks(container)
            sections = extract_links_from_container(container, url)
            merge_sections(aggregated_sections, sections)

        await browser.close()

    if aggregated_sections:
        generate_url_document(
            aggregated_sections,
            "Google Apps Script",
            OUTPUT_DIR / "apps_script_urls.md",
        )

    print("\n" + "=" * 60)
    print("[OK] URL extraction complete!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
