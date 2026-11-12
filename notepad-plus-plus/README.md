# Code Monkey AMOLED for Notepad++

A pure-black Notepad++ theme with Visual Studio syntax colors, matching the VS Code port. It colors the editor, margins, tabs and every built-in language. It also sets Inconsolata Nerd Font Mono as the editor font.

## Install

1. [Install Inconsolata Nerd Font Mono](../FONTS.md).
2. Copy [Code Monkey AMOLED.xml](Code%20Monkey%20AMOLED.xml) into `%AppData%\Notepad++\themes\`. Create the folder if it doesn't exist:

   ```powershell
   $dest = "$env:APPDATA\Notepad++\themes"
   New-Item -ItemType Directory -Force $dest
   Copy-Item "Code Monkey AMOLED.xml" $dest
   ```

   Portable copies of Notepad++ (with `doLocalConf.xml` next to `notepad++.exe`) read themes only from the `themes` folder next to `notepad++.exe`. Use that folder instead. **Settings > Import > Import style theme(s)...** also works, but it copies into the installation's `themes` folder and may need administrator rights.
3. Close every Notepad++ window and start it again. Notepad++ only finds new themes when it starts.
4. Open **Settings > Style Configurator...**, choose **Code Monkey AMOLED** under **Select theme**, then click **Save & Close**.

Notepad++ remembers a separate theme for light and dark mode. Turn on **Settings > Preferences... > Dark Mode > Dark mode** before step 4 to use the theme with dark menus and dialogs. If you choose it in light mode, the editor is black but the menus and dialogs stay light.

## Recommended settings

These are Notepad++ preferences, not theme settings, so the theme file can't set them.

- **Preferences > Editing 1 > Apply custom color to selected text foreground**: turn this on so selected text is white on `#264f78`. Otherwise selected text keeps its syntax colors, and some (comments, red, blue) are hard to read on the selection.
- **Preferences > Tab Bar > Draw a colored bar on active tab**: marks the active tab with a `#007acc` bar.
- **Preferences > Tab Bar > Change inactive tab color**: gives inactive tabs the theme's black background.
- **Preferences > Dark Mode > Customized**: matches the menus, toolbar, dialogs and controls to the palette. These colors live in Notepad++'s `config.xml`, not in the theme:

  | Setting | Color |
  | --- | --- |
  | Content background | `#000000` |
  | Hot track item | `#181818` |
  | Control background | `#111111` |
  | Dialog background | `#080808` |
  | Error | leave the default |
  | Text | `#dcdcdc` |
  | Darker text | `#999999` |
  | Disabled text | `#656565` |
  | Edge | `#303030` |
  | Link | `#1c97ea` |
  | Edge highlight | `#007acc` |
  | Edge disabled | `#202020` |

## Appearance

The file covers every lexer and global style in Notepad++ 8.9.8's `stylers.model.xml`: 91 languages plus the Search results panel. Each style keeps its Notepad++ name, ID and keyword list. Only the colors and fonts change.

| Surface | Color |
| --- | --- |
| Editor, margins, inactive tabs | `#000000` |
| Text, caret | `#dcdcdc` |
| Current line | `#111111` |
| Selection | `#264f78`, white text when the option above is on |
| Line numbers, fold markers | `#999999` |
| Indent guides, edge line | `#303030` |
| Whitespace and EOL symbols | `#454545` |
| Active tab bar | `#007acc` (`#303030` when unfocused) |
| Brace match | white on `#303030` |
| Smart highlight / Find mark | `#1c97ea` / `#dcdcaa` |

Syntax colors follow [SPEC.md](../SPEC.md#syntax-colors): keywords `#569cd6`, preprocessor and control `#c586c0`, strings `#ce9178`, numbers `#b5cea8`, functions `#dcdcaa`, types `#4ec9b0`, variables, properties and attributes `#9cdcfe`, constants `#4fc1ff`, comments `#6a9955`, regex `#d16969`, escapes and CSS selectors `#d7ba7d`, and errors `#f44747`. Markup headings are bold `#569cd6`, links are underlined `#1c97ea`, and diff additions and deletions use `#b5cea8` and `#ce9178`. ANSI escape sequences and the error list use the same 16 colors as the [Windows Terminal port](../windows-terminal/README.md).

Notepad++ uses a single keyword color for each lexer's main keyword list. Most languages put control flow and declarations in that same list, so `if` and `return` stay blue instead of VS Code's purple. **TYPE WORD** lists, such as C# `int` and TypeScript `string`, use the type color.

The five tab colors you can assign from a tab's context menu keep Notepad++'s dark-mode defaults, because the palette has no matching shades.

## Font

The theme sets **Inconsolata Nerd Font Mono** at 10pt, regular weight, in **Default Style** and **Global override**. Notepad++ font sizes are whole points, so 10pt is the closest to the spec's 13px. Notepad++ accepts one font name with no fallback list, and it can't set letter spacing. If the font isn't installed, Windows substitutes another font. To use a different font, change **Global Styles > Default Style** in the Style Configurator.

Menus, dialogs and tab labels use the Windows UI font. The dialog font is under **Preferences > General**.

## Not covered

- User Defined Languages keep their own colors, including the bundled Markdown language. Notepad++ ships `markdown._preinstalled_DM` for dark mode. Choose it under **Language > User Defined Language**.
- Plugin panels draw their own colors.
- Notepad++ draws highlight and mark colors semi-transparently over the text, so they show darker than the hex values above.

## Changing colors

Edit a style in **Settings > Style Configurator...** and save. Notepad++ writes the change into the theme file in your `themes` folder.

To change the palette for every language at once, edit the role colors at the top of [generate.py](generate.py) and rebuild the file from your installed Notepad++:

```powershell
python generate.py "C:\Program Files\Notepad++\stylers.model.xml" "Code Monkey AMOLED.xml" 8.9.8.1
```

The script copies every language and style from the model, so rebuilding after a Notepad++ update also picks up new languages. Style names it has no rule for fall back to the text color and are printed as `UNMATCHED`.

## Uninstall

Choose another theme in the Style Configurator, then delete `Code Monkey AMOLED.xml` from the `themes` folder.

## Source and license

Based on [Code Monkey](https://github.com/mmuffins/mediamonkey-codemonkey) by mmuffins, with Visual Studio colors from Microsoft's VS Code themes. MIT license in [LICENSE.md](LICENSE.md). The separately installed Nerd Font uses the [SIL Open Font License](https://github.com/ryanoasis/nerd-fonts/blob/v3.4.0/patched-fonts/Inconsolata/OFL.txt). Style names, IDs and keyword classes come from Notepad++'s `stylers.model.xml`.
