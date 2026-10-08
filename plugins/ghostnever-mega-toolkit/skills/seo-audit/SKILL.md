---
name: seo-audit
description: Audits a website's discoverability basics using its actual HTML, metadata, sitemap, and rendered pages. Use when asked to improve search visibility.
---
# SEO Audit

Inspect the live or local page, canonical URLs, robots rules, sitemap, structured data, and actual page content. Search engine indexing is not guaranteed by metadata alone.

## Check
- Descriptive page title, coherent description, canonical, language, and indexability.
- Correct redirects, robots.txt, sitemap URLs, and HTTP status for important pages.
- Unique visible page content and internal links that crawlers can follow.
- Valid structured data that matches page content; no invented ratings or claims.
- Mobile usability and loading issues that block content.

Distinguish implemented technical signals from verified indexing. Never promise ranking or search appearance; name the exact pages checked and remaining third-party steps.

## Toolkit module setting

Before following this workflow, check `%CODEX_HOME%/ghostnever-mega-toolkit/settings.json`; if `CODEX_HOME` is unset, check `%USERPROFILE%/.codex/ghostnever-mega-toolkit/settings.json`. If the JSON `disabled` array contains `seo-audit`, do not apply this skill's specialized workflow unless the user explicitly asks to use it for the current task. If the file is missing or the name is absent from `disabled`, this skill is enabled. The included `scripts/mega_toolkit_settings.py` helper manages this file.
