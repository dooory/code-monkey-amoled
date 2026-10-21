# Code Monkey AMOLED

A pure-black AMOLED take on the [Code Monkey](https://github.com/mmuffins/mediamonkey-codemonkey) MediaMonkey skin, ported to other apps: black and near-black surfaces, Visual Studio blue highlights, square corners and Inconsolata Nerd Font Mono.

| App | Folder | Install |
| --- | --- | --- |
| MediaMonkey 2024 | [`mediamonkey/`](mediamonkey/) | [README](mediamonkey/README.md) |
| VS Code | [`vscode/`](vscode/) | [README](vscode/README.md) |
| Discord (Equicord) | [`discord/`](discord/) | [README](discord/README.md) |
| Vivaldi | [`vivaldi/`](vivaldi/) | [README](vivaldi/README.md) |
| Obsidian | [`obsidian/`](obsidian/) | [README](obsidian/README.md) |
| Windows Terminal | [`windows-terminal/`](windows-terminal/) | [README](windows-terminal/README.md) |
| Codex CLI | [`codex-cli/`](codex-cli/) | [README](codex-cli/README.md) |
| Claude Code | [`claude-code/`](claude-code/) | [README](claude-code/README.md) |
| Roblox Studio (Roblox ModLoader) | [`rml/`](rml/) | [README](rml/README.md) |

## Font

[Install Inconsolata Nerd Font Mono](FONTS.md) for matching text and Nerd Font symbols across the ports. MediaMonkey and Discord download it automatically when it is not installed. Other apps use the installed font through the settings described in their READMEs. VS Code and Roblox Studio support editor fonts separately from their UI fonts.

## Palette

| | | | |
| --- | --- | --- | --- |
| `#000000` base | `#080808` secondary | `#111111` tertiary | `#181818` hover |
| `#303030` border | `#454545` contrast | `#dcdcdc` text | `#999999` muted text |
| `#1c97ea` highlight | `#007acc` highlight 2 | `#264f78` selection | |

The full palette, font settings and a porting checklist for new apps are in [SPEC.md](SPEC.md).

## License

MIT, based on Code Monkey by mmuffins. See [LICENSE.md](LICENSE.md). Each app folder carries its own copy of the license because each ships as a separate package. The VS Code and Windows Terminal licenses also cover the Visual Studio colors from Microsoft.
