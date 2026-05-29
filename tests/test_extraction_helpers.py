import importlib.util
import asyncio
import sys
import types
from pathlib import Path
from textwrap import dedent

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]


def load_module(monkeypatch, module_name, relative_path, *, crawl4ai=False):
    src_path = str(ROOT / "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

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
    assert "[overview](#docs-welcome)" in cleaned
    assert "```pine" in cleaned
    assert "indicator(\"Example\")" in cleaned
    assert "Copied" not in cleaned
    assert "Footer text" not in cleaned


def test_pine_docs_navigation_formats_admonitions_and_reference_links(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_formatting_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Type system

        TipAlthough collections cannot directly store IDs.

        The value can return [na](https://www.tradingview.com/pine-script-reference/v6/#var_na).

        NoteThe [array.new<int>()](https://www.tradingview.com/pine-script-reference/v6/#fun_array.new) function creates an array.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "**Tip:**\nAlthough collections" in cleaned
    assert "**Note:**\nThe [`array.new<int>()`](./reference_content.md#ref-fun-array-new) function" in cleaned
    assert "[`na`](./reference_content.md#ref-var-na)" in cleaned
    assert "TipAlthough" not in cleaned
    assert "NoteThe" not in cleaned


def test_pine_docs_navigation_preserves_external_links_and_skips_code(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_link_rewrite_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Links

        Read [external](https://example.com/page) and [arrays](https://www.tradingview.com/pine-script-docs/language/arrays/).

        ```pine
        // Keep URL literal: https://www.tradingview.com/pine-script-docs/language/type-system/
        indicator("Links")
        ```
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "[external](https://example.com/page)" in cleaned
    assert "[arrays](#docs-language-arrays)" in cleaned
    assert "// Keep URL literal: https://www.tradingview.com/pine-script-docs/language/type-system/" in cleaned


def test_pine_docs_navigation_removes_malformed_on_this_page_links(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_sidebar_link_noise_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Execution model

        Useful content.

          * Introduction](https://www.tradingview.com/pine-script-docs/language/execution-model/#introduction)[
          * Time series](https://www.tradingview.com/pine-script-docs/language/execution-model/#time-series)

        More useful content.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "Useful content." in cleaned
    assert "More useful content." in cleaned
    assert "#introduction" not in cleaned
    assert "#time-series" not in cleaned


def test_pine_docs_navigation_removes_previous_next_page_navigation(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_previous_next_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Inputs

        Useful content.

        [ Previous ](https://www.tradingview.com/pine-script-docs/concepts/chart-information/) [ Next Libraries  ](https://www.tradingview.com/pine-script-docs/concepts/libraries/)

        ## Next
        We now recommend you go to the [Next Steps](https://www.tradingview.com/pine-script-docs/primer/next-steps/) page.

        [

        [ ](https://www.tradingview.com/pine-script-docs/concepts/inputs/)

        More useful content.

        Previous
        Next
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "Useful content." in cleaned
    assert "More useful content." in cleaned
    assert "Previous" not in cleaned
    assert "Next" not in cleaned
    assert "We now recommend you go" not in cleaned
    assert "\n[\n" not in cleaned
    assert "[ ](" not in cleaned
    assert "#docs-concepts-chart-information" not in cleaned
    assert "#docs-concepts-libraries" not in cleaned


def test_pine_docs_navigation_rewrites_history_operator_link(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_history_operator_link_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Operators

        Past values use the [[]](https://www.tradingview.com/pine-script-reference/v6/#op_%5B%5D) operator.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "[[]](./reference_content.md#ref-op-5b-5d)" in cleaned
    assert "https://www.tradingview.com/pine-script-reference" not in cleaned


def test_pine_docs_navigation_rewrites_links_with_brackets_in_text(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_nested_bracket_link_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Execution model

        Use the [[] history-referencing operator](https://www.tradingview.com/pine-script-docs/language/operators/#-history-referencing-operator).
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "[[] history-referencing operator](#docs-language-operators)" in cleaned
    assert "https://www.tradingview.com/pine-script-docs" not in cleaned


def test_pine_docs_navigation_closes_single_line_code_before_rewriting_links(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_single_line_code_link_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Documenting functions

        `//@function <description>`
        [//@function](https://www.tradingview.com/pine-script-reference/v6/#an_@function) annotation defines the main description.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "```pine\n//@function <description>\n```" in cleaned
    assert "[//@function](./reference_content.md#ref-an-40-function)" in cleaned
    assert "https://www.tradingview.com/pine-script-reference" not in cleaned


def test_pine_docs_navigation_rewrites_shorthand_reference_fragments(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_shorthand_reference_links_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Reference shorthand

        See [ta.percentrank()](https://www.tradingview.com/pine-script-reference/v6/#ta.percentrank), [plot()](https://www.tradingview.com/pine-script-reference/v6/#plot), [hl2](https://www.tradingview.com/pine-script-reference/v6/#hl2), and [open](https://www.tradingview.com/pine-script-reference/v6/#open).
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "[`ta.percentrank()`](./reference_content.md#ref-fun-ta-percentrank)" in cleaned
    assert "[`plot()`](./reference_content.md#ref-fun-plot)" in cleaned
    assert "[`hl2`](./reference_content.md#ref-var-hl2)" in cleaned
    assert "[`open`](./reference_content.md#ref-var-open)" in cleaned
    assert "https://www.tradingview.com/pine-script-reference" not in cleaned


def test_generate_content_document_uses_unique_operator_anchors(tmp_path, monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_operator_anchor_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    output_file = tmp_path / "reference_content.md"

    module.generate_content_document(
        {
            "Operators": [
                {
                    "id": "op_+",
                    "name": "+",
                    "url": "https://www.tradingview.com/pine-script-reference/v6/#op_+",
                    "content": "Addition operator.",
                },
                {
                    "id": "op_-",
                    "name": "-",
                    "url": "https://www.tradingview.com/pine-script-reference/v6/#op_-",
                    "content": "Subtraction operator.",
                },
                {
                    "id": "op_[]",
                    "name": "[]",
                    "url": "https://www.tradingview.com/pine-script-reference/v6/#op_%5B%5D",
                    "content": "History operator.",
                },
            ]
        },
        "Pine Script V6 Reference",
        output_file,
    )

    text = output_file.read_text(encoding="utf-8")

    assert '<a id="ref-op-2b"></a>' in text
    assert '<a id="ref-op-2d"></a>' in text
    assert '<a id="ref-op-5b-5d"></a>' in text
    assert text.count('<a id="ref-op"></a>') == 0


def test_generate_reference_document_rewrites_fragment_only_reference_links(tmp_path, monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_reference_fragment_links_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    output_file = tmp_path / "reference_content.md"

    module.generate_content_document(
        {
            "Keywords": [
                {
                    "id": "kw_var",
                    "name": "var",
                    "url": "https://www.tradingview.com/pine-script-reference/v6/#kw_var",
                    "content": "See [na](#var_na), [array.new<type>()](#fun_array.new<type>), and [-](#op_-).",
                }
            ]
        },
        "Pine Script V6 Reference",
        output_file,
    )

    text = output_file.read_text(encoding="utf-8")

    assert "[na](#ref-var-na)" in text
    assert "[array.new<type>()](#ref-fun-array-new-3c-type-3e)" in text
    assert "[-](#ref-op-2d)" in text
    assert "](#var_na)" not in text


def test_generate_content_document_adds_item_anchors_and_rewrites_links(tmp_path, monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_document_links_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    output_file = tmp_path / "docs_content.md"

    module.generate_content_document(
        {
            "Language": [
                {
                    "name": "Type system",
                    "url": "https://www.tradingview.com/pine-script-docs/language/type-system/",
                    "content": "See [Arrays](https://www.tradingview.com/pine-script-docs/language/arrays/) and [ta.sma](https://www.tradingview.com/pine-script-reference/v6/#fun_ta.sma).",
                }
            ]
        },
        "Pine Script V6 Documentation",
        output_file,
    )

    text = output_file.read_text(encoding="utf-8")

    assert "- [Type system](#docs-language-type-system)" in text
    assert '<a id="docs-language-type-system"></a>' in text
    assert "[Arrays](#docs-language-arrays)" in text
    assert "[ta.sma](./reference_content.md#ref-fun-ta-sma)" in text


def test_apps_script_markdown_extractor_preserves_rich_markdown(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_apps_script_rich_markdown_test",
        "src/extract_apps_script_content.py",
    )
    soup = BeautifulSoup(
        """
        <main>
          <h1>Title</h1>
          <p><strong>Bold</strong> and <em>italic</em> and <s>gone</s> and <u>under</u>.</p>
          <p>Visit <a href="/apps-script/guides/services">services</a>.</p>
          <blockquote>Quoted text</blockquote>
          <ul><li>First</li><li>Second</li></ul>
          <table><thead><tr><th>Name</th><th>Value</th></tr></thead><tbody><tr><td>A</td><td>1</td></tr></tbody></table>
          <pre><code class="language-javascript">function test() {\n  return 1;\n}</code></pre>
          <img src="/static/logo.png" alt="Logo" />
        </main>
        """,
        "html.parser",
    )

    markdown = module.extract_markdown_from_main(
        soup.select_one("main"),
        base_url="https://developers.google.com/apps-script/overview?hl=es-419",
    )

    assert "# Title" in markdown
    assert "**Bold** and *italic* and ~~gone~~ and <u>under</u>." in markdown
    assert "[services](https://developers.google.com/apps-script/guides/services)" in markdown
    assert "> Quoted text" in markdown
    assert "- First" in markdown
    assert "| Name | Value |" in markdown
    assert "```javascript\nfunction test() {\n  return 1;\n}\n```" in markdown
    assert "![Logo](https://developers.google.com/static/logo.png)" in markdown


def test_pine_docs_navigation_formats_admonitions_after_malformed_code_fence(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_malformed_fence_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Annotations

        `//@returns <description>
        NoteRedundant annotations are automatically ignored.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "**Note:**\nRedundant annotations" in cleaned
    assert "NoteRedundant" not in cleaned


def test_pine_docs_navigation_does_not_format_admonition_words_inside_fences(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_fenced_admonition_words_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Examples

        ```pine
        NoteValue = close
        ImportantValue = open
        ```

        NoteActual prose is still a callout.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "NoteValue = close" in cleaned
    assert "ImportantValue = open" in cleaned
    assert "**Note:** Value = close" not in cleaned
    assert "**Important:** Value = open" not in cleaned
    assert "**Note:**\nActual prose is still a callout." in cleaned


def test_pine_docs_navigation_keeps_inline_backticks_inside_pine_code(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_inline_backticks_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # CW10003

        [Pine Script®](https://tradingview.com/pine-script-docs)
        `//@version=6
        indicator("Conditional history-dependent call demo")
        // If a written call does not execute on a bar, nothing is saved to the time series, and the `[]`
        // operator cannot consistently retrieve a value corresponding to only one bar back.
        previousValue(source) => source[1]
        `
        Note that:
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "[Pine Script®](https://tradingview.com/pine-script-docs)" not in cleaned
    assert cleaned.count("```pine") == 1
    assert cleaned.count("```") == 2
    assert "// If a written call does not execute on a bar, nothing is saved to the time series, and the `[]`" in cleaned
    assert "// operator cannot consistently retrieve" in cleaned
    assert "previousValue(source) => source[1]\n```\nNote that:" in cleaned
    assert "```\n// operator" not in cleaned


def test_pine_docs_navigation_formats_comment_started_pine_blocks(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_comment_started_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Execution model

        `// Add 1 to the `executionNum` value.
        executionNum += 1
        `

        `close > ma`, which may remain true for multiple bars, is prose.
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "```pine\n// Add 1 to the `executionNum` value.\nexecutionNum += 1\n```" in cleaned
    assert "`close > ma`, which may remain true for multiple bars, is prose." in cleaned
    assert "\n`\n" not in cleaned


def test_pine_docs_navigation_formats_literal_pine_blocks(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_literal_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Type system

        `1
        -1
        750
        `

        `#000000
        #FF0000
        `

        `"This is a string"
        'This is another string'
        `
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "```pine\n1\n-1\n750\n```" in cleaned
    assert "```pine\n#000000\n#FF0000\n```" in cleaned
    assert "```pine\n\"This is a string\"\n'This is another string'\n```" in cleaned
    assert "\n`\n" not in cleaned


def test_pine_docs_navigation_formats_tuple_and_expression_blocks(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_tuple_expression_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Type system

        `[op, hi, lo, cl] = request.security(
            syminfo.tickerid, "1D",
            [open, high, low, close]
        )
        `

        `condition ? valueWhenTrue : valueWhenFalse
        `

        `high[10]
        ta.sma(close, 10)[1]
        source * length - source[1]
        close[0] > close[1] and close[1] > close[2]
        `
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "```pine\n[op, hi, lo, cl] = request.security(" in cleaned
    assert "```pine\ncondition ? valueWhenTrue : valueWhenFalse\n```" in cleaned
    assert "high[10]\nta.sma(close, 10)[1]\nsource * length - source[1]" in cleaned
    assert "close[0] > close[1] and close[1] > close[2]\n```" in cleaned
    assert "\n`\n" not in cleaned


def test_pine_docs_navigation_formats_keyword_blocks_with_nbsp(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_nbsp_keyword_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    nbsp = "\u00a0"
    raw_markdown = dedent(
        f"""
        # Loops

        `for{nbsp}index{nbsp}={nbsp}0{nbsp}to{nbsp}array.size(myArray){nbsp}-{nbsp}1
        {nbsp}{nbsp}{nbsp}{nbsp}element{nbsp}={nbsp}array.get(myArray,{nbsp}index)
        `

        `switch
        {nbsp}{nbsp}{nbsp}{nbsp}<expression1>{nbsp}=>{nbsp}<localBlock1>
        {nbsp}{nbsp}{nbsp}{nbsp}=>{nbsp}<localBlock2>
        `

        `export{nbsp}myEma(int{nbsp}x){nbsp}=>
        {nbsp}{nbsp}{nbsp}{nbsp}ta.ema(close,{nbsp}length{nbsp}={nbsp}x)
        `

        `import{nbsp}PineCoders/AllTimeHighLow/1{nbsp}as{nbsp}allTime
        `
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert f"```pine\nfor{nbsp}index" in cleaned
    assert f"```pine\nswitch\n{nbsp}{nbsp}{nbsp}{nbsp}<expression1>" in cleaned
    assert f"```pine\nexport{nbsp}myEma" in cleaned
    assert f"```pine\nimport{nbsp}PineCoders" in cleaned
    assert "\n`\n" not in cleaned


def test_pine_docs_navigation_formats_typed_declarations_and_pseudocode(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_typed_declaration_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Objects

        `type pivotPoint
            int x
            float y
        `

        `pivotPoint foundPoint = na
        foundPoint := pivotPoint.new(time, high)
        `

        `SignalType sigInput = input.enum(SignalType.long, "Signal type")
        `

        `long _startX = System.timeNow()
        <code_line_to_analyze>
        registerPerf(System.timeNow() - _startX, lineX)
        `
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "```pine\ntype pivotPoint\n    int x\n    float y\n```" in cleaned
    assert "```pine\npivotPoint foundPoint = na\nfoundPoint := pivotPoint.new(time, high)\n```" in cleaned
    assert "```pine\nSignalType sigInput = input.enum(SignalType.long, \"Signal type\")\n```" in cleaned
    assert "```pine\nlong _startX = System.timeNow()\n<code_line_to_analyze>" in cleaned
    assert "registerPerf(System.timeNow() - _startX, lineX)\n```" in cleaned
    assert "\n`\n" not in cleaned


def test_pine_docs_navigation_formats_identifier_and_member_expression_blocks(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_identifier_member_code_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Identifiers

        `myVar
        _myVar
        functionName
        3barsDown  // NOT VALID!
        `

        `enumName.fieldName
        `

        `(source - source[1]) + (source - source[2])
        `
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "```pine\nmyVar\n_myVar\nfunctionName\n3barsDown  // NOT VALID!\n```" in cleaned
    assert "```pine\nenumName.fieldName\n```" in cleaned
    assert "```pine\n(source - source[1]) + (source - source[2])\n```" in cleaned
    assert "\n`\n" not in cleaned


def test_pine_docs_navigation_keeps_wrapped_comment_backticks_inside_code(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_wrapped_comment_backtick_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Loops

        `//@version=6
        indicator("Wrapped comment")
        // Use a `while` loop to look backward through close` prices as long as the past `close
        // from `i` bars ago is inside the channel.
        plot(close)
        `
        Note that:
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert cleaned.count("```pine") == 1
    assert cleaned.count("```") == 2
    assert "// Use a `while` loop to look backward through close` prices as long as the past `close" in cleaned
    assert "// from `i` bars ago is inside the channel." in cleaned
    assert "plot(close)\n```\nNote that:" in cleaned
    assert "```\n// from `i`" not in cleaned


def test_pine_docs_navigation_repairs_premature_fence_after_wrapped_comment(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_split_fence_wrapped_comment_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Loops

        ```pine
        //@version=6
        // Use a `while` loop to look backward through close` prices as long as the past `close
        ```
            // from `i` bars ago is inside the channel.
            while close[i] >= channelLow and close[i] <= channelHigh
                i += 1
        `
        Note that:
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert cleaned.count("```pine") == 1
    assert cleaned.count("```") == 2
    assert "// Use a `while` loop to look backward through close` prices as long as the past `close" in cleaned
    assert "// from `i` bars ago is inside the channel." in cleaned
    assert "while close[i] >= channelLow and close[i] <= channelHigh" in cleaned
    assert "i += 1\n```\nNote that:" in cleaned
    assert "```\n    // from `i`" not in cleaned


def test_pine_docs_navigation_rewrites_reference_links_inside_pine_comments(monkeypatch):
    module = load_module(
        monkeypatch,
        "extract_content_comment_reference_link_test",
        "src/extract_content.py",
        crawl4ai=True,
    )
    raw_markdown = dedent(
        """
        # Annotations

        ```pine
        // The [@function](https://www.tradingview.com/pine-script-reference/v6/#an_@function) annotation is flexible.
        // Keep URL literal: https://www.tradingview.com/pine-script-docs/language/type-system/
        f() => int(na)
        ```
        """
    )

    cleaned = module.clean_docs_navigation(raw_markdown)

    assert "[@function](./reference_content.md#ref-an-40-function)" in cleaned
    assert "https://www.tradingview.com/pine-script-reference/v6/#" not in cleaned
    assert "// Keep URL literal: https://www.tradingview.com/pine-script-docs/language/type-system/" in cleaned


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
