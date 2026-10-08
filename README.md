# GhosTnever Codex Toolkit

Focused Codex plugins for everyday software work, from understanding a codebase to reviewing changes, debugging CI, planning releases, and maintaining documentation. The Mega Toolkit combines 21 practical skills in one plugin; the focused plugins remain available when you want a smaller install.

## Plugins

| Plugin | What it helps with |
| --- | --- |
| [Repository Onboarding](plugins/repo-onboarding) | Map an unfamiliar codebase, its entry points, tests, and verified setup commands. |
| [Change Review](plugins/change-review) | Find concrete correctness and regression issues in a requested diff. |
| [CI Failure Guide](plugins/ci-failure-guide) | Trace build and test failures to a focused next check. |
| [Release Checklist](plugins/release-checklist) | Review release readiness and draft notes without publishing automatically. |
| [Docs from Code](plugins/docs-from-code) | Write developer docs grounded in the current implementation. |
| [GhosTnever Mega Toolkit](plugins/ghostnever-mega-toolkit) | 21 skills for planning, coding, debugging, testing, security, performance, APIs, databases, accessibility, GitHub Actions, releases, and game mods. |

## Add this marketplace

In Codex, add this GitHub repository as a plugin marketplace. Then install a plugin by its ID from the marketplace browser. With the CLI:

```powershell
codex plugin marketplace add https://github.com/GhosTnever-lkm/ghosTnever-codex-toolkit.git --ref main
codex plugin list
codex plugin add repo-onboarding --marketplace ghosTnever-codex-toolkit
```

Swap `repo-onboarding` for any plugin ID in the table. To install the all-in-one toolkit, use `ghostnever-mega-toolkit`. Restart Codex if it asks you to reload plugins.

## Design notes

- Skills only: no network service, credentials, or background process.
- Read-only review by default. Commits, releases, deployments, and broad edits require a separate user request.
- Each skill distinguishes inspected evidence from inference and unverified checks.
- Plugin manifests and marketplace metadata live beside the source for easy inspection.

## Validate locally

```powershell
codex plugin marketplace add .\work\codex-plugins\ghosTnever-codex-toolkit
codex plugin list
codex plugin marketplace remove ghosTnever-codex-toolkit
```

The local marketplace check adds and removes only this toolkit marketplace entry; it does not install plugins.

## License

MIT. See [LICENSE](LICENSE).
