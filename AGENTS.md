# AGENTS.md

## Repo Shape
- This is a Python documentation scraper/generator, not a packaged app. Source scripts live in `src/`; generated Markdown and URL indexes live in `output/`.
- Main entrypoint: `python src/run_all.py`. It runs URL extraction before content extraction for both Pine Script and Google Apps Script.
- `output/*.md` files are generated artifacts. They can be large; inspect with `grep` or targeted `read` offsets instead of loading whole files.
- `ruvector.db` is currently untracked. Do not delete or rewrite it unless the user explicitly asks.

## Setup And Commands
- Prefer Python 3.10-3.12 for full scraper runs. Local Python 3.14 can run offline checks, but dependency resolution may force native source builds on Windows (observed with Crawl4AI's `lxml` dependency).
- Install dependencies: `python setup.py`. This runs `pip install -r requirements.txt` and `python -m playwright install chromium`.
- Manual setup: `pip install -r requirements.txt` then `python -m playwright install chromium`.
- Full extraction: `python src/run_all.py`.
- Pine URL index only: `python src/extract_urls.py`.
- Pine content only: `python src/extract_content.py`; run `extract_urls.py` first because it reads `output/docs_urls.md`.
- Apps Script URL index only: `python src/extract_apps_script_urls.py`.
- Apps Script content only: `python src/extract_apps_script_content.py`; run `extract_apps_script_urls.py` first because it reads `output/apps_script_urls.md`.
- CI workflow `.github/workflows/python-package-conda.yml` references `environment.yml`, but that file is absent. Trust `requirements.txt` and `setup.py` for local setup until CI is fixed.
- No tests are currently present. CI would run `pytest` after installing pytest, but a focused syntax/lint check is more realistic for small edits.

## Runtime Gotchas
- Scrapers need network access to `tradingview.com` and `developers.google.com`, plus Playwright Chromium.
- Full extraction can be slow and overwrites generated files in `output/`; do not run it for unrelated edits.
- `src/extract_content.py` uses Playwright for the Pine reference page and Crawl4AI for Pine docs pages.
- Apps Script extraction intentionally removes Google devsite sidebar/nav selectors such as `.devsite-on-this-page`, `.devsite-toc`, `nav`, and `aside`.

## Code Conventions
- Keep scripts simple: module-level constants, `Path(__file__).resolve().parent.parent` for repo root, `OUTPUT_DIR.mkdir(parents=True, exist_ok=True)`, UTF-8 reads/writes.
- Preserve source navigation order when generating URL and content documents.
- For async scripts, keep the existing `async def main()` plus `if __name__ == "__main__": asyncio.run(main())` pattern.
- Be conservative with extraction filters. Sidebar/footer cleanup is source-specific and easy to over-trim.

## Skill And Context Rules
- Start each task by checking applicable Superpowers skills. If `using-superpowers` was already injected by the user, do not load it again.
- Search memory before repo-changing work when a memory tool is available. If the memory service is down, note it briefly and continue.
- Use `graphify` for questions about repo/file relationships, architecture maps, or dependency flow, especially if `graphify-out/` exists. For narrow file lookup, use `glob`/`grep` first.
- Use `caveman` or terse mode only when the user asks for token savings/brevity or context is tight; do not let compression obscure command order or safety warnings.
- Use planning skills for multi-step implementation plans, not for small direct edits like this instruction file.
- Use debugging/TDD skills when fixing failures or adding behavior; otherwise keep verification proportional to this small scraper repo.
- Prefer `grep` and targeted `read` slices for `output/reference_content.md` and `output/docs_content.md`; avoid full-file reads unless explicitly needed.
- For ECC/OpenCode skill configuration tasks, use ECC-oriented skills such as `ecc-guide`, `agent-sort`, or `configure-ecc`; do not add ECC boilerplate to scraper code.
- Model routing: keep high-reasoning models for architecture, CI failures, dependency/version decisions, and fragile scraper refactors. Use cheaper/faster variants for grep-style lookup, formatting, rote summaries, and single-file mechanical edits.
