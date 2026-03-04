"""
Gorgon Doc Generator
---------------------
enhanced_data.json'dan her modul icin bir .md dosyasi uretir.
Cikti dizininde VitePress uyumlu yapilandirilmis dokumantasyon olusturur.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

# ─── Ayarlar ──────────────────────────────────────────────────────────────────
INPUT_FILE  = "enhanced_data.json"
OUTPUT_DIR  = Path("docs")            # Markdown ciktilari buraya
SITE_TITLE  = "Gorgon Game Engine"
SITE_DESC   = "C++ Oyun Kütüphanesi Dokümantasyonu"


# ─── Markdown Yardımcıları ─────────────────────────────────────────────────────
def md_badge(text: str, color: str = "blue") -> str:
    label = text.replace(" ", "%20")
    return f"![{text}](https://img.shields.io/badge/{label}-{color})"


def md_code(code: str, lang: str = "cpp") -> str:
    if not code:
        return ""
    return f"\n```{lang}\n{code.strip()}\n```\n"


def md_table(headers: list, rows: list) -> str:
    sep = "|".join(["---"] * len(headers))
    hdr = "| " + " | ".join(headers) + " |"
    rows_md = "\n".join("| " + " | ".join(str(c) for c in row) + " |" for row in rows)
    return f"{hdr}\n|{sep}|\n{rows_md}"


# ─── Modül MD Üretici ─────────────────────────────────────────────────────────
def generate_module_md(module_name: str, files: list) -> str:
    lines = []

    # Başlık
    lines.append(f"# {module_name}\n")
    lines.append(f"> Auto-generated documentation for the **{module_name}** module of the Gorgon C++ Game Engine.\n")
    lines.append("")

    # İçindekiler
    toc = []
    all_classes = [cls for fd in files for cls in fd.get("classes", [])]
    all_enums   = [e for fd in files for e in fd.get("enums", [])]
    all_fns     = [fn for fd in files for fn in fd.get("free_functions", [])]

    if all_classes:
        toc.append("- [Classes](#classes)")
    if all_enums:
        toc.append("- [Enums](#enums)")
    if all_fns:
        toc.append("- [Functions](#functions)")

    if toc:
        lines.append("## Contents\n")
        lines.extend(toc)
        lines.append("")

    # ── Classes ───────────────────────────────────────────────────────────────
    if all_classes:
        lines.append("---\n\n## Classes\n")
        for cls in all_classes:
            ns   = cls.get("namespace") or ""
            desc = cls.get("description", "")
            methods = cls.get("methods", [])

            lines.append(f"### `{cls['name']}`\n")
            if ns:
                lines.append(f"**Namespace:** `{ns}`\n")
            if desc:
                lines.append(f"{desc}\n")

            if methods:
                lines.append("#### Methods\n")
                for m in methods:
                    m_desc  = m.get("description", "")
                    m_params = ", ".join(m.get("params", [])) if m.get("params") else "—"
                    m_ret   = m.get("return_type", "void")
                    m_ex    = m.get("example", "")

                    markers = []
                    if m.get("is_virtual"): markers.append("`virtual`")
                    if m.get("is_static"):  markers.append("`static`")
                    marker_str = " ".join(markers) + " " if markers else ""

                    lines.append(f"##### {marker_str}`{m['name']}({m_params})`\n")
                    lines.append(f"**Returns:** `{m_ret}`\n")
                    if m_desc:
                        lines.append(f"{m_desc}\n")
                    if m_ex:
                        lines.append("**Example:**")
                        lines.append(md_code(m_ex))
            lines.append("")

    # ── Enums ─────────────────────────────────────────────────────────────────
    if all_enums:
        lines.append("---\n\n## Enums\n")
        for enum in all_enums:
            ns   = enum.get("namespace") or ""
            desc = enum.get("description", "")
            vals = enum.get("values", [])

            lines.append(f"### `{enum['name']}`\n")
            if ns:
                lines.append(f"**Namespace:** `{ns}`\n")
            if desc:
                lines.append(f"{desc}\n")

            if vals:
                rows = [(v.get("name", ""), v.get("description", "")) for v in vals]
                lines.append(md_table(["Value", "Description"], rows))
            lines.append("")

    # ── Free Functions ────────────────────────────────────────────────────────
    if all_fns:
        lines.append("---\n\n## Functions\n")
        for fn in all_fns:
            ns     = fn.get("namespace") or ""
            desc   = fn.get("description", "")
            params = ", ".join(fn.get("params", [])) if fn.get("params") else ""
            ret    = fn.get("return_type", "void")
            ex     = fn.get("example", "")

            lines.append(f"### `{fn['name']}({params})`\n")
            lines.append(f"**Returns:** `{ret}`")
            if ns:
                lines.append(f"  |  **Namespace:** `{ns}`")
            lines.append("\n")
            if desc:
                lines.append(f"{desc}\n")
            if ex:
                lines.append("**Example:**")
                lines.append(md_code(ex))
            lines.append("")

    return "\n".join(lines)


def generate_index_md(module_names: list) -> str:
    lines = [
        f"# {SITE_TITLE}",
        "",
        f"> {SITE_DESC}",
        "",
        "## Modules",
        "",
    ]
    for name in sorted(module_names):
        lines.append(f"- [{name}](./{name}/index.md)")
    lines.append("")
    return "\n".join(lines)


def generate_vitepress_config(module_names: list) -> str:
    sidebar_items = ",\n      ".join(
        f'{{ text: "{m}", link: "/{m}/" }}' for m in sorted(module_names)
    )
    return f"""\
import {{ defineConfig }} from 'vitepress'

export default defineConfig({{
  title: '{SITE_TITLE}',
  description: '{SITE_DESC}',
  themeConfig: {{
    nav: [
      {{ text: 'Home', link: '/' }},
    ],
    sidebar: [
      {{
        text: 'Modules',
        items: [
          {sidebar_items}
        ]
      }}
    ],
    socialLinks: [
      {{ icon: 'github', link: 'https://github.com/YOUR_USERNAME/gorgon-docs' }}
    ],
    search: {{
      provider: 'local'
    }}
  }}
}})
"""


# ─── Ana Akış ─────────────────────────────────────────────────────────────────
def run(input_file: str = None, output_dir: str = None):
    inp = input_file or INPUT_FILE
    out = Path(output_dir) if output_dir else OUTPUT_DIR

    print(f"[Generator] Girdi: {inp}")
    with open(inp, 'r', encoding='utf-8') as f:
        all_data = json.load(f)

    # Modüle göre grupla
    modules: dict[str, list] = defaultdict(list)
    for fd in all_data:
        mod = fd.get("module", "misc")
        modules[mod].append(fd)

    # Cikti dizinlerini olustur
    (out / ".vitepress").mkdir(parents=True, exist_ok=True)

    # Her modul icin MD uret
    for mod_name, files in modules.items():
        mod_dir = out / mod_name
        mod_dir.mkdir(parents=True, exist_ok=True)
        md = generate_module_md(mod_name, files)
        md_path = mod_dir / "index.md"
        md_path.write_text(md, encoding='utf-8')
        print(f"  Yazildi: {md_path}")

    # Anasayfa index.md
    idx_md = generate_index_md(list(modules.keys()))
    (out / "index.md").write_text(idx_md, encoding='utf-8')
    print(f"  Yazildi: {out}/index.md")

    # VitePress config
    cfg = generate_vitepress_config(list(modules.keys()))
    cfg_path = out / ".vitepress" / "config.mjs"
    cfg_path.write_text(cfg, encoding='utf-8')
    print(f"  Yazildi: {cfg_path}")

    print(f"\n[Generator] Tamamlandi! {len(modules)} modul icin dokuman uretildi.")
    print(f"  Cikti dizini: {out.resolve()}")
    return str(out.resolve())


if __name__ == "__main__":
    inp = sys.argv[1] if len(sys.argv) > 1 else None
    out = sys.argv[2] if len(sys.argv) > 2 else None
    run(input_file=inp, output_dir=out)
