# Code Monkey AMOLED spec

Reference for porting the theme to a new app. The MediaMonkey skin is the source of truth: the palette comes from `mediamonkey/skin/skin_base_add.less`, and the role names below match its LESS variables. When a value changes, change it there first, then here, then in each port.

## Palette

Every UI color in a port should be one of these. If an app needs a shade that isn't here, use the nearest palette color, picking the next step up when the nearest one would make a hover or active state look the same as its resting state.

### Surfaces

| Role | Hex | Use |
| --- | --- | --- |
| `base` | `#000000` | Main background: editor, chat, content area |
| `secondary` | `#080808` | Side bars, controls, modals |
| `tertiary` | `#111111` | Headers, title and status bars, active tab, inputs, scrollbar track |
| `hoverBg` | `#181818` | Hovered rows and items |
| `hoverBg2` | `#202020` | Pressed or active items |

### Lines and greys

| Role | Hex | Use |
| --- | --- | --- |
| `border` | `#303030` | Borders, dividers, button background |
| `buttonBorder` | `#424242` | Button border, strong borders |
| `contrast` | `#454545` | Scrollbar thumb, inactive selection |

### Text

| Role | Hex | Use |
| --- | --- | --- |
| `text` | `#dcdcdc` | Body text |
| `textStrong` | `#ffffff` | Headings, text on accent backgrounds, selected text |
| `textMuted` | `#999999` | Secondary text, icons, title bar text, placeholders, line numbers |
| `textDisabled` | `#656565` | Disabled text |

### Accents

These three are the only colors the MediaMonkey skin lets users change (`mediamonkey/config.js`), so ports should expose them as settings where the app allows.

| Role | Hex | Use |
| --- | --- | --- |
| `highlight` | `#1c97ea` | Links, hover accents, selected-tab border |
| `highlight2` | `#007acc` | Buttons, focus and hover borders, window border, active tab or channel edge, mentions |
| `selected` | `#264f78` | Selected rows and text selection |

The skin's source keeps a commented-out Visual Studio 2022 purple alternative (`#7261e6` / `#3f3682`) for `highlight` / `highlight2`. It isn't part of the theme.

## Typography

| Property | Value |
| --- | --- |
| Font | Inconsolata |
| Fallbacks | Consolas, monospace |
| Base size | 13px |
| Weight | 450 |
| Letter spacing | 0.6px (Discord: 0.3px, see below) |
| Width (`font-stretch`) | 103% |

Inconsolata is a variable font (OFL, `mediamonkey/skin/fonts/OFL.txt`). Bundle the TTF when the app can load local fonts; otherwise load it from Google Fonts (`family=Inconsolata:wdth,wght@50..200,200..900`).

0.6px is the default. Discord uses 0.3px on purpose; a port can use a different value when the app calls for it.

## Shape

- Square corners everywhere: radius 0. If an app makes this a setting, default it to 0.
- 1px window border in `highlight2` (MediaMonkey).
- Active tab or list item is marked with an accent edge (`highlight2`), not just a fill.

## Syntax colors

Code-editor ports only (VS Code today). Taken from VS Code's Dark+ theme, which uses the same Visual Studio palette as the skin. Plain code text uses `text` (`#dcdcdc`).

| Token | Hex |
| --- | --- |
| Keywords, storage, tags | `#569cd6` |
| Control flow keywords | `#c586c0` |
| Strings | `#ce9178` |
| Numbers | `#b5cea8` |
| Functions | `#dcdcaa` |
| Types, classes | `#4ec9b0` |
| Variables, parameters | `#9cdcfe` |
| Constants | `#4fc1ff` |
| Comments | `#6a9955` |
| Regex | `#d16969` |
| CSS selectors / escapes | `#d7ba7d` |
| Invalid | `#f44747` |

The full scope list is in `vscode/themes/code-monkey-amoled-color-theme.json` under `tokenColors`.

## Porting checklist

How the existing ports map roles to surfaces. Fill in the same rows for a new app.

| Surface | MediaMonkey | VS Code | Discord |
| --- | --- | --- | --- |
| Main background | `base` | `base` (editor, panel, menus) | `base` (chat, app frame) |
| Side bar | `secondary` | `secondary` (side bar, activity bar) | `secondary` |
| Header / title / status bar | `tertiary` | `tertiary` | `tertiary` (floating surfaces) |
| Inputs | `border` when focused or pressed | `hoverBg` | `tertiary` |
| Hover | `hoverBg` | `hoverBg` | `hoverBg` |
| Pressed / active | `hoverBg2` | `hoverBg2` | `hoverBg2` |
| Selection | `selected` | `selected` | `selected` |
| Active tab or item | `highlight` border | `tertiary` fill, `highlight2` top edge | `highlight2` left edge |
| Focus ring | `highlight2` border | `highlight2` | `highlight` |
| Borders | `border` | `border` | `border`, `buttonBorder` for strong |
| Scrollbar | `contrast` thumb on `tertiary` track | `contrast` thumb (80% alpha) | `contrast` thumb on `tertiary` track |
| Button | `border` fill, `buttonBorder` edge, `highlight2` edge on hover, `highlight2` fill when pressed | `highlight2` fill, `highlight` on hover | brand: `highlight2`, `highlight` on hover; secondary: `border`, `buttonBorder` on hover |
| Links | `highlight` | `highlight` | `highlight` |
| Font | bundled TTF | user setting (themes can't set fonts) | Google Fonts |

Before calling a port done:

1. Every UI color is in the palette (search the theme file for hex values and compare).
2. Hover, active and selected states all differ from each other and from the resting state.
3. Corners are square.
4. Inconsolata loads, with Consolas as the fallback.
5. The three accent colors can be changed in one place.
