from __future__ import annotations

import json
import os
import runpy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PLUGIN_ROOT.parents[1]
SETTINGS_SCRIPT = PLUGIN_ROOT / "scripts" / "mega_toolkit_settings.py"
SKILL_ROOT = PLUGIN_ROOT / "skills"


class ToolkitSettingsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.env = os.environ.copy()
        self.env["CODEX_HOME"] = self.temp_dir.name
        self.settings_path = (
            Path(self.temp_dir.name) / "ghostnever-mega-toolkit" / "settings.json"
        )

    def run_helper(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SETTINGS_SCRIPT), *args],
            capture_output=True,
            text=True,
            env=self.env,
            check=False,
        )

    def test_manifest_and_helpers_match_the_real_skill_directories(self) -> None:
        helper_skills = set(runpy.run_path(str(SETTINGS_SCRIPT))["SKILLS"])
        real_task_skills = {
            path.name
            for path in SKILL_ROOT.iterdir()
            if path.is_dir() and path.name != "toolkit-settings"
        }
        all_skill_directories = {path.name for path in SKILL_ROOT.iterdir() if path.is_dir()}
        manifest = json.loads(
            (PLUGIN_ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        manifest_skills = {Path(path).name for path in manifest["skills"]}
        repository_version = (REPOSITORY_ROOT / "VERSION").read_text(encoding="utf-8").strip()

        self.assertEqual(41, len(real_task_skills))
        self.assertEqual(real_task_skills, helper_skills)
        self.assertEqual(all_skill_directories, manifest_skills)
        self.assertEqual(41, len(helper_skills))
        self.assertEqual(repository_version, manifest["version"])

        self.assertIn("41 practical skills", (REPOSITORY_ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn(
            "41 practical workflow skills",
            (PLUGIN_ROOT / "README.md").read_text(encoding="utf-8"),
        )
        for changelog in (
            REPOSITORY_ROOT / "CHANGELOG.md",
            PLUGIN_ROOT / "CHANGELOG.md",
        ):
            self.assertIn(f"## {repository_version} - ", changelog.read_text(encoding="utf-8")[:160])

    def test_missing_settings_lists_every_skill_as_enabled(self) -> None:
        result = self.run_helper("list")
        self.assertEqual(0, result.returncode, result.stderr)
        rows = [line for line in result.stdout.splitlines() if line.startswith(("ВКЛ", "ВЫКЛ"))]
        self.assertEqual(41, len(rows))
        self.assertTrue(all(line.startswith("ВКЛ") for line in rows))
        self.assertFalse(self.settings_path.exists())

    def test_enable_disable_and_enable_all_preserve_other_settings(self) -> None:
        self.settings_path.parent.mkdir(parents=True)
        original = {
            "version": 17,
            "disabled": ["docs-from-code"],
            "appearance": {"theme": "dark", "keep": True},
        }
        self.settings_path.write_text(json.dumps(original), encoding="utf-8")

        result = self.run_helper("disable", "api-design")
        self.assertEqual(0, result.returncode, result.stderr)
        saved = json.loads(self.settings_path.read_text(encoding="utf-8"))
        self.assertEqual(["api-design", "docs-from-code"], saved["disabled"])
        self.assertEqual({"theme": "dark", "keep": True}, saved["appearance"])
        self.assertEqual(1, saved["version"])

        result = self.run_helper("enable", "docs-from-code")
        self.assertEqual(0, result.returncode, result.stderr)
        saved = json.loads(self.settings_path.read_text(encoding="utf-8"))
        self.assertEqual(["api-design"], saved["disabled"])
        self.assertEqual({"theme": "dark", "keep": True}, saved["appearance"])

        result = self.run_helper("enable", "all")
        self.assertEqual(0, result.returncode, result.stderr)
        saved = json.loads(self.settings_path.read_text(encoding="utf-8"))
        self.assertEqual([], saved["disabled"])
        self.assertEqual({"theme": "dark", "keep": True}, saved["appearance"])

    def test_unknown_skill_is_rejected_without_creating_settings(self) -> None:
        result = self.run_helper("disable", "not-a-real-skill")
        self.assertEqual(2, result.returncode)
        self.assertIn("Неизвестный навык", result.stderr)
        self.assertFalse(self.settings_path.exists())

    def test_invalid_existing_settings_fail_without_overwriting_the_file(self) -> None:
        self.settings_path.parent.mkdir(parents=True)
        original = "{ definitely not json"
        self.settings_path.write_text(original, encoding="utf-8")

        result = self.run_helper("enable", "git-workflow")
        self.assertEqual(1, result.returncode)
        self.assertIn("Не удалось прочитать", result.stderr)
        self.assertEqual(original, self.settings_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
