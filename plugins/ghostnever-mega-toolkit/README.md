# GhosTnever Mega Toolkit

One Codex plugin with 41 practical workflow skills and local controls to enable or disable each workflow. It covers the full path from understanding a codebase and planning work to implementation, review, release, and long-term maintenance.

## Skills

| Area | Included workflows |
| --- | --- |
| Understand and plan | Repository Tour, Feature Planning, Implementation Workflow, Refactoring Plan |
| Build and debug | Bug Hunting, Python Engineering, TypeScript and Node.js Engineering, Shell Scripting |
| Git and collaboration | Git Workflow, Pull Request Preparation, Conflict Resolution |
| Test and quality | Test Engineering, Integration Test Design, Flaky Test Triage, Data Validation, Localization QA |
| Review and security | Change Review, Secure Code Review, Dependency Audit, Archive Hardening, Secret Redaction |
| Product and interfaces | API Design, Product Usability Review, Accessibility Audit, SEO Audit, Browser Automation |
| Data and reliability | Database Migrations, Database Performance, SQL Query Review, Logging and Observability, Incident Response, Incident Postmortem, CI Failure Triage |
| Ship and maintain | GitHub Actions, Release Readiness, Release Packaging, Docs from Code, Configuration Management |
| Game modding | Game Mod Support, Mod Compatibility |
| Toolkit control | Toolkit Settings |

The toolkit includes 41 task skills; `Toolkit Settings` is the built-in helper guide for the controls.

## Install in Codex

Add the [GhosTnever Codex Toolkit marketplace](https://github.com/GhosTnever-lkm/ghosTnever-codex-toolkit) and install `ghostnever-mega-toolkit` from the plugin browser. With the CLI:

```powershell
codex plugin marketplace add https://github.com/GhosTnever-lkm/ghosTnever-codex-toolkit.git --ref main
codex plugin add ghostnever-mega-toolkit --marketplace ghosTnever-codex-toolkit
```

## Enable and disable skills

In Codex, ask to enable or disable a workflow by name; the always-on Toolkit Settings skill updates the local setting. On Windows, the included PowerShell helper works without Python:

```powershell
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" list
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" disable git-workflow
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" enable git-workflow
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" enable all
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" reset
```

`mega_toolkit_settings.py` is also available for cross-platform use when Python 3 is installed.

The settings file is local: `%CODEX_HOME%\ghostnever-mega-toolkit\settings.json`, or `%USERPROFILE%\.codex\ghostnever-mega-toolkit\settings.json` if `CODEX_HOME` is unset. A missing file means all skills are enabled. The helper supports per-skill enable and disable, listing, and reset. Codex does not currently expose individual native graphical toggles; each skill's instructions respect this local setting, and a user can request a one-time override.

## How it works

This plugin contains instruction-only skills. It adds no background service, external account connection, or network permission. Review-oriented skills are read-only by default; editing, release, deployment, and external publishing still follow the user's request and repository guidance.

## Support / Pro Version

The toolkit is free and open source under the MIT License. Optional support: [Boosty](https://boosty.to/azizazimov) · [Buy Me a Coffee](https://www.buymeacoffee.com/azizazimov8) · [Gumroad](https://azimovian22.gumroad.com/). There is no paid Pro edition for this plugin at this time.

## License

MIT. See [LICENSE](LICENSE).
