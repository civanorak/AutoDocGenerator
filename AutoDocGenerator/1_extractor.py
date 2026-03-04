"""
Gorgon C++ Library Extractor
-----------------------------
*.h ve *.cpp dosyalarini tarayip siniflar, enum'lar, fonksiyonlar
ve /// yorum satirlarini JSON olarak cikartir.
"""

import os
import re
import json
import sys
from pathlib import Path

# ─── Ayarlar ──────────────────────────────────────────────────────────────────
DEFAULT_SOURCE_DIR = r"C:\Users\CİVAN ORAK\Downloads\Gorgon-main\Source\Gorgon"
OUTPUT_FILE = "extracted_data.json"

SKIP_DIRS = {".vs", "External", "build", "install", "__pycache__"}

# ─── Regex Kalıpları ───────────────────────────────────────────────────────────
RE_NAMESPACE   = re.compile(r'^\s*namespace\s+(\w+)\s*\{')
RE_CLASS       = re.compile(r'^\s*(?:class|struct)\s+(\w+)(?:\s*:\s*[^{]+)?\s*\{')
RE_ENUM        = re.compile(r'^\s*enum(?:\s+class)?\s+(\w+)\s*(?::\s*\w+)?\s*\{')
RE_FUNCTION    = re.compile(r'^\s*((?:virtual|static|inline|explicit|constexpr|const)?\s*)'
                            r'([\w:<>*&,\s]+?)\s+(\w+)\s*\(([^)]*)\)\s*(?:const)?\s*(?:=\s*0\s*)?[;{]')
RE_DOC_COMMENT = re.compile(r'^\s*///\s?(.*)')
RE_ENUM_VALUE  = re.compile(r'^\s*(\w+)\s*(?:=\s*[^,\n]+)?,?\s*(?:///\s?(.*))?$')


def collect_files(source_dir: str) -> list[Path]:
    """Tüm .h ve .cpp dosyalarini dondurur."""
    paths = []
    for root, dirs, files in os.walk(source_dir):
        # Atlanan klasorleri cikar
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(('.h', '.cpp')):
                paths.append(Path(root) / f)
    return sorted(paths)


def extract_file(filepath: Path) -> dict:
    """Tek bir .h/.cpp dosyasini analiz edip yapisal veri dondurur."""
    try:
        text = filepath.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return {"file": str(filepath), "error": str(e)}

    lines = text.splitlines()

    result = {
        "file": str(filepath),
        "module": filepath.stem,
        "namespaces": [],
        "classes": [],
        "enums": [],
        "free_functions": [],
        "raw_comments": [],
    }

    pending_comment = []
    current_namespace = None
    current_class = None
    brace_depth = 0
    class_brace_start = -1

    for i, line in enumerate(lines):
        # Parantez derinligi takibi
        brace_depth += line.count('{') - line.count('}')

        # Yorum toplama
        m = RE_DOC_COMMENT.match(line)
        if m:
            pending_comment.append(m.group(1).strip())
            continue

        # Namespace
        m = RE_NAMESPACE.match(line)
        if m:
            ns = m.group(1)
            if ns not in result["namespaces"]:
                result["namespaces"].append(ns)
            current_namespace = ns
            pending_comment.clear()
            continue

        # Class / Struct
        m = RE_CLASS.match(line)
        if m and 'class' in line or (m and 'struct' in line):
            class_name = m.group(1)
            entry = {
                "name": class_name,
                "namespace": current_namespace,
                "description": " ".join(pending_comment) if pending_comment else "",
                "methods": [],
                "line": i + 1,
            }
            result["classes"].append(entry)
            current_class = entry
            class_brace_start = brace_depth
            pending_comment.clear()
            continue

        # Sınıf parantezi kapandıysa sıfırla
        if current_class and brace_depth < class_brace_start:
            current_class = None
            class_brace_start = -1

        # Enum
        m = RE_ENUM.match(line)
        if m:
            enum_name = m.group(1)
            entry = {
                "name": enum_name,
                "namespace": current_namespace,
                "class": current_class["name"] if current_class else None,
                "description": " ".join(pending_comment) if pending_comment else "",
                "values": [],
                "line": i + 1,
            }
            result["enums"].append(entry)
            pending_comment.clear()
            continue

        # Fonksiyon imzasi (sadece istenenler)
        m = RE_FUNCTION.match(line)
        if m:
            func_name = m.group(3).strip()
            # constructor / destructor ve makrolardan kac
            if func_name and func_name[0].islower() or func_name[0].isupper():
                return_type = (m.group(1).strip() + ' ' + m.group(2).strip()).strip()
                params_raw = m.group(4).strip()
                params = [p.strip() for p in params_raw.split(',') if p.strip()] if params_raw else []
                fn_entry = {
                    "name": func_name,
                    "return_type": return_type,
                    "params": params,
                    "description": " ".join(pending_comment) if pending_comment else "",
                    "line": i + 1,
                    "is_virtual": "virtual" in m.group(1),
                    "is_static": "static" in m.group(1),
                }
                if current_class:
                    current_class["methods"].append(fn_entry)
                else:
                    result["free_functions"].append(fn_entry)
            pending_comment.clear()
            continue

        # Bos satir pending yorumu temizler
        if line.strip() == "" and brace_depth <= 1:
            if pending_comment:
                result["raw_comments"].append(" ".join(pending_comment))
            pending_comment.clear()

    return result


def run(source_dir: str = None, output_file: str = None):
    src = source_dir or DEFAULT_SOURCE_DIR
    out = output_file or OUTPUT_FILE

    print(f"[Extractor] Kaynak dizin: {src}")
    files = collect_files(src)
    print(f"[Extractor] {len(files)} dosya bulundu.")

    all_data = []
    for fp in files:
        rel = fp.relative_to(src) if fp.is_relative_to(Path(src)) else fp
        print(f"  İşleniyor: {rel}")
        data = extract_file(fp)
        all_data.append(data)

    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    total_classes = sum(len(d.get("classes", [])) for d in all_data)
    total_fns     = sum(len(d.get("free_functions", [])) for d in all_data)
    total_enums   = sum(len(d.get("enums", [])) for d in all_data)
    print(f"\n[Extractor] Tamamlandi!")
    print(f"  Siniflar   : {total_classes}")
    print(f"  Fonksiyonlar: {total_fns}")
    print(f"  Enum'lar   : {total_enums}")
    print(f"  Cikti      : {out}")
    return all_data


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else None
    run(source_dir=src)
