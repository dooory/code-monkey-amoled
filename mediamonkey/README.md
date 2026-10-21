# Code Monkey AMOLED

A pure-black AMOLED color variant of the Code Monkey skin for MediaMonkey 2024. It keeps the original layout, controls and blue highlights, with black and near-black backgrounds and Inconsolata Nerd Font Mono.

## Install

Zip the *contents* of this folder (so `info.json` is at the root of the archive, not inside a `mediamonkey/` folder) and rename the zip to `.mmip`, or install the supplied package. Add it through MediaMonkey's **Tools > Add-ons > Add** menu, then select **Code Monkey AMOLED** under **Tools > Options > Skin**.

The original Code Monkey 3.1.63 add-on is listed as compatible with MediaMonkey 2024 and versions 5.0.3–5.9. This derivative preserves its skin/add-on structure. It has not been verified in a live MediaMonkey installation.

## Font

The skin uses an installed copy of Inconsolata Nerd Font Mono, or downloads it from the pinned Nerd Fonts v3.4.0 release. [Install the font](../FONTS.md) for offline use. It keeps the Inconsolata typeface and adds developer and Powerline symbols. The original Inconsolata font and Consolas remain fallbacks. See [FONTS.md](../FONTS.md) for the Nerd Font source and license.

## Source and license

Based on [mmuffins/mediamonkey-codemonkey](https://github.com/mmuffins/mediamonkey-codemonkey). The original author's MIT license is included in `LICENSE.md`. The original blue accent and selection colors are retained; the palette changes are in `skin/skin_base_add.less`.
