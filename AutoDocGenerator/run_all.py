"""
run_all.py  —  Gorgon Auto-Doc Generator
==========================================
Bu script tüm 3 aşamayı sırayla çalıştırır:
  1. Extractor  → extracted_data.json
  2. Enhancer   → enhanced_data.json   (Ollama kullanır)
  3. Generator  → docs/  (VitePress uyumlu .md dosyaları)

Kullanım:
  python run_all.py [kaynak_dizin]  [ollama_model]

Örnek:
  python run_all.py "C:/Downloads/Gorgon-main/Source/Gorgon" llama3
"""

import sys
import time

# ─── Argümanlar ───────────────────────────────────────────────────────────────
SOURCE_DIR   = sys.argv[1] if len(sys.argv) > 1 else None
OLLAMA_MODEL = sys.argv[2] if len(sys.argv) > 2 else "llama3"

print("=" * 60)
print("  Gorgon Auto-Doc Generator")
print("=" * 60)

# ─── AŞAMA 1: Extract ─────────────────────────────────────────────────────────
print("\n[Aşama 1/3]  Extractor baslatiliyor...\n")
t0 = time.time()
import importlib, sys as _sys
import extractor as ext_mod
ext_mod = importlib.import_module("1_extractor".replace("-","_")) if "1_extractor" not in sys.modules else sys.modules["1_extractor"]

# Python modül adı - ile başlayamaz, doğrudan import edeceğiz
import importlib.util, os

def load_script(path: str):
    spec = importlib.util.spec_from_file_location("_mod", path)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

base = os.path.dirname(os.path.abspath(__file__))

extractor = load_script(os.path.join(base, "1_extractor.py"))
extractor.run(source_dir=SOURCE_DIR)
print(f"  → Süre: {time.time()-t0:.1f}s\n")

# ─── AŞAMA 2: Enhance ─────────────────────────────────────────────────────────
print("[Aşama 2/3]  Enhancer baslatiliyor (Ollama)...\n")
t1 = time.time()
enhancer = load_script(os.path.join(base, "2_enhancer.py"))
enhancer.run(model=OLLAMA_MODEL)
print(f"  → Süre: {time.time()-t1:.1f}s\n")

# ─── AŞAMA 3: Generate ────────────────────────────────────────────────────────
print("[Aşama 3/3]  Generator baslatiliyor...\n")
t2 = time.time()
generator = load_script(os.path.join(base, "3_generator.py"))
docs_dir = generator.run()
print(f"  → Süre: {time.time()-t2:.1f}s\n")

total = time.time() - t0
print("=" * 60)
print(f"  TAM! Toplam süre: {total:.1f}s")
print(f"  Dokümantasyon: {docs_dir}")
print("")
print("  Sıradaki adımlar:")
print("  1. npm install -g vitepress")
print(f"  2. cd {docs_dir}")
print("  3. vitepress dev   ← yerel önizleme")
print("  4. vitepress build ← GitHub Pages için derleme")
print("=" * 60)
