#!/usr/bin/env python3
"""Enable or disable GhosTnever Mega Toolkit skills for this Codex profile."""
from __future__ import annotations
import json
import os
import sys
import tempfile
from pathlib import Path

SKILLS = [
    "accessibility-audit", "api-design", "archive-hardening", "browser-automation",
    "bug-hunting", "change-review", "ci-failure-triage", "configuration-management",
    "conflict-resolution", "data-validation", "database-migrations", "database-performance",
    "dependency-audit", "docs-from-code", "feature-planning", "flaky-test-triage",
    "game-mod-support", "git-workflow", "github-actions", "implementation-workflow",
    "incident-postmortem", "incident-response", "integration-test-design", "localization-qa",
    "logging-observability", "mod-compatibility", "performance-analysis",
    "product-usability-review", "pull-request-prep", "python-engineering", "refactoring-plan",
    "release-packaging", "release-readiness", "repo-tour", "secret-redaction",
    "secure-code-review", "seo-audit", "shell-scripting", "sql-query-review",
    "test-engineering", "typescript-node",
]


def settings_path() -> Path:
    base = os.environ.get("CODEX_HOME") or str(Path.home() / ".codex")
    return Path(base).expanduser() / "ghostnever-mega-toolkit" / "settings.json"


def load(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        disabled = data.get("disabled", [])
        if not isinstance(disabled, list) or any(not isinstance(x, str) for x in disabled):
            raise ValueError("поле disabled должно быть списком имён навыков")
        unknown = set(disabled) - set(SKILLS)
        if unknown:
            raise ValueError("неизвестные навыки в настройках: " + ", ".join(sorted(unknown)))
        return set(disabled)
    except (json.JSONDecodeError, OSError, ValueError) as exc:
        raise SystemExit(f"Не удалось прочитать {path}: {exc}")


def save(path: Path, disabled: set[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps({"version": 1, "disabled": sorted(disabled)}, ensure_ascii=False, indent=2) + "\n"
    fd, tmp_name = tempfile.mkstemp(prefix="settings-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(payload)
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def main() -> int:
    args = sys.argv[1:]
    path = settings_path()
    disabled = load(path)
    if not args or args[0] in {"help", "--help", "-h"}:
        print("Команды: list | enable <навык|all> | disable <навык> | reset")
        print(f"Настройки: {path}")
        return 0
    command = args[0].lower()
    if command == "list" and len(args) == 1:
        for name in SKILLS:
            state = "ВЫКЛ" if name in disabled else "ВКЛ"
            print(f"{state:4}  {name}")
        print(f"\nФайл настроек: {path}")
        return 0
    if command == "reset" and len(args) == 1:
        save(path, set())
        print("Все 41 рабочих навыков включены.")
        return 0
    if command in {"enable", "disable"} and len(args) == 2:
        name = args[1].lower()
        if name == "all" and command == "enable":
            disabled.clear()
        elif name not in SKILLS:
            print("Неизвестный навык. Используйте команду list.", file=sys.stderr)
            return 2
        elif command == "enable":
            disabled.discard(name)
        else:
            disabled.add(name)
        save(path, disabled)
        print(("Включён" if command == "enable" else "Выключен") + f" навык: {name}")
        print(f"Сохранено: {path}")
        return 0
    print("Формат: list | enable <навык|all> | disable <навык> | reset", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

