r"""Generate "Code Monkey AMOLED.xml" from Notepad++'s stylers.model.xml.

Usage (from this folder):
    python generate.py "C:\Program Files\Notepad++\stylers.model.xml" "Code Monkey AMOLED.xml" 8.9.8.1

The third argument is the Notepad++ version recorded in the file header.
Every LexerType, WordsStyle and WidgetStyle in the model is kept with its name,
styleID, keywordClass and ext. Only colors and font attributes are replaced.
Unmapped style names fall back to the text color and are printed as UNMATCHED.
"""
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from xml.sax.saxutils import quoteattr

# UI palette (SPEC.md)
BASE, SECONDARY, TERTIARY, HOVER = "000000", "080808", "111111", "181818"
BORDER, CONTRAST = "303030", "454545"
TEXT, STRONG, MUTED, DISABLED = "DCDCDC", "FFFFFF", "999999", "656565"
HIGHLIGHT, HIGHLIGHT2, SELECTED = "1C97EA", "007ACC", "264F78"

# Syntax palette (SPEC.md, VS Code Dark+)
R = dict(
    text=TEXT, keyword="569CD6", control="C586C0", string="CE9178", number="B5CEA8",
    function="DCDCAA", type="4EC9B0", variable="9CDCFE", constant="4FC1FF",
    comment="6A9955", regex="D16969", escape="D7BA7D", invalid="F44747",
    punct="808080", list="6796E6", muted=MUTED, link=HIGHLIGHT,
)

BOLD, ITALIC, UNDERLINE = 1, 2, 4

# Ordered (regex, role, fontStyle) rules over the upper-cased style name. First match wins.
RULES = [
    (r"^(ADDED|ADDED KEY|DIFF ADDITION)$", "number", 0),
    (r"^(DELETED|REMOVED KEY|DIFF DELETION)$", "string", 0),
    (r"^DIFF CHANGED$", "keyword", 0),
    (r"^DIFF MESSAGE$", "link", 0),
    (r"ERROR|ILLEGAL|INVALID|^BAD |UNKNOWN|GARBAGE|WRONG|NOT CLOSED|^STRING EOL|TOO MANY", "invalid", 0),
    (r"^COMMENT DOC KEYWORD$|^DOCUMENTATION (MACRO|HELPER)", "keyword", 0),
    (r"COMMENT|^POD|^BLOCKQUOTE$|^AFTER LABEL$", "comment", 0),
    (r"^(URL|URI|LINK|COMPACT IRI|EMAIL)\b", "link", UNDERLINE),
    (r"^H[1-6]$|^HEADER$|^HEADING", "keyword", BOLD),
    (r"^STRONG", "text", BOLD),
    (r"^EM1", "control", ITALIC),
    (r"^EM2", "text", UNDERLINE),
    (r"^[UO]LIST$", "list", 0),
    (r"^HRULE$", "muted", 0),
    (r"^(CODE|CODE2|CODEBLOCK)$", "string", 0),
    (r"^VAR IN REGEX", "variable", 0),
    (r"REGEX", "regex", 0),
    (r"ESCAPE|SPECIAL CHAR", "escape", 0),
    (r"^VAR IN |^STRING VAR|VARIABLE|SCALAR|^ARRAY$|^HASH$|^PARAM|^INSTANCE VAR|^CLASS VAR|^GLOBAL$", "variable", 0),
    (r"^DEFAULT (ON|TEXT|STYLE|COMMENT)|^DEFAULT$", "text", 0),
    (r"STRING|CHARACTER|^CHAR$|QUOTE|VERBATIM|HEREDOC|^HERE |BACKTICK|^TRIPLE|^F TRIPLE|^CDATA$|^TEMPLATE LIT|^IN QUOTE$|^WORD IN QUOTE$|^VALUE$", "string", 0),
    (r"^BOOL$|^NIL$|^SELF$|^SUPER$", "keyword", 0),
    (r"NUMBER|NUMERIC|^HEX|^BIN|DIGIT|^MONEY|^DATE|^TIME|^PAIR|^TUPLE|^BINARY", "number", 0),
    (r"^DECORATOR|^ANNOTATION", "function", 0),
    (r"FUNC|METHOD|CMDLET|^ALIAS$|BUILTIN|BUILT-IN FUNC|CALLABLE|^COMMAND$|^SHORT COMMAND$|^TARGET$|^LABEL|REFERENCE \(TO A LABEL\)|^MACRO$|^DEF NAME$|PREDECLARED|WINDOW INSTRUCTION|^PLUGIN|^STD OPERATOR$", "function", 0),
    (r"TYPE|CLASS|STRUCT|^STD PACKAGE|MODULE NAME|NAMESPACE|STATIC BUILT-IN OBJECT|^COMOBJ$|^CORE API$|^MODULE$|^INSTANCE$", "type", 0),
    (r"CONSTANT|^ATOM|^ENUM|PREDEFINED", "constant", 0),
    (r"PREPROC|^IFDEF|^IF DEFINE|^#IFDEF|^MACRO|^PREWORD|^DIRECTIVE|^PRAGMA|^IMPORT$", "control", 0),
    (r"ATTRIBUTE|PROPERTY|^KEY$|^VALUE NAME$|^COL NAME|^NODE NAME|^OPTION$", "variable", 0),
    (r"^(XML START|XML END)$", "punct", 0),
    (r"OPERATOR|DELIMITER|BRACE|^PAREN|^ASSIGN|DIVISION|^DIVSION|^SYMBOLS?$|^ASTERISK$|^QUESTION MARK$", "text", 0),
    (r"KEYWORD|INSTRUCTION|^WORD|RESERVED|COMMAND|STATEMENT|OPCODE|REGISTER|MODIFI|QUALIFIER|DECLARATION|SECTION|^TAG|^SGML COMMAND$|^ASM$|^RETURN$|^ENTITY$|^TABLE|^ASP SYMBOL$|^USER|^SUB|^SENT$|^GROUP$", "keyword", 0),
    (r"IDENTIFIER|^TEXT$|^WHITE ?SPACE$|^NAME$|^ANY OTHER|^SGML|^IDEOL$|^DATA$|^DOCUMENT$", "text", 0),
]

# Exact names the regex rules don't cover (checked after per-lexer overrides, before RULES).
NAMED = {
    "CONTROL": "control", "FOREACHDEF": "control", "WHILEDEF": "control", "POSTPROC": "control",
    "PREFACE": "control", "KWS END": "keyword", "DEFWORDS": "keyword", "PAGE EX": "keyword",
    "TASK START/END": "keyword", "EXPAND": "keyword", "ADVERB": "keyword", "INSTR": "keyword",
    "LOCALE": "keyword", "DESCRIPTORS": "keyword",
    "VAR": "variable", "POSITIONAL": "variable", "ASSOCIATIVE": "variable", "MU": "variable",
    "SYMBOL TABLE": "variable", "MAJOR": "variable", "ANONYMOUS": "variable",
    "CLIP PROPERTIES": "variable",
    "GUID IN KEY PATH": "constant", "LITERAL": "constant", "IMMEVAL": "constant", "MINOR": "constant",
    "NODEPATH": "constant", "FILE { %/C/WINNT/SOME.DLL }": "constant", "ISSUE { #123-CD-456 }": "constant",
    "DSC VALUE": "string", "FORMAT BODY": "string",
    "MATH BLOCK": "escape", "MATH INLINE": "escape", "SPECIAL": "escape",
    "CAPITAL": "type", "GRAMMAR": "type", "RECORD": "type", "SYSTEM TABLE": "type",
    "DOMAIN DEFINITIONS": "type", "OBJECT DEFINITIONS": "type",
    "SPECIAL SELECTOR": "function", "FILTER": "function", "BASE WORD": "function", "EVENT": "function",
    "SYSTEM STORED PROC": "function", "SGML 1ST PARAM": "variable",
    "TRANSLATION": "regex",
    "STRIKEOUT": "muted", "CONTINUATION": "muted", "LINENUM": "muted", "PRECHAR (NOT USED)": "text",
    "INFIX": "text", "INFIXEOL": "text",
}

# Per-lexer overrides: {lexer: {STYLE NAME: (role or hex, fontStyle)}}
OVR = {
    "css": {
        "TAG": ("escape", 0), "CLASS": ("escape", 0), "ID": ("escape", 0),
        "PSEUDOCLASS": ("escape", 0), "UNKNOWN PSEUDOCLASS": ("escape", 0),
        "PSEUDOELEMENT": ("escape", 0), "LEGACY PSEUDOELEMENT": ("escape", 0),
        "ATTRIBUTE": ("escape", 0), "IDENTIFIER": ("variable", 0),
        "UNKNOWN IDENTIFIER": ("variable", 0), "IMPORTANT": ("keyword", 0),
        "DIRECTIVE": ("control", 0), "MEDIA": ("keyword", 0),
    },
    "html": {"TAG UNKNOWN": ("keyword", 0), "ATTRIBUTE UNKNOWN": ("variable", 0)},
    "xml": {"TAG UNKNOWN": ("keyword", 0), "ATTRIBUTE UNKNOWN": ("variable", 0)},
    "yaml": {"IDENTIFIER": ("variable", 0), "REFERENCE": ("type", 0), "DOCUMENT": ("control", 0), "TEXT": ("string", 0)},
    "ini": {"SECTION": ("keyword", 0), "DEFVAL": ("control", 0)},
    "props": {"SECTION": ("keyword", 0), "DEFVAL": ("control", 0)},
    "toml": {"TABLE": ("keyword", 0), "KEY": ("variable", 0)},
    "json": {"LD KEYWORD": ("control", 0)},
    "diff": {"COMMAND": ("keyword", BOLD), "HEADER": ("keyword", 0), "POSITION": ("control", 0)},
    "batch": {"HIDE SYMBOL": ("muted", 0), "COMMAND": ("function", 0)},
    "bash": {"HERE DELIM": ("keyword", 0), "BACKTICKS": ("string", 0)},
    "rust": {"KEYWORDS 1": ("keyword", 0), "KEYWORDS 2": ("type", 0), "KEYWORDS 3": ("type", 0),
             "LIFETIME": ("keyword", 0), "MACRO": ("function", 0)},
    "sql": {"USER1": ("function", 0), "KEYWORD2": ("type", 0), "Q OPERATOR": ("string", 0)},
    "mssql": {},
    "python": {"BUILTINS": ("function", 0), "CLASS NAME": ("type", 0)},
    "php": {"QUESTION MARK": ("keyword", 0)},
    "searchResult": {},
    "ruby": {"SYMBOL": ("constant", 0)},
    "lisp": {"SYMBOL": ("constant", 0)},
    "scheme": {"SYMBOL": ("constant", 0)},
    "smalltalk": {"SYMBOL": ("constant", 0)},
    "vhdl": {"STD OPERATOR": ("keyword", 0)},
    "raku": {"REGEX VAR": ("variable", 0)},
    "visualprolog": {"COMMENT KEY": ("keyword", 0)},
}

# User keyword lists: empty unless the user fills them in Style Configurator,
# so give each slot a different syntax color.
USER_CYCLE = ["type", "function", "variable", "constant", "control", "escape", "number", "keyword"]

# ANSI mapping, same as windows-terminal/settings.json
ANSI = {"BLACK": "000000", "RED": "D16969", "GREEN": "6A9955", "YELLOW": "D7BA7D", "BROWN": "D7BA7D",
        "BLUE": "007ACC", "MAGENTA": "646695", "CYAN": "4EC9B0", "WHITE": "DCDCDC", "GRAY": "DCDCDC"}
ANSI_BRIGHT = {"BLACK": "656565", "RED": "F44747", "GREEN": "B5CEA8", "YELLOW": "DCDCAA",
               "BLUE": "1C97EA", "MAGENTA": "C586C0", "CYAN": "9CDCFE", "WHITE": "FFFFFF"}

unmatched = defaultdict(list)


def color(role):
    return R.get(role, role)


def classify(lexer, name):
    """Return (fg, bg, fontStyle) for a WordsStyle."""
    up = name.upper()
    bg = BASE
    if lexer == "escseq":
        m = re.match(r"^(BOLD )?(\w+) on (\w+)$", name)
        if m:
            bold, fgn, bgn = m.groups()
            pal = ANSI_BRIGHT if bold else ANSI
            fg = TEXT if fgn == "DEFAULT" else pal[fgn]
            bgc = BASE if bgn == "DEFAULT" else ANSI[bgn]
            return fg, bgc, BOLD if bold else 0
        return (MUTED if "Identifier" in name else R["invalid"]), BASE, 0
    if lexer == "errorlist":
        m = re.match(r"^ANSI COLOR (BRIGHT |DARK )?(\w+)$", up)
        if m:
            mod, c = m.groups()
            if mod == "DARK " and c == "GRAY":
                return ANSI_BRIGHT["BLACK"], BASE, 0
            return (ANSI_BRIGHT if mod else ANSI)[c], BASE, 0
        if up == "ESCAPE SEQUENCE":
            return MUTED, BASE, 0
    if lexer == "searchResult":
        return {
            "SEARCH HEADER": (HIGHLIGHT, TERTIARY, BOLD),
            "FILE HEADER": (R["type"], SECONDARY, BOLD),
            "LINE NUMBER": (MUTED, BASE, 0),
            "HIT WORD": (STRONG, SELECTED, 0),
            "CURRENT LINE BACKGROUND COLOUR": (None, TERTIARY, None),
        }[up]
    if lexer in ("ihex", "srec", "tehex"):
        for pat, role in [(r"WRONG|UNKNOWN|GARBAGE", "invalid"), (r"^RECSTART", "keyword"),
                          (r"^RECTYPE|^RECCOUNT", "control"), (r"^BYTECOUNT", "number"),
                          (r"ADDRESS", "type"), (r"^DATA_ODD", "text"), (r"^DATA_EVEN", "variable"),
                          (r"^DATA_EMPTY", "muted"), (r"^CHECKSUM", "escape"), (r"^DEFAULT", "text")]:
            if re.search(pat, up):
                return color(role), bg, 0
    o = OVR.get(lexer, {}).get(up) or OVR.get(lexer, {}).get(name)
    if o:
        return color(o[0]), bg, o[1]
    m = re.match(r"^USER (KEYWORDS|TAGS|ATTRIBUTES|SCALAR) ?(\d)$", up) or re.match(r"^USER(?: DEFINED)?(\d)?$", up)
    if m:
        kind = m.group(1) if m.lastindex and m.lastindex >= 2 else None
        if kind == "TAGS":
            return R["keyword"], bg, 0
        if kind == "ATTRIBUTES":
            return R["variable"], bg, 0
        if kind == "SCALAR":
            return R["variable"], bg, 0
        n = int(m.group(m.lastindex) or 1) if m.lastindex else 1
        return color(USER_CYCLE[(n - 1) % len(USER_CYCLE)]), bg, 0
    m = re.match(r"^KEYWORDS? ?(\d)$", up) or re.match(r"^KEYWORDS?(\d)$", up)
    if m:
        n = int(m.group(1))
        cyc = ["keyword", "type", "function", "variable", "constant", "control", "escape", "number"]
        return color(cyc[(n - 1) % len(cyc)]), bg, 0
    if up in NAMED:
        return color(NAMED[up]), bg, 0
    for pat, role, fs in RULES:
        if re.search(pat, up):
            return color(role), bg, fs
    unmatched[name].append(lexer)
    return TEXT, bg, 0


FONT = "Inconsolata Nerd Font Mono"

GLOBAL = {
    "Default Style": dict(fgColor=TEXT, bgColor=BASE, fontName=FONT, fontStyle="0", fontSize="10"),
    "Indent guideline style": dict(fgColor=BORDER, bgColor=BASE),
    "Brace highlight style": dict(fgColor=STRONG, bgColor=BORDER, fontStyle="1"),
    "Bad brace colour": dict(fgColor=R["invalid"], bgColor=BASE, fontStyle="1"),
    "Current line background colour": dict(bgColor=TERTIARY),
    "Selected text colour": dict(bgColor=SELECTED, fgColor=STRONG),
    "Multi-selected text color": dict(bgColor=SELECTED),
    "Caret colour": dict(fgColor=TEXT),
    "Multi-edit carets color": dict(fgColor=HIGHLIGHT),
    "Edge colour": dict(fgColor=BORDER),
    "Line number margin": dict(fgColor=MUTED, bgColor=BASE),
    "Bookmark margin": dict(bgColor=BASE),
    "Change History margin": dict(bgColor=BASE),
    "Change History modified": dict(fgColor=HIGHLIGHT2, bgColor=HIGHLIGHT2),
    "Change History revert modified": dict(fgColor=R["escape"], bgColor=R["escape"]),
    "Change History revert origin": dict(fgColor=R["type"], bgColor=R["type"]),
    "Change History saved": dict(fgColor=R["comment"], bgColor=R["comment"]),
    "Fold": dict(fgColor=MUTED, bgColor=BASE),
    "Fold active": dict(fgColor=HIGHLIGHT),
    "Fold margin": dict(fgColor=BASE, bgColor=BASE),
    "White space symbol": dict(fgColor=CONTRAST),
    "Smart Highlighting": dict(bgColor=HIGHLIGHT),
    "Find Mark Style": dict(bgColor=R["function"]),
    "Find status: Not found": dict(fgColor=R["invalid"]),
    "Find status: Message": dict(fgColor=HIGHLIGHT),
    "Find status: Search end reached": dict(fgColor=R["number"]),
    "Mark Style 1": dict(bgColor=R["type"]),
    "Mark Style 2": dict(bgColor=R["constant"]),
    "Mark Style 3": dict(bgColor=R["control"]),
    "Mark Style 4": dict(bgColor=R["comment"]),
    "Mark Style 5": dict(bgColor=R["string"]),
    "Incremental highlight all": dict(bgColor=R["escape"]),
    "Tags match highlighting": dict(bgColor=HIGHLIGHT2),
    "Tags attribute": dict(bgColor=R["type"]),
    "Active tab focused indicator": dict(fgColor=HIGHLIGHT2),
    "Active tab unfocused indicator": dict(fgColor=BORDER),
    "Active tab text": dict(fgColor=TEXT),
    "Inactive tabs": dict(fgColor=MUTED, bgColor=BASE),
    # Individual tab colors are user-applied markers; keep Notepad++'s dark-mode
    # defaults in both slots so they stay legible under light text.
    "Tab color 1": dict(bgColor="807848"),
    "Tab color 2": dict(bgColor="568048"),
    "Tab color 3": dict(bgColor="507094"),
    "Tab color 4": dict(bgColor="804849"),
    "Tab color 5": dict(bgColor="754880"),
    "Tab color dark mode 1": dict(bgColor="807848"),
    "Tab color dark mode 2": dict(bgColor="568048"),
    "Tab color dark mode 3": dict(bgColor="507094"),
    "Tab color dark mode 4": dict(bgColor="804849"),
    "Tab color dark mode 5": dict(bgColor="754880"),
    "URL hovered": dict(fgColor=HIGHLIGHT),
    "Document map": dict(fgColor=STRONG, bgColor=CONTRAST),
    "EOL custom color": dict(fgColor=CONTRAST),
    "Non-printing characters custom color": dict(fgColor=CONTRAST),
    "Global override": dict(fgColor=TEXT, bgColor=BASE, fontName=FONT, fontStyle="0", fontSize=""),
}

HEADER = """<?xml version="1.0" encoding="UTF-8" ?>
<!--
Style name:  Code Monkey AMOLED
Description: Pure-black AMOLED port of the Code Monkey MediaMonkey skin, with
             Visual Studio (VS Code Dark+) syntax colors and Inconsolata Nerd Font Mono.
Source:      https://github.com/dooory/code-monkey-amoled
Model:       stylers.model.xml modelDate {model_date} (Notepad++ {npp_version})
License:     MIT, see LICENSE.md
-->
"""


def attrs(d, order):
    return " ".join(f"{k}={quoteattr(d[k])}" for k in order if k in d and d[k] is not None)


def main(model_path, out_path, npp_version):
    root = ET.parse(model_path).getroot()
    out = [HEADER.format(model_date=root.get("modelDate"), npp_version=npp_version)]
    out.append(f'<NotepadPlus modelDate="{root.get("modelDate")}">\n    <LexerStyles>\n')
    for lt in root.find("LexerStyles"):
        lex = lt.get("name")
        out.append(f'        <LexerType {attrs(dict(lt.attrib), ["name", "desc", "ext"])}>\n')
        for ws in lt:
            d = dict(ws.attrib)
            fg, bg, fs = classify(lex, d["name"])
            if fg is not None and "fgColor" in d:
                d["fgColor"] = fg
            if "bgColor" in d:
                d["bgColor"] = bg
            if fs is not None and "fontStyle" in d:
                d["fontStyle"] = str(fs)
            if "fontName" in d:
                d["fontName"] = ""
            if "fontSize" in d:
                d["fontSize"] = ""
            order = ["name", "styleID", "fgColor", "bgColor", "fontName", "fontStyle", "fontSize", "keywordClass"]
            order += [k for k in d if k not in order]
            out.append(f"            <WordsStyle {attrs(d, order)} />\n")
        out.append("        </LexerType>\n")
    out.append("    </LexerStyles>\n    <GlobalStyles>\n")
    seen = set()
    for w in root.find("GlobalStyles"):
        d = dict(w.attrib)
        name = d["name"]
        seen.add(name)
        if name not in GLOBAL:
            raise SystemExit(f"no global mapping for {name!r}")
        for k, v in GLOBAL[name].items():
            d[k] = v
        order = ["name", "styleID", "fgColor", "bgColor", "fontName", "fontStyle", "fontSize"]
        order += [k for k in d if k not in order]
        out.append(f"        <WidgetStyle {attrs(d, order)} />\n")
    missing = set(GLOBAL) - seen
    if missing:
        raise SystemExit(f"mapped globals not in model: {missing}")
    out.append("    </GlobalStyles>\n</NotepadPlus>\n")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:  # UTF-8, no BOM
        f.write("".join(out))
    for name, lexers in sorted(unmatched.items()):
        print("UNMATCHED", name, sorted(set(lexers)))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "?")
