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
| Font | Inconsolata Nerd Font Mono |
| Fallbacks | Inconsolata, Consolas, monospace |
| Base size | 13px |
| Weight | 400, bold 700 |
| Letter spacing | 0.6px (Discord: 0.3px, see below) |
| Width (`font-stretch`) | 100%, natural width |

Inconsolata Nerd Font Mono is the shared font. The repository does not bundle it; users install it from the Nerd Fonts release. The patched fonts are static, so ports use weight 400 and natural width instead of requesting weight 450 and width 103 from the original variable font. See [FONTS.md](FONTS.md) for installation, source, license and app limitations.

MediaMonkey and Discord prefer a local installation and otherwise download the pinned Nerd Fonts release. Discord falls back to the original Inconsolata from Google Fonts; MediaMonkey falls back to its bundled variable Inconsolata. Other ports select the installed font through their supported settings.

0.6px is the default. Discord uses 0.3px on purpose; a port can use a different value when the app calls for it.

## Shape

- Square corners everywhere: radius 0. If an app makes this a setting, default it to 0.
- 1px window border in `highlight2` (MediaMonkey).
- Active tab or list item is marked with an accent edge (`highlight2`), not just a fill.

## Syntax colors

Code-editor syntax and terminal ANSI output may use the colors from VS Code's Dark+ theme, which uses the same Visual Studio palette as the skin. Plain text uses `text` (`#dcdcdc`). These output colors are separate from the UI palette above.

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

### Windows Terminal mapping

The port in `windows-terminal/settings.json` sets both a terminal color scheme and an application theme. Its ANSI colors come from the VS Code port, while its surfaces use the UI palette.

| Surface | Windows Terminal |
| --- | --- |
| Main background | `base`, fully opaque, no background image or acrylic |
| Text / cursor | `text` |
| Selection | `selected` |
| Tab row | `secondary` |
| Active / inactive tab | `tertiary` / `base` |
| Focused / unfocused window frame | `highlight2` / `border`, Windows 11 only |
| Controls, hover, scrollbar, corners | Native dark appearance, not individually configurable by custom themes |
| Font | Locally installed Inconsolata Nerd Font Mono, Inconsolata / Consolas fallback, 9.75pt, weight 400, native cell spacing |

ANSI blue and bright blue use `highlight2` and `highlight`. The other ANSI slots use the existing syntax colors, with `#646695` from the full VS Code token list for normal purple. Programs can supply their own RGB output colors. The scheme's blue, bright blue and selection entries expose the three accents; the application theme sets its window frame separately.

### CLI ports

The Codex CLI port in `codex-cli/` uses a `.tmTheme` file for syntax highlighting, adapted from the VS Code port's TextMate rules. It cannot set the rest of Codex's interface colors. The host terminal supplies the black background, font and normal selection colors.

The Claude Code port in `claude-code/` uses the supported custom JSON theme format. Message backgrounds, borders, accents and fullscreen selection use the UI palette. Semantic status colors and agent labels use the Visual Studio syntax palette so errors, warnings and success remain distinct. Diff backgrounds use separate near-black shades and grey word highlights. Unspecified tokens inherit the dark preset, including code syntax highlighting.

Both ports use the Windows Terminal port for the terminal's appearance. Neither theme sets fonts or window corners. Installation paths and supported surfaces are documented in each port's README.

## Porting checklist

How the existing ports map roles to surfaces. "Derived" means the app computes the shade from a base color, so it may fall outside the palette. Fill in the same rows for a new app.

| Surface | MediaMonkey | VS Code | Discord | Vivaldi | Obsidian |
| --- | --- | --- | --- | --- | --- |
| Main background | `base` | `base` (editor, panel, menus) | `base` (chat, app frame) | `base` (address bar, panels, window) | `base` (editor) |
| Side bar | `secondary` | `secondary` (side bar, activity bar) | `secondary` | `base` | `secondary` (side bars, ribbon, tab bar) |
| Header / title / status bar | `tertiary` | `tertiary` | `tertiary` (floating surfaces) | `tertiary` (tab bar, as accent) | `tertiary` |
| Inputs | `border` when focused or pressed | `hoverBg` | `tertiary` | derived from `base` | `tertiary` |
| Hover | `hoverBg` | `hoverBg` | `hoverBg` | derived from `base` | `hoverBg` |
| Pressed / active | `hoverBg2` | `hoverBg2` | `hoverBg2` | derived from `base` | `hoverBg2` |
| Selection | `selected` | `selected` | `selected` | `highlight2` | `selected` |
| Active tab or item | `highlight` border | `tertiary` fill, `highlight2` top edge | `highlight2` left edge | `base` tab on `tertiary` tab bar | `tertiary` tab with `highlight2` top edge; `selected` file with `highlight2` left edge |
| Focus ring | `highlight2` border | `highlight2` | `highlight` | `highlight2` | `highlight2` |
| Borders | `border` | `border` | `border`, `buttonBorder` for strong | derived from `base` | `border`, `buttonBorder` on hover |
| Scrollbar | `contrast` thumb on `tertiary` track | `contrast` thumb (80% alpha) | `contrast` thumb on `tertiary` track | Vivaldi default | `contrast` thumb on `tertiary` track |
| Button | `border` fill, `buttonBorder` edge, `highlight2` edge on hover, `highlight2` fill when pressed | `highlight2` fill, `highlight` on hover | brand: `highlight2`, `highlight` on hover; secondary: `border`, `buttonBorder` on hover | `highlight2` | `border` fill, `buttonBorder` on hover; accent: `highlight2`, `highlight` on hover |
| Links | `highlight` | `highlight` | `highlight` | n/a (web pages aren't themed) | `highlight` |
| Font | local Nerd Font or pinned download | user setting (themes can't set fonts) | local Nerd Font or pinned download | UI CSS mod (local install) | theme font variables (local install) |

Before calling a port done:

1. Every UI color you set is in the palette (search the theme file for hex values and compare).
2. Hover, active and selected states all differ from each other and from the resting state.
3. Corners are square.
4. Inconsolata Nerd Font Mono loads where supported, with Inconsolata and Consolas as fallbacks. Document surfaces whose fonts the app does not let a theme change.
5. The three accent colors can be changed in one place.
