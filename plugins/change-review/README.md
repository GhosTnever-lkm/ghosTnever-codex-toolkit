# Change Review

> Review a diff for correctness and regression risk, reporting only actionable findings.

## Install

In Codex, add the [GhosTnever Codex Toolkit](https://github.com/GhosTnever-lkm/ghosTnever-codex-toolkit) marketplace, then install **Change Review**.

You can also clone this repository and add it as a local marketplace:

```text
codex plugin marketplace add .\path\to\ghosTnever-codex-toolkit
codex plugin add change-review --marketplace ghosTnever-codex-toolkit
```

## Try it

- "Review my current changes for bugs."
- "Check this commit for regression risks."
- "Review the diff around error handling only."

## Scope

This plugin contains a focused Codex skill. It does not install external services or run background processes. Review repository guidance and user authorization before taking actions.

## License

MIT. See [LICENSE](LICENSE).
