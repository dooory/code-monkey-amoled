# Code Monkey AMOLED for Vivaldi

A pure-black Vivaldi theme based on the Code Monkey AMOLED MediaMonkey skin: black address bar and panels, a `#111111` tab bar like the skin's headers, `#007acc` highlights and square corners.

## Install

Open the theme on [themes.vivaldi.net](https://themes.vivaldi.net/themes/PKbv8KkElr3) in Vivaldi and install it from there.

### From this folder

1. Zip `settings.json` on its own (it must be at the root of the zip):

   ```powershell
   Compress-Archive -Path settings.json -DestinationPath code-monkey-amoled.zip -Force
   ```
2. In Vivaldi, open **Settings > Themes**, choose **Import Theme...**, and pick `code-monkey-amoled.zip`.
3. Select **Code Monkey AMOLED** in the theme list.

## Font (optional)

Themes can't change Vivaldi's UI font. To use the skin's font:

1. [Install Inconsolata Nerd Font Mono](../FONTS.md).
2. Open `vivaldi://experiments` and turn on **Allow for using CSS modifications**.
3. In **Settings > Appearance > Custom UI Modifications**, choose this folder (or any folder containing `code-monkey-amoled.css`), then restart Vivaldi.

## Changing colors

Select the theme, then change it in the Theme Editor under **Settings > Themes**:

| Vivaldi setting | Default | Code Monkey role |
| --- | --- | --- |
| Background | `#000000` | base |
| Foreground | `#dcdcdc` | text |
| Highlight | `#007acc` | highlight2 |
| Accent | `#111111` | tertiary (tab bar) |
| Window background | `#000000` | base |

Vivaldi works out hover and border shades from these, so they won't match the palette exactly.

## Source and license

Based on [mmuffins/mediamonkey-codemonkey](https://github.com/mmuffins/mediamonkey-codemonkey) via the Code Monkey AMOLED skin. MIT license in `LICENSE.md`.
