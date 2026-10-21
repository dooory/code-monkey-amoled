# Code Monkey AMOLED for Codex CLI

Visual Studio syntax colors on black, matching the VS Code port. Codex's theme setting controls code highlighting. Your terminal supplies the main background, font, selection and most interface colors.

## Install

1. Apply the [Windows Terminal theme](../windows-terminal/README.md), or set your terminal to black with `#dcdcdc` text and `#264f78` selection. [Install Inconsolata Nerd Font Mono](../FONTS.md) and select it in your terminal.
2. Copy [code-monkey-amoled.tmTheme](code-monkey-amoled.tmTheme) into `$CODEX_HOME/themes/`. Create the folder if needed. When `CODEX_HOME` is unset, use `~/.codex/themes/`, normally `%USERPROFILE%\.codex\themes\` on Windows.
3. Restart Codex and run `/theme`. Choose `Code Monkey AMOLED` from the picker.

Alternatively, merge [config.toml](config.toml) into `$CODEX_HOME/config.toml`, normally `~/.codex/config.toml`. Add `theme = "code-monkey-amoled"` to your existing `[tui]` table. Keep its other settings and avoid creating a second `[tui]` table.

## Appearance and customization

The theme copies the VS Code port's TextMate token rules into the `.tmTheme` format. Codex uses its own syntax grammars, so individual tokens can differ from VS Code. VS Code semantic highlighting and strikethrough rules are not included.

Edit the first `settings` dictionary for the black background, text and selection colors. Edit subsequent scoped dictionaries for syntax colors. These values affect only surfaces Codex renders through its syntax highlighter. Prompt boxes, status indicators, terminal font and window corners are controlled by Codex or the terminal.

See the official OpenAI documentation for [`/theme`](https://developers.openai.com/codex/cli/slash-commands#choose-a-syntax-theme-with-theme) and [`tui.theme`](https://developers.openai.com/codex/config-reference). Custom `.tmTheme` loading and the `themes/` path were checked against the installed Codex CLI 0.163.0. Live rendering has not been verified.

## Uninstall

Choose another theme with `/theme`, then remove the copied `.tmTheme` file. If configured manually, remove or change only `tui.theme`.

## License

MIT, based on Code Monkey by mmuffins and Microsoft's Visual Studio syntax colors. See [LICENSE.md](LICENSE.md).
