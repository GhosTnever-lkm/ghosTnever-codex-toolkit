---
name: toolkit-settings
description: Shows how to inspect, enable, or disable individual GhosTnever Mega Toolkit skills using the included settings command. Use when the user asks to configure toolkit modules.
---
# Toolkit Settings

Use `scripts/mega_toolkit_settings.py` from the installed plugin directory to manage modules. Run it with Python 3:

```powershell
python <plugin-folder>\scripts\mega_toolkit_settings.py list
python <plugin-folder>\scripts\mega_toolkit_settings.py disable git-workflow
python <plugin-folder>\scripts\mega_toolkit_settings.py enable git-workflow
python <plugin-folder>\scripts\mega_toolkit_settings.py enable all
python <plugin-folder>\scripts\mega_toolkit_settings.py reset
```

The settings file is `%CODEX_HOME%\ghostnever-mega-toolkit\settings.json`, or `%USERPROFILE%\.codex\ghostnever-mega-toolkit\settings.json` if `CODEX_HOME` is not set. A missing file means every skill is enabled. Disabling a skill prevents the toolkit from applying that specialized workflow; the user may explicitly request a one-time override. `reset` restores the default with all skills enabled. No settings are sent over the network.

Codex currently does not expose an independent graphical toggle for every skill, so this helper provides the per-skill controls.

