from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "ghostnever-mega-toolkit"
SCRIPTS = PLUGIN / "scripts"
SPEC = importlib.util.spec_from_file_location(
    "mega_toolkit_settings", SCRIPTS / "mega_toolkit_settings.py"
)
assert SPEC and SPEC.loader
SETTINGS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SETTINGS)


class ToolkitCatalogTests(unittest.TestCase):
    def test_version_and_plugin_skill_catalog_match(self) -> None:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        manifest = json.loads((PLUGIN / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
        portable_manifest = json.loads((PLUGIN / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(version, manifest["version"])
        self.assertEqual(version, portable_manifest["version"])

        declared = {Path(path).name for path in manifest["skills"]}
        actual = {path.name for path in (PLUGIN / "skills").iterdir() if path.is_dir()}
        self.assertEqual(actual, declared)
        task_skills = actual - {"toolkit-settings"}
        self.assertEqual(41, len(task_skills))
        self.assertEqual(task_skills, set(SETTINGS.SKILLS))

        powershell = (SCRIPTS / "mega_toolkit_settings.ps1").read_text(encoding="utf-8")
        block = re.search(r"\$skillNames\s*=\s*@\((.*?)\)", powershell, re.DOTALL)
        self.assertIsNotNone(block)
        powershell_skills = set(re.findall(r"'([^']+)'", block.group(1) if block else ""))
        self.assertEqual(task_skills, powershell_skills)

    def test_every_skill_has_matching_frontmatter_and_settings_guard(self) -> None:
        for name in SETTINGS.SKILLS:
            with self.subTest(skill=name):
                text = (PLUGIN / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                frontmatter = re.match(r"\A---\s*\nname:\s*([^\n]+)", text)
                self.assertIsNotNone(frontmatter)
                self.assertEqual(name, frontmatter.group(1).strip() if frontmatter else None)
                self.assertIn(f"disabled` array contains `{name}`", text)
                self.assertIn("settings.json", text)

    def test_local_marketplace_validation_uses_repository_root(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("codex plugin marketplace add .", readme)
        self.assertNotIn(".\\work\\codex-plugins\\ghosTnever-codex-toolkit", readme)

    def test_skill_toggle_scope_is_clear_in_all_docs(self) -> None:
        sentence = (
            "These switches do not uninstall or hide a skill from the installed plugin catalog; "
            "they only control whether its specialized workflow is applied."
        )
        documents = (
            ROOT / "README.md",
            PLUGIN / "README.md",
            PLUGIN / "skills" / "toolkit-settings" / "SKILL.md",
        )
        for path in documents:
            with self.subTest(document=path.relative_to(ROOT)):
                self.assertIn(sentence, path.read_text(encoding="utf-8"))


class PythonSettingsCommandTests(unittest.TestCase):
    def run_helper(self, home: Path, *args: str) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["CODEX_HOME"] = str(home)
        env.pop("USERPROFILE", None)
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "mega_toolkit_settings.py"), *args],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
        )

    def test_disable_enable_all_and_reset_preserve_other_settings(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            path = home / "ghostnever-mega-toolkit" / "settings.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps({"version": 1, "disabled": [], "custom": {"theme": "dark"}}),
                encoding="utf-8",
            )

            result = self.run_helper(home, "disable", "git-workflow")
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertIn("Выключен навык: git-workflow", result.stdout)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(["git-workflow"], saved["disabled"])
            self.assertEqual({"theme": "dark"}, saved["custom"])

            cases = (
                (("enable", "git-workflow"), []),
                (("disable", "git-workflow"), ["git-workflow"]),
                (("enable", "all"), []),
                (("disable", "python-engineering"), ["python-engineering"]),
                (("reset",), []),
            )
            for command, expected_disabled in cases:
                with self.subTest(command=command):
                    result = self.run_helper(home, *command)
                    self.assertEqual(0, result.returncode, result.stderr)
                    saved = json.loads(path.read_text(encoding="utf-8"))
                    self.assertEqual(expected_disabled, saved["disabled"])
                    self.assertEqual({"theme": "dark"}, saved["custom"])

    def test_rejects_unknown_skill_without_changing_settings(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            path = home / "ghostnever-mega-toolkit" / "settings.json"
            path.parent.mkdir(parents=True)
            original = json.dumps({"version": 1, "disabled": []})
            path.write_text(original, encoding="utf-8")
            result = self.run_helper(home, "disable", "not-a-skill")
            self.assertEqual(2, result.returncode)
            self.assertEqual(original, path.read_text(encoding="utf-8"))


class PowerShellSettingsCommandTests(unittest.TestCase):
    @unittest.skipUnless(os.name == "nt", "PowerShell helper is Windows-specific")
    def test_powershell_helper_updates_and_preserves_settings(self) -> None:
        shell = shutil.which("pwsh") or shutil.which("powershell")
        self.assertIsNotNone(shell)
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            path = home / "ghostnever-mega-toolkit" / "settings.json"
            path.parent.mkdir(parents=True)
            path.write_text(
                json.dumps({"version": 1, "disabled": [], "custom": {"theme": "dark"}}),
                encoding="utf-8",
            )

            def run(*args: str) -> subprocess.CompletedProcess[str]:
                env = os.environ.copy()
                env["CODEX_HOME"] = str(home)
                command = [shell, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", str(SCRIPTS / "mega_toolkit_settings.ps1"), *args]
                return subprocess.run(command, check=False, capture_output=True, text=True, env=env)

            result = run("disable", "git-workflow")
            self.assertEqual(0, result.returncode, result.stderr)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(["git-workflow"], saved["disabled"])
            self.assertEqual({"theme": "dark"}, saved["custom"])

            result = run("enable", "all")
            self.assertEqual(0, result.returncode, result.stderr)
            saved = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual([], saved["disabled"])
            self.assertEqual({"theme": "dark"}, saved["custom"])

    @unittest.skipUnless(os.name == "nt", "PowerShell helper is Windows-specific")
    def test_reset_rejects_extra_skill_name_without_modifying_settings(self) -> None:
        shell = shutil.which("pwsh") or shutil.which("powershell")
        self.assertIsNotNone(shell)
        with tempfile.TemporaryDirectory() as temporary:
            home = Path(temporary)
            path = home / "ghostnever-mega-toolkit" / "settings.json"
            path.parent.mkdir(parents=True)
            original = {"version": 1, "disabled": ["git-workflow"], "custom": {"theme": "dark"}}
            path.write_text(json.dumps(original), encoding="utf-8")
            env = os.environ.copy()
            env["CODEX_HOME"] = str(home)
            result = subprocess.run(
                [shell, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-File", str(SCRIPTS / "mega_toolkit_settings.ps1"), "reset", "git-workflow"],
                check=False, capture_output=True, text=True, env=env,
            )
            self.assertNotEqual(0, result.returncode)
            self.assertEqual(original, json.loads(path.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
