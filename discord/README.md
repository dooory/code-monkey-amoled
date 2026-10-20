# Code Monkey AMOLED for Discord

A pure-black Discord theme for Equicord, ported from the Code Monkey AMOLED MediaMonkey skin. It uses the skin's black and near-black surfaces, blue highlights and selection color, square corners and the Inconsolata font.

## Install

1. In Discord, open **Settings > Equicord > Themes > Online Themes**.
2. Paste this link and save:

   ```
   https://raw.githubusercontent.com/dooory/code-monkey-amoled/main/discord/code-monkey-amoled.theme.css
   ```
3. Set Discord's appearance to **Dark** (or Midnight).

The theme loads from this repository, so updates pushed to `main` apply the next time Discord starts.

## Customize

Override the theme's variables in **Settings > Equicord > Themes > Edit QuickCSS**:

```css
:root {
    --cm-highlight: #1c97ea !important;
    --cm-letter-spacing: 0.3px !important;
}
```

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
