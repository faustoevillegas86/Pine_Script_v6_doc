#!/usr/bin/env python3
"""
Pine Script V6 - Content Extractor (v3)
Robust extraction with proper HTML structure navigation.

Key improvements:
- Extracts text from all nested divs (tv-pine-reference-item__text)
- Preserves code blocks with proper line breaks
- Adds spaces between inline elements
- Formats description, type, syntax, and parameters properly
"""

import asyncio
import re
import copy
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright
from crawl4ai import AsyncWebCrawler, BrowserConfig
from bs4 import BeautifulSoup, NavigableString

# Configuration
ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"

REFERENCE_URL = "https://www.tradingview.com/pine-script-reference/v6/"
DOCS_URL = "https://www.tradingview.com/pine-script-docs/welcome/"

# Section mappings for Reference
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


def get_text_with_spacing(elem) -> str:
    """
    Extract text from element preserving spaces between inline elements.
    This prevents text like 'the library()function' becoming 'thelibrary()function'.
    """
    if isinstance(elem, NavigableString):
        return str(elem)
    
    # For code elements, get text without extra spaces
    if elem.name in ['code', 'span'] and elem.parent and elem.parent.name not in ['pre']:
        return elem.get_text()
    
    result = ""
    for child in elem.children:
        if isinstance(child, NavigableString):
            result += str(child)
        elif hasattr(child, 'name'):
            child_text = get_text_with_spacing(child)
            # Add space before inline elements if needed
            if child.name in ['code', 'a', 'span', 'strong', 'em', 'b', 'i']:
                if result and not result.endswith(' ') and not result.endswith('\n'):
                    result += ' '
                result += child_text
                if not child_text.endswith(' '):
                    result += ' '
            else:
                result += child_text
    
    return result


def extract_code_block_text(elem) -> str:
    """
    Extract text from a code/pre element preserving line breaks.
    Converts <br/> tags to actual newlines and iterates through spans.
    """
    code_text = ""
    
    # Find the innermost code element if exists
    inner = elem.find('code') if elem.name == 'pre' else elem
    if not inner:
        inner = elem
    
    for child in inner.children:
        if isinstance(child, str):
            code_text += str(child)
        elif hasattr(child, 'name'):
            if child.name == 'br':
                code_text += '\n'
            elif child.name == 'span':
                # Recursively get text from span
                code_text += extract_code_block_text(child)
            else:
                code_text += child.get_text()
    
    return code_text


def extract_item_content(item_div) -> dict:
    """
    Extract content from item div with proper structure handling.
    Navigates the nested HTML structure correctly.
    """
    try:
        item_id = item_div.get('id', 'unknown')
        
        # Get header/name
        header = item_div.find(['h3', 'h2', 'h1'])
        item_name = header.get_text(strip=True) if header else item_id
        
        # Clone for safe manipulation
        working_div = copy.deepcopy(item_div)
        
        # Remove scripts and styles
        for el in working_div(['script', 'style']):
            el.decompose()
        
        # Find content wrapper
        content_div = working_div.find('div', {'class': 'tv-pine-reference-item__content'})
        if not content_div:
            content_div = working_div
        
        # Remove "SEE ALSO" section
        see_also = content_div.find('div', {'class': 'tv-pine-reference-item__sub-header'}, 
                                     string=re.compile(r'see\s*also', re.I))
        if see_also:
            # Remove see_also and its next siblings
            for sibling in list(see_also.find_next_siblings()):
                try:
                    sibling.decompose()
                except:
                    pass
            try:
                see_also.decompose()
            except:
                pass
        
        # Also try text matching
        for tag in content_div.find_all():
            if (tag.get_text(strip=True) or '').lower() == 'see also':
                try:
                    tag.decompose()
                except:
                    pass
                break
        
        # Remove see-also links
        for see_also_links in content_div.find_all('div', {'class': 'tv-pine-reference-item__see-also'}):
            try:
                see_also_links.decompose()
            except:
                pass
        
        # Build content from structure
        content_parts = []
        current_section = None
        
        for elem in content_div.find_all(['div', 'pre', 'code'], recursive=True):
            classes = elem.get('class', [])
            
            # Sub-headers (Type, Syntax, Arguments, Example, Remarks, etc.)
            if 'tv-pine-reference-item__sub-header' in classes:
                section_text = elem.get_text(strip=True)
                if section_text.lower() == 'see also':
                    break  # Stop at see also
                current_section = section_text
                content_parts.append(f"\n**{section_text}**")
            
            # Main text content
            elif 'tv-pine-reference-item__text' in classes:
                text = get_text_with_spacing(elem).strip()
                # Clean excessive whitespace
                text = re.sub(r'\s+', ' ', text)
                if text:
                    content_parts.append(text)
            
            # Code examples
            elif elem.name == 'pre' or 'tv-pine-reference-item__code' in classes:
                code_text = extract_code_block_text(elem)
                if code_text.strip():
                    content_parts.append(f"\n```pine\n{code_text.strip()}\n```\n")
            
            # Arguments list
            elif 'tv-pine-reference-item__text-group' in classes:
                text = get_text_with_spacing(elem).strip()
                if text:
                    content_parts.append(text)
        
        # If we got no content from structured extraction, fall back
        if not content_parts or sum(len(p) for p in content_parts) < 20:
            # Try getting all text divs
            for text_div in content_div.find_all('div', {'class': 'tv-pine-reference-item__text'}):
                text = get_text_with_spacing(text_div).strip()
                if text:
                    content_parts.append(text)
            
            # Still nothing? Get all text
            if not content_parts:
                content = content_div.get_text(separator='\n', strip=True)
                content = re.sub(r'\n\n\n+', '\n\n', content)
                return {
                    'id': item_id,
                    'name': item_name,
                    'content': content,
                    'size': len(content)
                }
        
        content = '\n'.join(content_parts)
        content = re.sub(r'\n\n\n+', '\n\n', content)
        content = content.replace('\xa0', ' ')
        content = content.strip()
        
        return {
            'id': item_id,
            'name': item_name,
            'content': content,
            'size': len(content)
        }
    except Exception as e:
        return {
            'id': item_div.get('id', 'unknown'),
            'error': str(e)[:100]
        }


async def extract_reference_content():
    """Extract all content from Pine Script Reference using Playwright."""
    print("\n[Reference] Extracting content with Playwright...")
    
    sections = {}
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            await page.goto(REFERENCE_URL, wait_until='networkidle', timeout=90000)
            await asyncio.sleep(5)
            html = await page.content()
        except Exception as e:
            print(f"[Reference] Error: {e}")
            await browser.close()
            return {}
        
        await browser.close()
    
    try:
        soup = BeautifulSoup(html, 'lxml')
    except:
        soup = BeautifulSoup(html, 'html.parser')
    
    items = soup.find_all('div', {'class': 'tv-pine-reference-item'})
    print(f"[Reference] Found {len(items)} items in page")
    
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
        
        # Extract with proper handling
        extracted = extract_item_content(item)
        
        if 'error' not in extracted:
            sections[section_name].append({
                'id': item_id,
                'name': extracted['name'],
                'content': extracted['content'],
                'url': f"{REFERENCE_URL}#{item_id}"
            })
    
    total = sum(len(v) for v in sections.values())
    print(f"[Reference] Extracted {total} items in {len(sections)} sections")
    return sections


async def extract_docs_content():
    """Extract all content from Pine Script Docs using crawl4ai."""
    print("\n[Docs] Extracting content with crawl4ai...")
    
    urls_file = OUTPUT_DIR / "docs_urls.md"
    if not urls_file.exists():
        print("[Docs] Error: docs_urls.md not found. Run extract_urls.py first.")
        return {}
    
    # Parse URLs from markdown file
    urls_to_crawl = []
    current_section = "General"
    
    file_content = urls_file.read_text(encoding='utf-8')
    for line in file_content.split('\n'):
        if line.startswith('## ') and not line.startswith('## Table'):
            current_section = line[3:].strip()
        elif line.startswith('- ['):
            match = re.match(r'- \[([^\]]+)\]\(([^\)]+)\)', line)
            if match:
                name = match.group(1)
                url = match.group(2)
                if url.startswith('http'):
                    urls_to_crawl.append({
                        'name': name,
                        'url': url,
                        'section': current_section
                    })
    
    print(f"[Docs] Found {len(urls_to_crawl)} URLs to crawl")
    
    browser_config = BrowserConfig(
        headless=True,
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"]
    )
    
    sections = {}
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        for i, item in enumerate(urls_to_crawl):
            try:
                print(f"  [{i+1}/{len(urls_to_crawl)}] {item['name'][:35]}...", end=" ", flush=True)
                
                result = await crawler.arun(url=item['url'])
                
                if result.success:
                    # Use crawl4ai's markdown conversion
                    if isinstance(result.markdown, str):
                        page_content = result.markdown
                    else:
                        page_content = result.markdown.raw_markdown if result.markdown else ""
                    
                    # Clean navigation
                    page_content = clean_docs_navigation(page_content)
                    
                    section = item['section']
                    if section not in sections:
                        sections[section] = []
                    
                    sections[section].append({
                        'name': item['name'],
                        'url': item['url'],
                        'content': page_content
                    })
                    
                    print("[OK]")
                else:
                    print(f"[FAIL]")
                    
            except Exception as e:
                print(f"[FAIL] {str(e)[:30]}")
            
            await asyncio.sleep(0.5)
    
    total = sum(len(v) for v in sections.values())
    print(f"[Docs] Extracted {total} pages in {len(sections)} sections")
    return sections


def clean_docs_navigation(content: str) -> str:
    """
    Remove navigation elements and URLs from markdown content.
    Strips markdown links, keeping only link text.
    Completely removes 'On this page' sidebar sections.
    """
    import re
    
    # Remove markdown links but keep text: [text](url) -> text
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    
    # Remove bare URLs
    content = re.sub(r'https?://[^\s\)]+', '', content)
    
    # Remove any line containing "On this page" (case insensitive)
    content = re.sub(r'^.*[Oo]n this page.*$', '', content, flags=re.MULTILINE)
    
    lines = content.split('\n')
    cleaned = []
    started_content = False
    in_sidebar_nav = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines at start
        if not started_content and not stripped:
            continue
        
        # Skip short bullet points before content (navigation menu)
        if stripped.startswith('* ') and len(stripped) < 60:
            if not started_content:
                continue
        
        # Start content at first heading
        if not started_content:
            if line.startswith('# '):
                started_content = True
                cleaned.append(line)
            continue
        
        # Skip footer
        if 'Copyright' in line:
            break
        
        # Skip Previous/Next navigation links
        if stripped.startswith('Previous') or stripped.startswith('Next'):
            continue
        
        # Skip "Copied" markers (from code copy buttons)
        if stripped == 'Copied':
            continue
        
        # Skip "Pine Script®" standalone lines (code block markers)
        if stripped == 'Pine Script®':
            continue
        
        # Skip external community links (footer elements)
        skip_patterns = [
            'Pine Q&A chat', 'Stack Overflow', 'Telegram', 'Reddit',
            'Discord', 'Facebook', 'Twitter', 'YouTube', 'LinkedIn',
            '↗'  # External link indicator
        ]
        if any(pattern in stripped for pattern in skip_patterns):
            continue
        
        cleaned.append(line)
    
    result = '\n'.join(cleaned)
    
    # Fix code blocks: The markdown has patterns like:
    # `code line 1
    # code line 2
    # `
    # We need to convert to:
    # ```pine
    # code line 1
    # code line 2
    # ```
    
    lines = result.split('\n')
    fixed_lines = []
    in_code_block = False
    code_buffer = []
    
    for line in lines:
        stripped = line.strip()
        
        # Check for line starting with backtick (start of code block)
        if stripped.startswith('`') and not stripped.startswith('```') and not in_code_block:
            # Check if this looks like Pine code
            content_after = stripped[1:]  # Remove the backtick
            if content_after.startswith('//@') or content_after.startswith('indicator') or content_after.startswith('strategy') or content_after.startswith('library'):
                in_code_block = True
                fixed_lines.append('```pine')
                fixed_lines.append(content_after)  # Add code without backtick
                continue
        
        # Check for line ending with backtick (end of code block)
        if in_code_block and stripped == '`':
            in_code_block = False
            fixed_lines.append('```')
            continue
        
        if in_code_block and stripped.endswith('`') and not stripped.endswith('```'):
            # End of code block with content
            in_code_block = False
            fixed_lines.append(stripped[:-1])  # Remove trailing backtick
            fixed_lines.append('```')
            continue
        
        fixed_lines.append(line)
    
    result = '\n'.join(fixed_lines)
    
    # Clean up excessive whitespace
    result = re.sub(r'\n{3,}', '\n\n', result)
    
    return result.strip()


def generate_content_document(sections: dict, source_name: str, output_file: Path):
    """Generate markdown document with content and index."""
    
    doc = f"# {source_name} - Complete Content\n\n"
    doc += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    
    # Table of contents
    doc += "## Table of Contents\n\n"
    total = 0
    for section in sections.keys():  # Preserve original order
        items = sections[section]
        count = len(items)
        total += count
        section_anchor = section.lower().replace(' ', '-')
        doc += f"- [{section}](#{section_anchor}) ({count})\n"
    
    doc += f"\n**Total: {total} items**\n\n"
    doc += "---\n\n"
    
    # Content sections
    for section in sections.keys():  # Preserve original order
        items = sections[section]
        doc += f"## {section}\n\n"
        
        for item in items:  # Preserve original order
            name = item.get('name', item.get('id', 'Unknown'))
            content = item.get('content', '')
            
            doc += f"### {name}\n\n"
            doc += content + "\n\n"
            doc += "---\n\n"
    
    output_file.write_text(doc, encoding='utf-8')
    size_mb = output_file.stat().st_size / (1024 * 1024)
    print(f"[OK] Saved: {output_file.name} ({total} items, {size_mb:.2f} MB)")


async def main():
    """Main execution."""
    print("="*60)
    print("PINE SCRIPT V6 - CONTENT EXTRACTOR v3")
    print("="*60)
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Extract Reference content
    reference_sections = await extract_reference_content()
    if reference_sections:
        generate_content_document(
            reference_sections,
            "Pine Script V6 Reference",
            OUTPUT_DIR / "reference_content.md"
        )
    
    # Extract Docs content
    docs_sections = await extract_docs_content()
    if docs_sections:
        generate_content_document(
            docs_sections,
            "Pine Script V6 Documentation",
            OUTPUT_DIR / "docs_content.md"
        )
    
    print("\n" + "="*60)
    print("[OK] Content extraction complete!")
    print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
