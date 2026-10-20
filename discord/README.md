# Code Monkey AMOLED for Discord

A pure-black Discord theme for Equicord, ported from the Code Monkey AMOLED MediaMonkey skin. It uses the skin's black and near-black surfaces, blue highlights and selection color, square corners and the Inconsolata font.

## Install

1. Run the installer, which finds Equicord's themes folder and copies the theme there:

   ```powershell
   powershell -ExecutionPolicy Bypass -File .\install.ps1
   ```

   Or copy `code-monkey-amoled.theme.css` into the folder by hand (**Settings > Equicord > Themes > Open Themes Folder**).
2. Enable **Code Monkey AMOLED** in the Themes tab.
3. Set Discord's appearance to **Dark** (or Midnight).

## Customize

Edit the variables at the top of the theme:

| Variable | Default | Purpose |
| --- | --- | --- |
| `--cm-highlight` | `#1c97ea` | Links, hover accents |
| `--cm-highlight2` | `#007acc` | Buttons, mentions, active channel edge |
| `--cm-selected` | `#264f78` | Selected channel and text selection |
| `--cm-font` | Inconsolata | UI font |
| `--cm-letter-spacing` | `0.3px` | Text tracking |
| `--cm-radius` | `0px` | Corner radius |

Inconsolata loads from Google Fonts. Offline, it falls back to Consolas.

## Source and license

Based on [mmuffins/mediamonkey-codemonkey](https://github.com/mmuffins/mediamonkey-codemonkey) via the Code Monkey AMOLED skin. MIT license in `LICENSE.md`.
