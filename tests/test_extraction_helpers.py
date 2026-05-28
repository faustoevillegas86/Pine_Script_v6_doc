import importlib.util
import asyncio
import sys
import types
from pathlib import Path
from textwrap import dedent

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]


def load_module(monkeypatch, module_name, relative_path, *, crawl4ai=False):
    playwright = types.ModuleType("playwright")
    playwright_async_api = types.ModuleType("playwright.async_api")
    playwright_async_api.async_playwright = lambda: None
    monkeypatch.setitem(sys.modules, "playwright", playwright)
    monkeypatch.setitem(sys.modules, "playwright.async_api", playwright_async_api)

    if crawl4ai:
        crawl4ai_module = types.ModuleType("crawl4ai")
        crawl4ai_module.AsyncWebCrawler = object
        crawl4ai_module.BrowserConfig = object
        monkeypatch.setitem(sys.modules, "crawl4ai", crawl4ai_module)

    spec = importlib.util.spec_from_file_location(module_name, ROOT / relative_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_apps_script_url_parser_skips_table_of_contents_and_anchors(tmp_path, monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_apps_script_content_test",
        "src/extract_apps_script_content.py",
    )
    urls_file = tmp_path / "apps_script_urls.md"
    urls_file.write_text(
        "\n".join(
            [
                "# Google Apps Script (ES-419) - URL Index",
                "",
                "## Table of Contents",
                "",
                "- [Overview](#overview) (2)",
                "",
                "---",
                "",
                "## Overview",
                "",
                "- [Real Page](https://developers.google.com/apps-script/overview?hl=es-419)",
                "- [Anchor Only](#anchor)",
            ]
        ),
        encoding="utf-8",
    )

    assert module.parse_urls_from_markdown(urls_file) == [
        {
            "section": "Overview",
            "name": "Real Page",
            "url": "https://developers.google.com/apps-script/overview?hl=es-419",
        }
    ]


def test_apps_script_sidebar_cleanup_keeps_article_content(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_apps_script_urls_test",
        "src/extract_apps_script_urls.py",
    )
    soup = BeautifulSoup(
        """
        <main>
          <nav>Navigation</nav>
          <aside>Aside links</aside>
          <div class="devsite-on-this-page">En esta pagina</div>
          <article><h1>Keep me</h1><p>Article content</p></article>
        </main>
        """,
        "html.parser",
    )
    main = soup.select_one("main")

    module.remove_sidebar_content(main)

    text = main.get_text(" ", strip=True)
    assert "Navigation" not in text
    assert "Aside links" not in text
    assert "En esta pagina" not in text
    assert "Keep me" in text
    assert "Article content" in text


def test_apps_script_url_document_normalizes_multiline_names(tmp_path, monkeypatch):
    urls_module = load_module(
        monkeypatch,
        "extract_apps_script_urls_generate_test",
        "src/extract_apps_script_urls.py",
    )
    content_module = load_module(
        monkeypatch,
        "extract_apps_script_content_parse_test",
        "src/extract_apps_script_content.py",
    )
    urls_file = tmp_path / "apps_script_urls.md"

    urls_module.generate_url_document(
        {
            "ReferenciaOrganiza tus páginas con colecciones Guarda y categoriza el contenido según tus preferencias.": [
                {
                    "name": "API\nde Apps Script",
                    "url": "https://developers.google.com/apps-script/api/concepts?hl=es-419",
                }
            ]
        },
        urls_file,
    )

    text = urls_file.read_text(encoding="utf-8")
    assert "## Referencia" in text
    assert "- [API de Apps Script](https://developers.google.com/apps-script/api/concepts?hl=es-419)" in text
    assert "API\nde Apps Script" not in text
    assert content_module.parse_urls_from_markdown(urls_file) == [
        {
            "section": "Referencia",
            "name": "API de Apps Script",
            "url": "https://developers.google.com/apps-script/api/concepts?hl=es-419",
        }
    ]


def test_apps_script_title_strips_google_site_suffix(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_apps_script_title_test",
        "src/extract_apps_script_urls.py",
    )
    soup = BeautifulSoup(
        """
        <html>
          <head><title>Apps Script | Google for Developers</title></head>
          <body><main><h2>Desarrolla soluciones de alta calidad con facilidad</h2></main></body>
        </html>
        """,
        "html.parser",
    )

    assert module.extract_page_title(
        soup.select_one("main"),
        soup,
        "https://developers.google.com/apps-script?hl=es-419",
    ) == "Apps Script"


def test_apps_script_generic_card_link_uses_card_heading(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_apps_script_card_link_test",
        "src/extract_apps_script_urls.py",
    )

    async def no_sleep(*args, **kwargs):
        return None

    monkeypatch.setattr(module.asyncio, "sleep", no_sleep)

    class FakePage:
        async def goto(self, *args, **kwargs):
            return None

        async def content(self):
            return dedent(
                """
                <main>
                  <div class="devsite-landing-row-item">
                    <div class="devsite-landing-row-item-body">
                      <h3>Guía de inicio rápido de Vertex AI</h3>
                      <div>El servicio avanzado de Vertex AI...</div>
                      <div class="devsite-landing-row-item-buttons">
                        <a href="/apps-script/quickstart/vertex-ai?hl=es-419">Ver muestra</a>
                      </div>
                    </div>
                  </div>
                </main>
                """
            )

    title, items = asyncio.run(
        module.extract_page_urls(
            FakePage(),
            "https://developers.google.com/apps-script?hl=es-419",
        )
    )

    assert title == "https://developers.google.com/apps-script?hl=es-419"
    assert items == [
        {
            "name": "Guía de inicio rápido de Vertex AI",
            "url": "https://developers.google.com/apps-script/quickstart/vertex-ai?hl=es-419",
        }
    ]


def test_pine_docs_navigation_cleanup_formats_code_and_removes_noise(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        Menu item

        # Welcome

        On this page

        Read the [overview](https://www.tradingview.com/pine-script-docs/welcome/).

        `//@version=6
        indicator("Example")
        `

        Copied

        Copyright 2026
        Footer text
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert cleaned.startswith("# Welcome")
    assert "On this page" not in cleaned
    assert "https://" not in cleaned
    assert "overview" in cleaned
    assert "```pine" in cleaned
    assert "indicator(\"Example\")" in cleaned
    assert "Copied" not in cleaned
    assert "Footer text" not in cleaned


def test_pine_docs_navigation_keeps_pages_that_start_at_second_level_heading(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_h2_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        Version Version 6 Version 5
          * [Overview](https://www.tradingview.com/pine-script-docs/errors/overview)

        [User Manual](https://www.tradingview.com/pine-script-docs) / Errors and warnings / CE10101
        ## [The condition of the “X” statement must evaluate to a “bool” value](https://www.tradingview.com/pine-script-docs/errors/CE10101/#the-condition-of-the-x-statement-must-evaluate-to-a-bool-value)

        This compilation error occurs if one or more conditions return a value that is not bool.

        ## On this page

        Copyright 2026
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert cleaned.startswith("## The condition")
    assert "This compilation error occurs" in cleaned
    assert "Version Version" not in cleaned
    assert "On this page" not in cleaned


def test_pine_docs_url_extraction_uses_visible_sidebar_section_names(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_urls_sidebar_sections_test",
        "src/extract_urls.py",
    )

    async def no_sleep(*args, **kwargs):
        return None

    monkeypatch.setattr(module.asyncio, "sleep", no_sleep)

    class FakePage:
        async def goto(self, *args, **kwargs):
            return None

        async def content(self):
            return dedent(
                """
                <ul class="toc">
                  <li class="item">
                    <a href="/pine-script-docs/welcome/">Welcome to Pine Script® v6</a>
                  </li>
                  <li class="item">
                    <details>
                      <summary>Pine Script® primer</summary>
                      <ul class="children">
                        <li><a href="/pine-script-docs/primer/first-steps/">First steps</a></li>
                      </ul>
                    </details>
                  </li>
                  <li class="item">
                    <details>
                      <summary>Errors and warnings</summary>
                      <ul class="children">
                        <li><a href="/pine-script-docs/errors/overview/">Overview</a></li>
                        <li><a href="/pine-script-docs/errors/CE10101/">CE10101</a></li>
                      </ul>
                    </details>
                  </li>
                </ul>
                """
            )

    sections = asyncio.run(module.extract_docs_urls(FakePage()))

    assert list(sections) == [
        "Welcome to Pine Script® v6",
        "Pine Script® primer",
        "Errors and warnings",
    ]
    assert sections["Errors and warnings"] == [
        {
            "name": "Overview",
            "url": "https://www.tradingview.com/pine-script-docs/errors/overview/",
        },
        {
            "name": "CE10101",
            "url": "https://www.tradingview.com/pine-script-docs/errors/CE10101/",
        },
    ]
