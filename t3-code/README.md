# Code Monkey AMOLED for T3 Code

A pure-black T3 Code theme: black chat and terminal, a `#080808` sidebar, a `#111111` toolbar, composer and user messages, blue accents and grey text. Errors and warnings use the Visual Studio syntax palette.

## Install

1. In T3 Code, open **Settings > Appearance** and choose **Add theme** under **Colors & themes**.
2. Drop [code-monkey-amoled.json](code-monkey-amoled.json) onto the dialog, choose it with **or import a file**, or paste its contents into **Theme JSON**.
3. Select **Code Monkey AMOLED**. It only has a dark variant. Set **Appearance mode** to dark if T3 Code is following a light system appearance.

The file uses T3 Code's own theme format (`"version": 1`) and sets all 61 color roles, so nothing falls back to T3 Code's built-in palette. It was checked with the theme parser from T3 Code 0.1.9, the installed version. Live rendering has not been verified.

Keep **Contrast** at 100% to see the palette exactly as written. Lower values reduce the contrast of colors and borders. At a **Glass opacity** below 100%, the composer is partly transparent, so it can look darker than `#111111`.

## Font

[Install Inconsolata Nerd Font Mono](../FONTS.md), then select it for both **Interface font** and **Monospace font** under **Settings > Appearance**. Theme files can't set fonts. Turn on **Separate fonts** to choose the prompt, code and terminal fonts one at a time. The skin's base size is 13px; set it with T3 Code's font size controls if you want it to match.

## Appearance and customization

| T3 Code roles | Color | Code Monkey role |
| --- | --- | --- |
| `canvas`, `chrome`, `terminalBackground` | `#000000` | base |
| `sidebar`, `surface`, `surfaceOverlay`, `codeBackground` | `#080808` | secondary |
| `toolbar`, `surfaceRaised`, `messageSurface`, `muted`, `sidebarControlSurface`, status surfaces | `#111111` | tertiary |
| `accentSurface`, `sidebarRowHover`, `toolbarControl` | `#181818` | hoverBg |
| `sidebarRowSelected`, `toolbarControlHover` | `#202020` | hoverBg2 |
| `border`, `toolbarBorder`, `sidebarBorder`, `secondary` | `#303030` | border |
| `input` | `#424242` | buttonBorder |
| `terminalScrollbar` / `terminalScrollbarHover` | `#454545` / `#656565` | contrast / textDisabled |
| Text roles | `#dcdcdc` | text |
| Muted text, placeholder and icon roles | `#999999` | textMuted |
| `focus`, `accent`, `update`, `messageAction` | `#007acc` | highlight2 |
| `messageActionHover`, `updateForeground`, `searchMatchActiveBackground` | `#1c97ea` | highlight |
| `sidebarRowActive`, `searchMatchBackground`, `terminalSelection` | `#264f78` | selected |
| `error` / `warning` and their foregrounds | `#f44747` / `#d7ba7d` | Visual Studio syntax colors |

To change the three accents, edit the matching rows of the JSON file and import it again. **Edit theme** in T3 Code also works, but its **Accent** group derives the focus, update and cursor colors from one color, so the results can fall outside the palette. The current thread in the sidebar uses `sidebarRowActive`. Rows you multi-select use `sidebarRowSelected`.

Error, warning and update banners use `#111111`, with colored text and icons instead of tinted backgrounds.

Contrast notes: body text is at least 6.19:1 on every surface, and all foregrounds pass WCAG AA except two. Muted sidebar text on the current-thread row is 2.98:1. White on the hovered send button (`#1c97ea`) is 3.15:1, the same pairing the VS Code port uses. The `#303030` borders are decorative, as in the other ports.

This format sets colors only. Code-block syntax colors come from T3 Code's built-in highlighter theme, and terminal ANSI colors aren't part of the format. Corner radius is fixed by the app and can't be made square.

## Uninstall

Select another theme under **Colors & themes**, then choose **Remove theme** on Code Monkey AMOLED.

## License

MIT, based on Code Monkey by mmuffins and Microsoft's Visual Studio colors. See [LICENSE.md](LICENSE.md).
