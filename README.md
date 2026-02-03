# Pine Script V6 Documentation Crawler

A Python-based tool for crawling and processing TradingView's Pine Script V6 documentation, built using the **Crawl4Ai** framework. This tool extracts, cleans, and organizes the documentation, making it easier to reference and analyze. Crawl4Ai provides the core framework for web crawling, data extraction, and asynchronous processing.

## ✨ Features

### Crawling
- Automatically extracts documentation from TradingView's Pine Script V6 website using Crawl4Ai
- Efficiently handles navigation through documentation pages
- Supports batch processing with rate limiting
- Maintains a structured extraction schema for consistent results
- Saves individual URLs and combined documentation files

### Content Processing
- Cleans and formats documentation content
- Preserves Pine Script code blocks with proper syntax highlighting
- Extracts and formats function documentation
- Removes unnecessary navigation elements (footer links, "On this page" sections)
- Processes content into a clean, readable markdown format

### Output Organization
- Creates separate files for URLs and content
- Generates combined documentation files for easy reference
- Maintains original section order from TradingView documentation
- Tracks extraction statistics and timestamps

## 📊 Documentation Coverage

| Source | Items | Sections | Size |
|--------|-------|----------|------|
| Reference Manual | 941 | 7 | 0.7 MB |
| User Manual | 71 | 11 | 2.7 MB |

### Reference Sections
Annotations (10), Constants (239), Functions (475), Keywords (15), Operators (21), Types (20), Variables (161)

### User Manual Sections
Welcome, Primer, Language, Visuals, Concepts, Writing, FAQ, Error Messages, Release Notes, Migration Guides, Where Can I Get More Information

## 🛠️ Setup

### 1. Clone the repository:
```bash
git clone https://github.com/faustoevillegas86/Pine_Script_v6_doc.git
cd Pine_Script_v6_doc
```

### 2. Install dependencies:
```bash
python setup.py
```

Or manually:
```bash
pip install -r requirements.txt
playwright install chromium
```

## 🚀 Usage

### Run Complete Extraction
```bash
python src/run_all.py
```

### Run Individually
```bash
python src/extract_urls.py     # Extract URLs only
python src/extract_content.py  # Extract content only
```

## � Project Structure

```
Pine_Script_v6_doc/
├── README.md
├── requirements.txt
├── setup.py                  # Installs all dependencies
├── src/
│   ├── run_all.py            # Run complete extraction
│   ├── extract_urls.py       # URL extraction
│   └── extract_content.py    # Content extraction
└── output/
    ├── reference_urls.md     # 941 Reference URLs
    ├── reference_content.md  # Complete reference documentation
    ├── docs_urls.md          # 71 Docs URLs
    └── docs_content.md       # Complete user manual
```

## 📝 Output Files

| File | Description |
|------|-------------|
| `reference_urls.md` | URLs to all 941 reference items |
| `reference_content.md` | Complete API reference (functions, types, constants, etc.) |
| `docs_urls.md` | URLs to all 71 documentation pages |
| `docs_content.md` | Complete user manual with tutorials and guides |

## 🔧 Dependencies

| Package | Purpose |
|---------|---------|
| crawl4ai | Web scraping framework |
| beautifulsoup4 | HTML parsing |
| playwright | Browser automation |
| requests | HTTP requests |
| aiofiles | Async file operations |

---

**Source**: TradingView Pine Script V6 Documentation  
**Framework**: [Crawl4Ai](https://github.com/unclecode/crawl4ai)  
**Last Updated**: February 2026
