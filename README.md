# Pine Script V6 Documentation

Complete documentation for TradingView's Pine Script V6, extracted and organized.

## 📁 Project Structure

```
Pine_Script_v6_doc/
├── README.md
├── requirements.txt
├── setup.py                  # Installs dependencies
├── src/
│   ├── run_all.py            # Run complete extraction
│   ├── extract_urls.py       # Extracts URLs from docs
│   └── extract_content.py    # Extracts content from pages
└── output/
    ├── reference_urls.md     # 941 Reference URLs
    ├── reference_content.md  # 941 items (0.7 MB)
    ├── docs_urls.md          # 71 Docs URLs
    └── docs_content.md       # 71 pages (2.7 MB)
```

## 🛠️ Installation

### Quick Setup (Recommended)
```bash
python setup.py
```

### Manual Installation
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

### Dependencies
| Package | Version | Purpose |
|---------|---------|---------|
| crawl4ai | >=0.4.0 | Web scraping |
| beautifulsoup4 | ~=4.12 | HTML parsing |
| playwright | >=1.49.0 | Browser automation |
| requests | ~=2.26 | HTTP requests |
| aiofiles | >=24.1.0 | Async file I/O |

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

## 📊 Documentation Stats

### Reference Manual (941 items)
| Section | Count |
|---------|-------|
| Annotations | 10 |
| Constants | 239 |
| Functions | 475 |
| Keywords | 15 |
| Operators | 21 |
| Types | 20 |
| Variables | 161 |

### User Manual (71 pages)
| Section | Count |
|---------|-------|
| Welcome | 1 |
| Primer | 3 |
| Language | 16 |
| Visuals | 11 |
| Concepts | 13 |
| Writing | 5 |
| FAQ | 13 |
| Error Messages | 1 |
| Release Notes | 1 |
| Migration Guides | 6 |
| Where Can I Get More Info | 1 |

## 📝 Output Files

| File | Description | Size |
|------|-------------|------|
| `reference_urls.md` | URLs to all 941 reference items | 89 KB |
| `reference_content.md` | Complete reference documentation | 0.7 MB |
| `docs_urls.md` | URLs to all 71 doc pages | 7 KB |
| `docs_content.md` | Complete user manual | 2.7 MB |

---

**Source**: TradingView Pine Script V6 Documentation  
**Last Updated**: February 2026
