# Shared font

The theme uses **Inconsolata Nerd Font Mono**, the Nerd Fonts edition of the original Inconsolata typeface. It adds developer, file-type and Powerline symbols. The Mono edition keeps those symbols within one character cell for terminal output.

## Install

1. Download [Inconsolata.zip](https://github.com/ryanoasis/nerd-fonts/releases/download/v3.4.0/Inconsolata.zip) from the Nerd Fonts v3.4.0 release and extract it.
2. Right-click `InconsolataNerdFontMono-Regular.ttf` and choose **Install**. Repeat for `InconsolataNerdFontMono-Bold.ttf`. The zip's other files are the proportional and non-Mono editions, which these ports don't use.
3. Restart apps that were open during installation.

Select the family **Inconsolata Nerd Font Mono** in app font settings. Inconsolata and Consolas remain fallbacks where font lists are supported. Those fallbacks do not include the full Nerd Font symbol set.

## App support

| App | How the font applies |
| --- | --- |
| MediaMonkey | The skin uses the installed font first, then downloads it from the pinned Nerd Fonts release. |
| Windows Terminal | The settings snippet selects the installed font for terminal panes. The application UI keeps its native font. |
| VS Code | The README supplies editor and integrated-terminal font settings. Color themes cannot set fonts or change the workbench UI font. |
| Discord | The theme uses the installed font first, then downloads it from the pinned Nerd Fonts release. It applies to UI and code text. |
| Obsidian | The theme selects the installed font for the interface, notes and code. Fonts chosen in Obsidian's appearance settings take precedence. |
| Vivaldi | The CSS UI modification selects the installed font. Browser themes alone cannot set fonts. Web pages keep their own fonts. |
| Roblox Studio | Select the installed font in **File > Studio Settings > Script Editor > Font**. The mod changes colors, so its other panels keep their native fonts. |

The patched font has static regular 400 and bold 700 weights. It does not have the original variable font's width axis. Ports use regular 400 and the natural width, while retaining their existing text sizes and letter spacing.

A Nerd Font supplies glyphs. Prompts and programs still need to output those symbols; installing it does not replace an app's existing icons.

## Source and license

The font isn't bundled with this repository. The ports pin [Nerd Fonts v3.4.0, Inconsolata](https://github.com/ryanoasis/nerd-fonts/tree/v3.4.0/patched-fonts/Inconsolata), which uses the [SIL Open Font License](https://github.com/ryanoasis/nerd-fonts/blob/v3.4.0/patched-fonts/Inconsolata/OFL.txt).
