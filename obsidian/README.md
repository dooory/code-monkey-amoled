# Code Monkey AMOLED for Obsidian

A pure-black Obsidian theme ported from the Code Monkey AMOLED MediaMonkey skin. It uses the skin's black and near-black surfaces, blue highlights and selection color, square corners, Inconsolata Nerd Font Mono and VS Code Dark+ code-block colors.

## Install

1. Copy this folder's `manifest.json` and `theme.css` into `<vault>/.obsidian/themes/Code Monkey AMOLED/`. The folder name must match the theme name:

   ```powershell
   $dest = "<vault>\.obsidian\themes\Code Monkey AMOLED"
   New-Item -ItemType Directory -Force $dest
   Copy-Item manifest.json, theme.css $dest
   ```
2. In Obsidian, open **Settings > Appearance**, set **Base color scheme** to **Dark**, and pick **Code Monkey AMOLED** under **Themes > Manage**.

The theme only styles dark mode.

## Font

[Install Inconsolata Nerd Font Mono](../FONTS.md). The theme uses it for the interface, editor text and code. Fonts chosen under **Settings > Appearance > Font** override the theme's. Text size stays under Obsidian's own **Font size** setting.

## Customize

Obsidian's **Accent color** setting has no effect, because the theme uses three accent colors. Change them in a CSS snippet instead: save this as `<vault>/.obsidian/snippets/code-monkey.css` and turn it on under **Settings > Appearance > CSS snippets**.

```css
.theme-dark {
    --cm-highlight: #1c97ea;
    --cm-highlight2: #007acc;
    --cm-selected: #264f78;
}
```

| Variable | Default | Purpose |
| --- | --- | --- |
| `--cm-highlight` | `#1c97ea` | Links, tags, hover accents |
| `--cm-highlight2` | `#007acc` | Buttons, checkboxes, focus borders, active tab and file edge |
| `--cm-selected` | `#264f78` | Active file and text selection |
| `--cm-font` | Inconsolata Nerd Font Mono | Interface, text and code font |
| `--cm-letter-spacing` | `0.6px` | Text tracking |
| `--cm-radius` | `0px` | Corner radius |

## Source and license

Based on [mmuffins/mediamonkey-codemonkey](https://github.com/mmuffins/mediamonkey-codemonkey) via the Code Monkey AMOLED skin. MIT license in `LICENSE.md`.
