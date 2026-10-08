---
name: toolkit-settings
description: Shows how to inspect, enable, or disable individual GhosTnever Mega Toolkit skills using the included settings command. Use when the user asks to configure toolkit modules.
---
# Toolkit Settings

When the user asks to enable or disable a module, update the local settings file directly. Resolve the base directory from `CODEX_HOME`; if it is unset, use `%USERPROFILE%\.codex`. Read `ghostnever-mega-toolkit/settings.json`, preserve any other entries, and update its `disabled` array. Create the file as `{"version":1,"disabled":[...]}` when missing. Disabling should add the skill name once; enabling should remove it; enabling all or resetting should clear the array. Do not disable this `toolkit-settings` guide. Confirm the changed state and path to the user.

The included PowerShell helper works on Windows without Python:

```powershell
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" list
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" disable git-workflow
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" enable git-workflow
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" enable all
& "<plugin-folder>\scripts\mega_toolkit_settings.ps1" reset
```

The settings file is `%CODEX_HOME%\ghostnever-mega-toolkit\settings.json`, or `%USERPROFILE%\.codex\ghostnever-mega-toolkit\settings.json` if `CODEX_HOME` is not set. A missing file means every skill is enabled. A disabled skill must not apply its specialized workflow unless the user explicitly requests a one-time override. Settings remain on the device and are not sent over the network. A Python helper is also included for cross-platform use.

Codex currently does not expose an independent graphical toggle for every skill, so this helper provides the per-skill controls.

