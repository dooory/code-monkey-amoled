# Code Monkey AMOLED for Windows Terminal

A pure-black Windows Terminal theme with near-black tabs, blue accents and `#264f78` selection. The 16 ANSI colors use the Visual Studio colors already present in the VS Code port.

## Install

1. [Install Inconsolata Nerd Font Mono](../FONTS.md). Inconsolata and Consolas are fallbacks, without the full Nerd Font symbol set.
2. In Windows Terminal, open **Settings > Open JSON file** and back up your settings.
3. Merge [settings.json](settings.json) into your existing settings:
   - Append its `schemes` entry to your `schemes` array.
   - Append its `themes` entry to your `themes` array, creating the array if needed.
   - Set the top-level `theme` to `"Code Monkey AMOLED"`.
   - Copy its `profiles.defaults` properties into your existing `profiles.defaults` object.
4. Save the file. Restart Terminal if the newly installed font does not appear.

Keep your existing profiles, default profile, keybindings and other settings. This file is a merge snippet, not a replacement for your settings. If reinstalling, replace the entries named `Code Monkey AMOLED` instead of adding duplicates.

The defaults apply to all profiles. Profile-specific appearance settings take precedence, including `colorScheme`, `font`, background images and `unfocusedAppearance`. Remove conflicting overrides from profiles you want to match. To theme only one profile, copy the `profiles.defaults` properties into that profile instead.

## Appearance

The font is Inconsolata Nerd Font Mono at 9.75pt, equivalent to the spec's 13px, with weight 400. Its symbols fit one character cell. Terminal keeps its normal cell spacing. The patched font is static, so no variable width axis is set.

The snippet disables transparency, acrylic, Mica and background images for solid black terminal panes. The window frame is blue on Windows 11. Terminal keeps its native control colors, hover effects and rounded corners because custom themes do not expose all of those settings.

## Changing colors

Edit the entry under `schemes` to change terminal colors. `blue` is `#007acc`, `brightBlue` is `#1c97ea`, and `selectionBackground` is `#264f78`. Programs that emit explicit RGB colors can override the ANSI palette.

Edit the entry under `themes` to change the tabs and window frame. See [Microsoft's theme reference](https://learn.microsoft.com/windows/terminal/customize-settings/themes) for the supported settings.

## Source and license

Based on [Code Monkey](https://github.com/mmuffins/mediamonkey-codemonkey) by mmuffins, with Visual Studio colors from Microsoft's VS Code themes. MIT license in [LICENSE.md](LICENSE.md). The separately installed Nerd Font uses the [SIL Open Font License](https://github.com/ryanoasis/nerd-fonts/blob/v3.4.0/patched-fonts/Inconsolata/OFL.txt).
