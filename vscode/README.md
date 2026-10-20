# Code Monkey AMOLED for VS Code

A pure-black dark theme based on the Code Monkey AMOLED skin for MediaMonkey 2024. It uses the skin's palette: black editor, near-black side bar, `#111111` headers, Visual Studio blue accents (`#007acc`, `#1c97ea`) and `#264f78` selection.

Syntax colors come from VS Code's built-in Dark+ theme, which is based on the same Visual Studio palette as the skin.

## Install

From this folder:

```
npx @vscode/vsce package --allow-missing-repository
code --install-extension code-monkey-amoled-1.0.0.vsix
```

Then pick **Code Monkey AMOLED** with **Preferences: Color Theme**.

To try it without installing, open this folder in VS Code, press F5, and pick the theme in the window that opens.

## Matching the skin's font

Themes can't set fonts. To match the skin, install [Inconsolata](https://fonts.google.com/specimen/Inconsolata) and add this to your settings:

```json
"editor.fontFamily": "Inconsolata, Consolas, monospace",
"editor.fontSize": 13,
"editor.fontWeight": "450",
"editor.letterSpacing": 0.6
```

## Changing colors

The skin's "Colorful" active tab option isn't a separate theme. To get it, add:

```json
"workbench.colorCustomizations": {
  "[Code Monkey AMOLED]": {
    "tab.activeBackground": "#007acc"
  }
}
```

The same setting can change the selection and highlight colors.

## Credits

- [Code Monkey](https://github.com/mmuffins/mediamonkey-codemonkey) skin by mmuffins (MIT)
- Dark+ token colors from [VS Code](https://github.com/microsoft/vscode) by Microsoft (MIT)

See `LICENSE.md`.
