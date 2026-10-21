# Code Monkey AMOLED for Claude Code

Near-black message panels, blue accents and grey text. Status messages and agent labels use the Visual Studio syntax palette to keep success, warnings and errors distinct.

## Install

1. Apply the [Windows Terminal theme](../windows-terminal/README.md), or set your terminal to black with `#dcdcdc` text and `#264f78` selection. [Install Inconsolata Nerd Font Mono](../FONTS.md) and select it in your terminal.
2. Copy [code-monkey-amoled.json](code-monkey-amoled.json) into `~/.claude/themes/`, normally `%USERPROFILE%\.claude\themes\` on Windows. Create the folder if needed.
3. Run `/theme` in Claude Code and select `Code Monkey AMOLED`. Restart once if you created the `themes` folder while Claude Code was running.

Use a Claude Code version with custom theme support. The format follows the [official custom theme reference](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme), checked with version 2.1.305 installed. Live rendering has not been verified.

## Appearance and customization

Edit `overrides` in the JSON file. Changes reload automatically after the themes folder has been detected. The main accents are `#007acc` and `#1c97ea`. `selectionBg` is `#264f78` in fullscreen mode. Your terminal controls normal text selection, the main background, font and window shape.

Message hover, conversation text selection and the composer sidebar colors apply only in fullscreen mode. Other message backgrounds also apply in the default renderer. Diff backgrounds use distinct near-black and grey shades, with stronger word highlights. Use the diff's addition and deletion markers to distinguish changes.

Unspecified tokens, including code syntax colors and the ultrathink rainbow, inherit Claude Code's built-in dark preset. This format does not expose TextMate syntax rules or corner styling.

## Uninstall

Choose a built-in theme with `/theme`, then remove the copied JSON file.

## License

MIT, based on Code Monkey by mmuffins and Microsoft's Visual Studio colors. See [LICENSE.md](LICENSE.md).
