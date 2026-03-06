#!/usr/bin/env python3
"""
Gorgon Game Engine — Static Documentation Site Generator
Reads markdown docs and generates a beautiful, self-contained HTML website.
All dependencies (CSS, JS, fonts) are bundled inline or locally.
"""

import os
import re
import json
import shutil
import html as html_module

# ─── Configuration ───────────────────────────────────────────────────────────
DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "site")
SITE_TITLE = "Gorgon Game Engine"
SITE_DESC = "C++ Game Library Documentation"

# ─── Markdown → HTML converter (pure Python, no dependencies) ──────────────

def md_to_html(md_text):
    """Convert markdown to HTML without external libraries."""
    lines = md_text.replace('\r\n', '\n').split('\n')
    html_parts = []
    in_code_block = False
    code_lang = ""
    code_lines = []
    in_table = False
    table_rows = []
    in_list = False
    list_items = []

    def flush_list():
        nonlocal in_list, list_items
        if in_list and list_items:
            html_parts.append('<ul class="md-list">')
            for item in list_items:
                html_parts.append(f'<li>{inline_format(item)}</li>')
            html_parts.append('</ul>')
            list_items = []
            in_list = False

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            html_parts.append('<div class="table-wrapper"><table>')
            for i, row in enumerate(table_rows):
                if i == 1 and all(c in '-| ' for c in row):
                    continue  # skip separator row
                cells = [c.strip() for c in row.split('|')[1:-1]]
                tag = 'th' if i == 0 else 'td'
                row_class = 'thead-row' if i == 0 else ''
                html_parts.append(f'<tr class="{row_class}">')
                for cell in cells:
                    html_parts.append(f'<{tag}>{inline_format(cell)}</{tag}>')
                html_parts.append('</tr>')
            html_parts.append('</table></div>')
            table_rows = []
            in_table = False

    def inline_format(text):
        """Handle inline markdown: bold, italic, code, links."""
        # Code spans
        text = re.sub(r'`([^`]+)`', r'<code class="inline-code">\1</code>', text)
        # Bold + italic
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
        # Bold
        text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
        # Italic
        text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
        # Links
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
        # HTML entities
        text = text.replace('&gt;', '>')
        text = text.replace('&lt;', '<')
        return text

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                escaped_code = html_module.escape('\n'.join(code_lines))
                html_parts.append(f'<pre class="code-block" data-lang="{code_lang}"><code>{escaped_code}</code></pre>')
                in_code_block = False
                code_lines = []
                code_lang = ""
            else:
                flush_list()
                flush_table()
                in_code_block = True
                code_lang = line.strip()[3:].strip()
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        stripped = line.strip()

        # Empty line
        if not stripped:
            flush_list()
            flush_table()
            continue

        # Table
        if '|' in stripped and stripped.startswith('|'):
            if not in_table:
                flush_list()
                in_table = True
            table_rows.append(stripped)
            continue
        else:
            flush_table()

        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if header_match:
            flush_list()
            level = len(header_match.group(1))
            text = header_match.group(2)
            anchor = re.sub(r'[^a-z0-9-]', '', text.lower().replace(' ', '-'))
            html_parts.append(f'<h{level} id="{anchor}" class="doc-heading">{inline_format(text)}</h{level}>')
            continue

        # Horizontal rule
        if stripped in ('---', '***', '___'):
            flush_list()
            html_parts.append('<hr class="doc-divider">')
            continue

        # Blockquote
        if stripped.startswith('>'):
            flush_list()
            text = stripped[1:].strip()
            html_parts.append(f'<blockquote class="doc-quote">{inline_format(text)}</blockquote>')
            continue

        # List items
        if re.match(r'^[-*+]\s+', stripped):
            in_list = True
            item_text = re.sub(r'^[-*+]\s+', '', stripped)
            list_items.append(item_text)
            continue
        if re.match(r'^\d+\.\s+', stripped):
            in_list = True
            item_text = re.sub(r'^\d+\.\s+', '', stripped)
            list_items.append(item_text)
            continue

        # Normal paragraph
        flush_list()
        html_parts.append(f'<p class="doc-paragraph">{inline_format(stripped)}</p>')

    # Flush remaining
    flush_list()
    flush_table()
    if in_code_block:
        escaped_code = html_module.escape('\n'.join(code_lines))
        html_parts.append(f'<pre class="code-block" data-lang="{code_lang}"><code>{escaped_code}</code></pre>')

    return '\n'.join(html_parts)


# ─── Collect all modules ─────────────────────────────────────────────────────

def collect_modules():
    """Scan docs/ for module directories."""
    modules = []
    for name in sorted(os.listdir(DOCS_DIR)):
        path = os.path.join(DOCS_DIR, name, "index.md")
        if os.path.isfile(path) and name not in ('.vitepress', 'getting-started'):
            modules.append(name)
    return modules


def read_md(filepath):
    """Read a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


# ─── Categorize modules ─────────────────────────────────────────────────────

CATEGORIES = {
    "🎮 Core": ["Base", "Basic", "Common", "Config", "Definitions", "Environment",
                 "Main", "OS", "Runtime", "Types", "Utils", "UtilsBase"],
    "🖼️ Graphics": ["Graphics", "Bitmap", "BitmapFont", "BlankImage", "Color",
                     "ColorPicker", "ColorPlane", "ColorSpaces", "Drawables",
                     "EmptyImage", "Filters", "Flip", "Font", "FontTheme",
                     "FrameBuffer", "FreeType", "GL", "GID", "HTMLRenderer",
                     "IL", "Image", "JPEG", "OpenGL", "PNG", "Renderer",
                     "ScalableObject", "Shader", "Shaders", "Texture",
                     "TextureAnimation", "TextureTargets", "Tinting",
                     "TintedObject"],
    "🎬 Animation": ["Animation", "AnimationServices", "AnimationStorage",
                      "Animations", "Controllers", "ControlledTimer"],
    "🖱️ Input": ["Input", "Keyboard", "KeyRepeater", "Mouse", "DnD"],
    "🪟 UI & Widgets": ["UI", "Widget", "WidgetContainer", "WidgetLayer",
                         "WidgetRegistry", "Button", "Checkbox", "CheckboxBase",
                         "CheckboxBlueprint", "Combobox", "ComboboxBase",
                         "ComboboxBlueprint", "Dialog", "DialogWindow",
                         "Dropdown", "Inputbox", "Label", "Listbox",
                         "ListboxBase", "ListboxBlueprint", "Numberbox",
                         "Panel", "PanelBase", "PanelBlueprint", "Progressbar",
                         "Percentbar", "RadioButton", "RadioButtons",
                         "RadioControl", "Scrollbar", "ScrollingWidget",
                         "Slider", "SliderBase", "SliderBlueprint", "Spinner",
                         "Textarea", "Textbox", "TextboxBase", "TextboxBlueprint",
                         "Tabpanel", "TabpanelBlueprint", "TabPanelPanel",
                         "TooltipManager", "Placeholder", "StatefulLabel",
                         "NumberInput", "TextInput", "CountingText", "Filler",
                         "IButton", "ICheckbox", "ILabel", "IListItem",
                         "INumberbox", "IOption", "IProgressor", "IScroller",
                         "ISlider", "ITextbox", "TwoStateControl",
                         "PetContainer", "PetTextbox"],
    "📐 Geometry": ["Geometry", "GeometryBoxes", "Point", "Point3D", "PointList",
                     "PointProperty", "Size", "SizeProperty", "Bounds",
                     "Rectangle", "Circle", "Line", "Polygon", "Region",
                     "Dimension", "Margin", "Alignment", "Transform3D",
                     "Bezier"],
    "🔊 Audio": ["Audio", "AudioStream", "Sound", "Source", "FLAC", "Vorbis",
                  "Wave", "PulseAudio", "PulseAudio.inc", "WASAPI", "WASAPI.inc",
                  "Multimedia"],
    "📁 IO & Data": ["File", "FileDialog", "Filesystem", "Folder", "Stream",
                      "MemoryStream", "Reader", "Writer", "Data", "DataExchange",
                      "DataItems", "Blob", "Storage", "LZMA", "CGI", "HTTP",
                      "URI", "Markdown", "Parse", "Tokenizer", "Query",
                      "Clipboard"],
    "🧩 Containers": ["Array", "Collection", "Container", "Hashmap", "Iterator",
                       "LinkNode", "List", "ListItem", "Vector"],
    "🪟 Window & Layout": ["Window", "WindowManager", "Layer", "LayerAdapter",
                            "LayerMover", "LayerResizer", "LayerWidget",
                            "Layerbox", "CustomLayer", "ExtenderLayer",
                            "FullscreenPanel", "InlinePanel", "ControlledPanel",
                            "VirtualPanel", "StackedObject", "ComponentStack",
                            "ComponentStackWidget", "Flow", "LinearOrganizer",
                            "ListOrganizer", "MovingListOrganizer", "Organizer",
                            "MaskedObject", "BorderData", "Monitor", "DWM"],
    "⚙️ System": ["Threading", "Timer", "Time", "Event", "ConsumableEvent",
                   "Exception", "Exceptions", "Assert", "Assert_Linux",
                   "Assert_Win32", "Logging", "Console", "Console_Nix",
                   "Console_Win32", "Random", "SGuid", "ScopeGuard", "Scope",
                   "Property", "CaptionValue", "Pointer", "Nullable", "Null",
                   "RefCounter", "GarbageCollection", "Registry"],
    "🔧 Advanced": ["AST", "AStar", "Pathfinders", "Scripting", "VirtualMachine",
                     "Instruction", "RuntimeFunction", "Compiler", "Compiler_GCC",
                     "Compiler_MSVC", "Compilers", "Reflection", "Enum",
                     "Struct", "Template", "Generator", "Blueprint", "Component",
                     "Composer", "Message", "Validators", "Simple", "Discrete",
                     "Language", "TMP", "String", "Embedding", "Scene",
                     "TiledMap", "World"],
    "🗔 Platform": ["Win32", "Windows", "Linux", "X11", "X11Keysym"],
    "📝 Text": ["AdvancedPrinter", "AdvancedPrinterConstants",
                 "AdvancedPrinterImpl", "AdvancedTextBuilder", "Marking",
                 "CastableManagedBuffer"],
    "🧱 Resources": ["Resource", "ResizableObjectResource", "Instance",
                      "FindObject", "ObjectFinding", "Helpers", "Any",
                      "PD", "Builtin"],
}


def get_category(module_name):
    for cat, members in CATEGORIES.items():
        if module_name in members:
            return cat
    return "📦 Other"


# ─── CSS ─────────────────────────────────────────────────────────────────────

def get_css():
    return '''/* Gorgon Docs — Design System */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
    --bg-primary: #0a0e1a;
    --bg-secondary: #111827;
    --bg-card: rgba(17, 24, 39, 0.8);
    --bg-card-hover: rgba(30, 41, 59, 0.9);
    --bg-sidebar: #0f1629;
    --bg-code: #1a1f35;
    --border: rgba(99, 102, 241, 0.15);
    --border-hover: rgba(99, 102, 241, 0.4);
    --text-primary: #e2e8f0;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    --accent: #6366f1;
    --accent-light: #818cf8;
    --accent-glow: rgba(99, 102, 241, 0.3);
    --green: #10b981;
    --orange: #f59e0b;
    --red: #ef4444;
    --cyan: #06b6d4;
    --pink: #ec4899;
    --sidebar-width: 280px;
    --header-height: 64px;
    --transition: 0.2s ease;
}

html { scroll-behavior: smooth; }

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.7;
    min-height: 100vh;
    overflow-x: hidden;
}

/* ─── Header ─── */
.site-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: var(--header-height);
    background: rgba(10, 14, 26, 0.85);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    padding: 0 24px;
    z-index: 1000;
}

.header-brand {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
    color: var(--text-primary);
}

.header-logo {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, var(--accent), var(--cyan));
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 700;
    color: white;
}

.header-title {
    font-size: 18px;
    font-weight: 700;
    letter-spacing: -0.3px;
}

.header-subtitle {
    font-size: 12px;
    color: var(--text-muted);
    margin-left: -12px;
}

.header-nav {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-left: auto;
}

.header-nav a {
    color: var(--text-secondary);
    text-decoration: none;
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 500;
    transition: var(--transition);
}

.header-nav a:hover, .header-nav a.active {
    color: var(--text-primary);
    background: rgba(99, 102, 241, 0.1);
}

.menu-toggle {
    display: none;
    background: none;
    border: 1px solid var(--border);
    color: var(--text-primary);
    width: 40px;
    height: 40px;
    border-radius: 8px;
    font-size: 20px;
    cursor: pointer;
    align-items: center;
    justify-content: center;
}

/* ─── Sidebar ─── */
.sidebar {
    position: fixed;
    top: var(--header-height);
    left: 0;
    width: var(--sidebar-width);
    height: calc(100vh - var(--header-height));
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    padding: 16px 0;
    z-index: 900;
    transition: transform 0.3s ease;
}

.sidebar-search {
    padding: 0 16px 16px;
    position: sticky;
    top: 0;
    background: var(--bg-sidebar);
    z-index: 5;
}

.sidebar-search input {
    width: 100%;
    padding: 10px 14px;
    border-radius: 8px;
    border: 1px solid var(--border);
    background: var(--bg-primary);
    color: var(--text-primary);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: var(--transition);
}

.sidebar-search input:focus {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px var(--accent-glow);
}

.sidebar-search input::placeholder { color: var(--text-muted); }

.sidebar-group { margin-bottom: 8px; }

.sidebar-group-title {
    padding: 8px 20px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--text-muted);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
    user-select: none;
}

.sidebar-group-title:hover { color: var(--text-secondary); }

.sidebar-group-title .chevron {
    transition: transform 0.2s;
    font-size: 10px;
}

.sidebar-group.collapsed .chevron { transform: rotate(-90deg); }
.sidebar-group.collapsed .sidebar-links { display: none; }

.sidebar-links { list-style: none; }

.sidebar-links a {
    display: block;
    padding: 5px 20px 5px 28px;
    color: var(--text-secondary);
    text-decoration: none;
    font-size: 13px;
    transition: var(--transition);
    border-left: 2px solid transparent;
}

.sidebar-links a:hover {
    color: var(--text-primary);
    background: rgba(99, 102, 241, 0.05);
    border-left-color: var(--accent);
}

.sidebar-links a.active {
    color: var(--accent-light);
    background: rgba(99, 102, 241, 0.1);
    border-left-color: var(--accent);
    font-weight: 500;
}

/* ─── Content ─── */
.main-content {
    margin-left: var(--sidebar-width);
    margin-top: var(--header-height);
    min-height: calc(100vh - var(--header-height));
    padding: 40px 48px 80px;
    max-width: 960px;
}

.main-content.full-width {
    max-width: 100%;
}

/* ─── HOME PAGE ─── */
.hero {
    text-align: center;
    padding: 60px 0 40px;
    position: relative;
}

.hero::before {
    content: '';
    position: absolute;
    top: -100px;
    left: 50%;
    transform: translateX(-50%);
    width: 600px;
    height: 400px;
    background: radial-gradient(ellipse, var(--accent-glow), transparent 70%);
    pointer-events: none;
    opacity: 0.4;
}

.hero h1 {
    font-size: 48px;
    font-weight: 700;
    letter-spacing: -1.5px;
    background: linear-gradient(135deg, var(--text-primary), var(--accent-light));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
    position: relative;
}

.hero p {
    font-size: 18px;
    color: var(--text-secondary);
    max-width: 500px;
    margin: 0 auto 32px;
}

.hero-stats {
    display: flex;
    justify-content: center;
    gap: 32px;
    margin-bottom: 40px;
}

.hero-stat {
    text-align: center;
}

.hero-stat .number {
    font-size: 28px;
    font-weight: 700;
    color: var(--accent-light);
}

.hero-stat .label {
    font-size: 12px;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.hero-actions {
    display: flex;
    justify-content: center;
    gap: 12px;
}

.btn {
    padding: 12px 24px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    transition: var(--transition);
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.btn-primary {
    background: linear-gradient(135deg, var(--accent), #4f46e5);
    color: white;
    border: none;
    box-shadow: 0 4px 15px var(--accent-glow);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px var(--accent-glow);
}

.btn-outline {
    background: transparent;
    color: var(--text-primary);
    border: 1px solid var(--border);
}

.btn-outline:hover {
    border-color: var(--accent);
    background: rgba(99, 102, 241, 0.1);
}

/* Category sections */
.category-section {
    margin-bottom: 40px;
}

.category-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
    color: var(--text-primary);
}

.module-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
    gap: 12px;
}

.module-card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    text-decoration: none;
    color: var(--text-primary);
    transition: all 0.25s ease;
    display: flex;
    align-items: center;
    gap: 10px;
    position: relative;
    overflow: hidden;
}

.module-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--cyan));
    opacity: 0;
    transition: opacity 0.25s;
}

.module-card:hover {
    background: var(--bg-card-hover);
    border-color: var(--border-hover);
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
}

.module-card:hover::before { opacity: 1; }

.module-card .icon {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    background: rgba(99, 102, 241, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    flex-shrink: 0;
}

.module-card .name {
    font-size: 14px;
    font-weight: 500;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* ─── Doc Content Styles ─── */
.doc-heading {
    margin-top: 32px;
    margin-bottom: 12px;
    font-weight: 600;
    letter-spacing: -0.3px;
    line-height: 1.3;
}

h1.doc-heading { font-size: 32px; margin-top: 0; border-bottom: 2px solid var(--border); padding-bottom: 12px; }
h2.doc-heading { font-size: 24px; color: var(--accent-light); margin-top: 40px; }
h3.doc-heading { font-size: 18px; margin-top: 28px; }
h4.doc-heading { font-size: 15px; color: var(--text-secondary); margin-top: 20px; }
h5.doc-heading { font-size: 14px; color: var(--cyan); margin-top: 16px; font-family: 'JetBrains Mono', monospace; }

.doc-paragraph {
    margin-bottom: 12px;
    color: var(--text-secondary);
    font-size: 15px;
    line-height: 1.8;
}

.doc-quote {
    margin: 16px 0;
    padding: 12px 20px;
    border-left: 3px solid var(--accent);
    background: rgba(99, 102, 241, 0.05);
    border-radius: 0 8px 8px 0;
    color: var(--text-secondary);
    font-style: italic;
}

.doc-divider {
    margin: 32px 0;
    border: none;
    border-top: 1px solid var(--border);
}

.md-list {
    margin: 12px 0;
    padding-left: 24px;
}

.md-list li {
    color: var(--text-secondary);
    font-size: 15px;
    margin-bottom: 6px;
    line-height: 1.6;
}

.inline-code {
    background: var(--bg-code);
    padding: 2px 8px;
    border-radius: 5px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85em;
    color: var(--cyan);
    border: 1px solid rgba(6, 182, 212, 0.15);
}

.code-block {
    background: var(--bg-code);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    margin: 16px 0;
    overflow-x: auto;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    line-height: 1.7;
    color: var(--text-primary);
    position: relative;
}

.code-block::before {
    content: attr(data-lang);
    position: absolute;
    top: 8px;
    right: 12px;
    font-size: 11px;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.code-block code {
    font-family: inherit;
    background: none;
    padding: 0;
    border: none;
    color: inherit;
}

.table-wrapper {
    margin: 16px 0;
    overflow-x: auto;
    border-radius: 10px;
    border: 1px solid var(--border);
}

table {
    width: 100%;
    border-collapse: collapse;
    background: var(--bg-secondary);
}

th, td {
    padding: 10px 16px;
    text-align: left;
    border-bottom: 1px solid var(--border);
    font-size: 14px;
}

th {
    background: var(--bg-code);
    font-weight: 600;
    color: var(--text-primary);
}

td { color: var(--text-secondary); }

/* ─── Breadcrumb ─── */
.breadcrumb {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 24px;
    font-size: 13px;
}

.breadcrumb a {
    color: var(--text-muted);
    text-decoration: none;
}

.breadcrumb a:hover { color: var(--accent-light); }
.breadcrumb .sep { color: var(--text-muted); }
.breadcrumb .current { color: var(--text-secondary); }

/* ─── Footer ─── */
.site-footer {
    margin-left: var(--sidebar-width);
    padding: 24px 48px;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--text-muted);
    font-size: 13px;
}

/* ─── Scrollbar ─── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-muted); }

/* ─── Responsive ─── */
@media (max-width: 768px) {
    .sidebar { transform: translateX(-100%); }
    .sidebar.open { transform: translateX(0); }
    .main-content { margin-left: 0; padding: 24px 16px 60px; }
    .site-footer { margin-left: 0; }
    .menu-toggle { display: flex; }
    .hero h1 { font-size: 32px; }
    .header-subtitle { display: none; }
    .module-grid { grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); }
}
'''


# ─── JavaScript ──────────────────────────────────────────────────────────────

def get_js():
    return '''// Gorgon Docs — Client-side interactivity

document.addEventListener('DOMContentLoaded', function() {
    // ─── Sidebar Search Filter ───
    const searchInput = document.getElementById('sidebar-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().trim();
            const groups = document.querySelectorAll('.sidebar-group');
            
            groups.forEach(group => {
                const links = group.querySelectorAll('.sidebar-links a');
                let hasVisible = false;
                
                links.forEach(link => {
                    const text = link.textContent.toLowerCase();
                    if (!query || text.includes(query)) {
                        link.style.display = '';
                        hasVisible = true;
                    } else {
                        link.style.display = 'none';
                    }
                });
                
                group.style.display = hasVisible ? '' : 'none';
                
                // Auto expand groups with matches
                if (query && hasVisible) {
                    group.classList.remove('collapsed');
                }
            });
        });
    }

    // ─── Sidebar Group Toggle ───
    document.querySelectorAll('.sidebar-group-title').forEach(title => {
        title.addEventListener('click', function() {
            this.parentElement.classList.toggle('collapsed');
        });
    });

    // ─── Mobile Menu Toggle ───
    const menuBtn = document.getElementById('menu-toggle');
    const sidebar = document.getElementById('sidebar');
    if (menuBtn && sidebar) {
        menuBtn.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });
        
        // Close sidebar on link click (mobile)
        sidebar.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                sidebar.classList.remove('open');
            });
        });
    }

    // ─── Highlight active sidebar link ───
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.sidebar-links a').forEach(link => {
        const href = link.getAttribute('href').split('/').pop();
        if (href === currentPage) {
            link.classList.add('active');
            // Expand parent group
            const group = link.closest('.sidebar-group');
            if (group) group.classList.remove('collapsed');
        }
    });
});
'''


# ─── HTML Templates ──────────────────────────────────────────────────────────

def html_page(title, content, is_home=False, current_module=None, modules=None, breadcrumb=""):
    """Generate a complete HTML page."""
    if modules is None:
        modules = []

    # Build sidebar groups
    categorized = {}
    uncategorized = []
    for mod in modules:
        cat = get_category(mod)
        if cat == "📦 Other":
            uncategorized.append(mod)
        else:
            categorized.setdefault(cat, []).append(mod)

    sidebar_html = '<div class="sidebar-search"><input type="text" id="sidebar-search" placeholder="Search modules..."></div>\n'

    # Getting Started link
    sidebar_html += '<div class="sidebar-group">\n'
    sidebar_html += '  <div class="sidebar-group-title">🚀 Guide <span class="chevron">▼</span></div>\n'
    sidebar_html += '  <ul class="sidebar-links">\n'
    sidebar_html += '    <li><a href="getting-started.html">Getting Started</a></li>\n'
    sidebar_html += '  </ul>\n'
    sidebar_html += '</div>\n'

    # Category groups
    for cat_name in CATEGORIES.keys():
        if cat_name not in categorized:
            continue
        mods = categorized[cat_name]
        collapsed = ' collapsed' if not is_home else ''
        sidebar_html += f'<div class="sidebar-group{collapsed}">\n'
        sidebar_html += f'  <div class="sidebar-group-title">{cat_name} <span class="chevron">▼</span></div>\n'
        sidebar_html += '  <ul class="sidebar-links">\n'
        for mod in sorted(mods):
            active = ' class="active"' if mod == current_module else ''
            sidebar_html += f'    <li><a href="modules/{mod}.html"{active}>{mod}</a></li>\n'
        sidebar_html += '  </ul>\n'
        sidebar_html += '</div>\n'

    # Uncategorized
    if uncategorized:
        sidebar_html += '<div class="sidebar-group collapsed">\n'
        sidebar_html += '  <div class="sidebar-group-title">📦 Other <span class="chevron">▼</span></div>\n'
        sidebar_html += '  <ul class="sidebar-links">\n'
        for mod in sorted(uncategorized):
            active = ' class="active"' if mod == current_module else ''
            sidebar_html += f'    <li><a href="modules/{mod}.html"{active}>{mod}</a></li>\n'
        sidebar_html += '  </ul>\n'
        sidebar_html += '</div>\n'

    # Fix relative paths for module pages
    css_path = "css/style.css"
    js_path = "js/app.js"
    home_link = "index.html"
    gs_link = "getting-started.html"

    if current_module:
        css_path = "../css/style.css"
        js_path = "../js/app.js"
        home_link = "../index.html"
        gs_link = "../getting-started.html"
        # Fix sidebar links
        sidebar_html = sidebar_html.replace('href="modules/', 'href="')
        sidebar_html = sidebar_html.replace('href="getting-started.html"', f'href="{gs_link}"')

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{SITE_DESC}">
    <title>{title} — {SITE_TITLE}</title>
    <link rel="stylesheet" href="{css_path}">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎮</text></svg>">
</head>
<body>
    <header class="site-header">
        <button class="menu-toggle" id="menu-toggle">☰</button>
        <a href="{home_link}" class="header-brand">
            <div class="header-logo">G</div>
            <span class="header-title">{SITE_TITLE}</span>
        </a>
        <span class="header-subtitle">&nbsp;Documentation</span>
        <nav class="header-nav">
            <a href="{home_link}"{' class="active"' if is_home else ''}>Home</a>
            <a href="{gs_link}">Getting Started</a>
        </nav>
    </header>

    <aside class="sidebar" id="sidebar">
        {sidebar_html}
    </aside>

    <main class="main-content{"  full-width" if is_home else ""}">
        {breadcrumb}
        {content}
    </main>

    <footer class="site-footer">
        <p>Gorgon Game Engine Documentation &mdash; Auto-generated with ❤️</p>
    </footer>

    <script src="{js_path}"></script>
</body>
</html>'''


# ─── Page Generators ─────────────────────────────────────────────────────────

def generate_home_page(modules):
    """Generate the home page with module cards organized by category."""
    categorized = {}
    uncategorized = []
    for mod in modules:
        cat = get_category(mod)
        if cat == "📦 Other":
            uncategorized.append(mod)
        else:
            categorized.setdefault(cat, []).append(mod)

    content = f'''
    <div class="hero">
        <h1>Gorgon Game Engine</h1>
        <p>Modern C++ Game Library — Complete API Documentation</p>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="number">{len(modules)}</div>
                <div class="label">Modules</div>
            </div>
            <div class="hero-stat">
                <div class="number">{len(CATEGORIES)}</div>
                <div class="label">Categories</div>
            </div>
            <div class="hero-stat">
                <div class="number">C++</div>
                <div class="label">Language</div>
            </div>
        </div>
        <div class="hero-actions">
            <a href="getting-started.html" class="btn btn-primary">🚀 Getting Started</a>
            <a href="https://github.com/civanorak/AutoDocGenerator" class="btn btn-outline">GitHub</a>
        </div>
    </div>
    '''

    cat_icons = {
        "🎮 Core": "⚡", "🖼️ Graphics": "🎨", "🎬 Animation": "🎬",
        "🖱️ Input": "🖱️", "🪟 UI & Widgets": "🧩", "📐 Geometry": "📐",
        "🔊 Audio": "🔊", "📁 IO & Data": "📁", "🧩 Containers": "📦",
        "🪟 Window & Layout": "🪟", "⚙️ System": "⚙️", "🔧 Advanced": "🔧",
        "🗔 Platform": "💻", "📝 Text": "📝", "🧱 Resources": "🧱",
    }

    for cat_name in CATEGORIES.keys():
        if cat_name not in categorized:
            continue
        mods = categorized[cat_name]
        icon = cat_icons.get(cat_name, "📦")
        content += f'<div class="category-section">\n'
        content += f'  <h2 class="category-title">{cat_name}</h2>\n'
        content += f'  <div class="module-grid">\n'
        for mod in sorted(mods):
            content += f'    <a href="modules/{mod}.html" class="module-card">\n'
            content += f'      <div class="icon">{icon}</div>\n'
            content += f'      <div class="name">{mod}</div>\n'
            content += f'    </a>\n'
        content += f'  </div>\n'
        content += f'</div>\n'

    if uncategorized:
        content += '<div class="category-section">\n'
        content += '  <h2 class="category-title">📦 Other</h2>\n'
        content += '  <div class="module-grid">\n'
        for mod in sorted(uncategorized):
            content += f'    <a href="modules/{mod}.html" class="module-card">\n'
            content += f'      <div class="icon">📄</div>\n'
            content += f'      <div class="name">{mod}</div>\n'
            content += f'    </a>\n'
        content += '  </div>\n'
        content += '</div>\n'

    return html_page(
        "Home",
        content,
        is_home=True,
        modules=modules,
    )


def generate_module_page(module_name, modules):
    """Generate HTML page for a single module."""
    md_path = os.path.join(DOCS_DIR, module_name, "index.md")
    md_content = read_md(md_path)
    html_content = md_to_html(md_content)

    breadcrumb = f'''
    <nav class="breadcrumb">
        <a href="../index.html">Home</a>
        <span class="sep">›</span>
        <span class="current">{module_name}</span>
    </nav>
    '''

    return html_page(
        module_name,
        html_content,
        current_module=module_name,
        modules=modules,
        breadcrumb=breadcrumb,
    )


def generate_getting_started_page(modules):
    """Generate the getting started page."""
    md_path = os.path.join(DOCS_DIR, "getting-started", "index.md")
    md_content = read_md(md_path)
    html_content = md_to_html(md_content)

    breadcrumb = '''
    <nav class="breadcrumb">
        <a href="index.html">Home</a>
        <span class="sep">›</span>
        <span class="current">Getting Started</span>
    </nav>
    '''

    return html_page(
        "Getting Started",
        html_content,
        modules=modules,
        breadcrumb=breadcrumb,
    )


# ─── Build Site ──────────────────────────────────────────────────────────────

def build():
    print("🔨 Gorgon Docs — Static Site Generator")
    print("=" * 50)

    # 1. Collect modules
    modules = collect_modules()
    print(f"📦 Found {len(modules)} modules")

    # 2. Clean & create output structure
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    os.makedirs(os.path.join(OUTPUT_DIR, "css"))
    os.makedirs(os.path.join(OUTPUT_DIR, "js"))
    os.makedirs(os.path.join(OUTPUT_DIR, "modules"))
    print("📁 Created output directory structure")

    # 3. Write CSS
    with open(os.path.join(OUTPUT_DIR, "css", "style.css"), 'w', encoding='utf-8') as f:
        f.write(get_css())
    print("🎨 Generated CSS")

    # 4. Write JS
    with open(os.path.join(OUTPUT_DIR, "js", "app.js"), 'w', encoding='utf-8') as f:
        f.write(get_js())
    print("⚡ Generated JavaScript")

    # 5. Generate index page
    with open(os.path.join(OUTPUT_DIR, "index.html"), 'w', encoding='utf-8') as f:
        f.write(generate_home_page(modules))
    print("🏠 Generated home page")

    # 6. Generate getting started
    with open(os.path.join(OUTPUT_DIR, "getting-started.html"), 'w', encoding='utf-8') as f:
        f.write(generate_getting_started_page(modules))
    print("📖 Generated Getting Started page")

    # 7. Generate module pages
    for i, mod in enumerate(modules):
        with open(os.path.join(OUTPUT_DIR, "modules", f"{mod}.html"), 'w', encoding='utf-8') as f:
            f.write(generate_module_page(mod, modules))

        if (i + 1) % 50 == 0:
            print(f"   ... {i + 1}/{len(modules)} modules")

    print(f"📚 Generated {len(modules)} module pages")

    # 8. Generate search index JSON
    search_data = []
    for mod in modules:
        search_data.append({
            "name": mod,
            "category": get_category(mod),
            "url": f"modules/{mod}.html"
        })

    with open(os.path.join(OUTPUT_DIR, "js", "search.js"), 'w', encoding='utf-8') as f:
        f.write(f"const SEARCH_INDEX = {json.dumps(search_data, indent=2)};")
    print("🔍 Generated search index")

    print("=" * 50)
    print(f"✅ Site generated successfully!")
    print(f"📂 Output: {OUTPUT_DIR}")
    print(f"🌐 Open: {os.path.join(OUTPUT_DIR, 'index.html')}")


if __name__ == "__main__":
    build()
