#!/usr/bin/env python3
"""
Pine Script V6 - URL Extractor
Extracts URLs from both sources and generates indexed documents.

Sources:
- Reference: tradingview.com/pine-script-reference/v6
- Docs: tradingview.com/pine-script-docs
"""

import asyncio
import re
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Configuration
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

REFERENCE_URL = "https://www.tradingview.com/pine-script-reference/v6/"
DOCS_URL = "https://www.tradingview.com/pine-script-docs/welcome/"

# Section mappings for Reference (in display order)
REFERENCE_SECTIONS = {
    'an': 'Annotations',
    'const': 'Constants', 
    'fun': 'Functions',
    'kw': 'Keywords',
    'op': 'Operators',
    'type': 'Types',
    'var': 'Variables'
}

# Section order for Reference (as on website)
REFERENCE_ORDER = ['Annotations', 'Constants', 'Functions', 'Keywords', 'Operators', 'Types', 'Variables']

# Section order for Docs (as on website navigation)
DOCS_ORDER = [
    'Welcome',
    'Primer',
    'Language',
    'Visuals',
    'Concepts',
    'Writing',
    'Faq',
    'Error Messages',
    'Release Notes',
    'Migration Guides',
    'Where Can I Get More Information'
]


async def extract_reference_urls(page):
    """Extract all URLs from Pine Script Reference page."""
    print("\n[Reference] Extracting URLs...")
    
    try:
        await page.goto(REFERENCE_URL, wait_until='domcontentloaded', timeout=90000)
        await asyncio.sleep(5)
        
        html = await page.content()
    except Exception as e:
        print(f"[Reference] Error loading page: {e}")
        return {}
    
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', {'class': 'tv-pine-reference-item'})
    
    sections = {}
    for item in items:
        item_id = item.get('id', '')
        if not item_id:
            continue
        
        # Get section from prefix
        match = re.match(r'([a-z]+)_', item_id)
        if match:
            prefix = match.group(1)
            section_name = REFERENCE_SECTIONS.get(prefix, prefix.upper())
        else:
            section_name = 'Other'
        
        if section_name not in sections:
            sections[section_name] = []
        
        url = f"{REFERENCE_URL}#{item_id}"
        
        # Get item name
        header = item.find(['h2', 'h3', 'h1'])
        name = header.get_text(strip=True) if header else item_id
        
        sections[section_name].append({
            'id': item_id,
            'name': name,
            'url': url
        })
    
    print(f"[Reference] Found {sum(len(v) for v in sections.values())} items in {len(sections)} sections")
    return sections


async def extract_docs_urls(page):
    """Extract all URLs from Pine Script Docs."""
    print("\n[Docs] Extracting URLs...")
    
    try:
        await page.goto(DOCS_URL, wait_until='domcontentloaded', timeout=90000)
        await asyncio.sleep(5)
        
        html = await page.content()
    except Exception as e:
        print(f"[Docs] Error loading page: {e}")
        return {}
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all links on the page
    sections = {}
    
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        text = link.get_text(strip=True)
        
        if not href or not text:
            continue
        
        # Filter Pine Script docs URLs only
        if '/pine-script-docs/' not in href:
            continue
        
        # Include all pine-script-docs URLs (including migration guides)
        
        # Normalize URL
        if href.startswith('/'):
            url = f"https://www.tradingview.com{href}"
        elif not href.startswith('http'):
            continue
        else:
            url = href
        
        # Determine section from URL path
        path = href.replace('/pine-script-docs/', '').strip('/')
        parts = path.split('/')
        if len(parts) >= 1 and parts[0]:
            section = parts[0].replace('-', ' ').title()
        else:
            section = 'General'
        
        if section not in sections:
            sections[section] = []
        
        # Avoid duplicates
        if not any(item['url'] == url for item in sections[section]):
            sections[section].append({
                'name': text,
                'url': url
            })
    
    print(f"[Docs] Found {sum(len(v) for v in sections.values())} items in {len(sections)} sections")
    return sections


def generate_url_document(sections: dict, source_name: str, output_file: Path):
    """Generate markdown document with URL index."""
    
    doc = f"# {source_name} - URL Index\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    # Table of contents
    doc += "## Table of Contents\n\n"
    total = 0
    for section in sections.keys():
        count = len(sections[section])
        total += count
        anchor = section.lower().replace(' ', '-')
        doc += f"- [{section}](#{anchor}) ({count})\n"
    
    doc += f"\n**Total: {total} items**\n\n"
    doc += "---\n\n"
    
    # Sections with URLs
    for section in sections.keys():
        items = sections[section]
        doc += f"## {section}\n\n"
        
        for item in items:  # Preserve original order
            name = item.get('name', item.get('id', 'Unknown'))
            url = item['url']
            doc += f"- [{name}]({url})\n"
        
        doc += "\n"
    
    output_file.write_text(doc, encoding='utf-8')
    print(f"[OK] Saved: {output_file.name} ({total} URLs)")


async def main():
    """Main execution."""
    print("="*60)
    print("PINE SCRIPT V6 - URL EXTRACTOR")
    print("="*60)
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Extract Reference URLs
        reference_sections = await extract_reference_urls(page)
        if reference_sections:
            generate_url_document(
                reference_sections, 
                "Pine Script V6 Reference",
                OUTPUT_DIR / "reference_urls.md"
            )
        
        # Extract Docs URLs  
        docs_sections = await extract_docs_urls(page)
        if docs_sections:
            generate_url_document(
                docs_sections,
                "Pine Script V6 Documentation", 
                OUTPUT_DIR / "docs_urls.md"
            )
        
        await browser.close()
    
    print("\n" + "="*60)
    print("[OK] URL extraction complete!")
    print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
