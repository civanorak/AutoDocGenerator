"""
Gorgon AI Enhancer  (Ollama)
-----------------------------
Extractor'dan gelen JSON'u alir; bos ya da kisa aciklamasi olan
sinif ve fonksiyonlara Ollama araciligiyla zengin aciklama + ornek kod ekler.
"""

import json
import sys
import re
import requests
from pathlib import Path

# ─── Ayarlar ──────────────────────────────────────────────────────────────────
INPUT_FILE  = "extracted_data.json"
OUTPUT_FILE = "enhanced_data.json"

OLLAMA_URL   = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3"          # Sistemindeki model adini buraya yaz

# Aciklamasi bu uzunluktan kisaysa AI'ya sor
MIN_DESCRIPTION_LEN = 15

# Rate-limit: saniyede kac istek
DELAY_SECONDS = 0.3

import time


# ─── Ollama Yardımcısı ─────────────────────────────────────────────────────────
def ask_ollama(prompt: str, model: str = OLLAMA_MODEL) -> str:
    """Ollama'ya bir prompt gonderip yanit dondurur."""
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "num_predict": 300,
        }
    }
    try:
        r = requests.post(OLLAMA_URL, json=payload, timeout=60)
        r.raise_for_status()
        return r.json().get("response", "").strip()
    except Exception as e:
        return f"[Ollama Hatasi: {e}]"


def enhance_description(kind: str, name: str, existing: str, context: str = "") -> str:
    """Verilen C++ ogesi icin Ingilizce aciklama uretir (kisaca)."""
    prompt = (
        f"You are documenting a C++ game library called 'Gorgon'.\n"
        f"Write a concise English description (2-3 sentences max) for the following {kind}.\n"
        f"Name: {name}\n"
        f"Existing comment (may be empty): \"{existing}\"\n"
        f"{('Context: ' + context) if context else ''}\n"
        f"Reply with ONLY the description, no extra text."
    )
    return ask_ollama(prompt)


def enhance_function_example(name: str, return_type: str, params: list, desc: str) -> str:
    """Bir C++ fonksiyonu icin kisa kullanim ornegi uretir."""
    params_str = ", ".join(params) if params else "void"
    prompt = (
        f"You are documenting a C++ game library called 'Gorgon'.\n"
        f"Write a short C++ usage example (3-5 lines) for:\n"
        f"  {return_type} {name}({params_str})\n"
        f"Description: {desc}\n"
        f"Reply with ONLY valid C++ code inside a code block."
    )
    raw = ask_ollama(prompt)
    # Sadece kod blogu icerigini cikar
    m = re.search(r'```(?:cpp|c\+\+)?\n(.*?)```', raw, re.DOTALL)
    return m.group(1).strip() if m else raw.strip()


# ─── Ana Akis ─────────────────────────────────────────────────────────────────
def run(input_file: str = None, output_file: str = None, model: str = None):
    global OLLAMA_MODEL
    if model:
        OLLAMA_MODEL = model

    inp = input_file or INPUT_FILE
    out = output_file or OUTPUT_FILE

    print(f"[Enhancer] Girdi: {inp}")
    with open(inp, 'r', encoding='utf-8') as f:
        all_data = json.load(f)

    # Ollama baglantisini test et
    print("[Enhancer] Ollama baglantisi test ediliyor...")
    test = ask_ollama("Say 'OK' in one word.")
    if "Ollama Hatasi" in test:
        print(f"  UYARI: Ollama'ya ulasilamiyor — {test}")
        print("  AI zenginlestirmesi atlanacak, ham veriler korunacak.")
    else:
        print(f"  Ollama OK -> {test[:40]}")

    enhanced_count = 0

    for file_data in all_data:
        module = file_data.get("module", "unknown")

        # ── Sınıflar ──────────────────────────────────────────
        for cls in file_data.get("classes", []):
            if len(cls.get("description", "")) < MIN_DESCRIPTION_LEN:
                print(f"  [AI] Sinif: {module}::{cls['name']}")
                cls["description"] = enhance_description(
                    "class", cls["name"], cls.get("description", ""),
                    context=f"Module: {module}"
                )
                enhanced_count += 1
                time.sleep(DELAY_SECONDS)

            # Sinif metodlari
            for method in cls.get("methods", []):
                if len(method.get("description", "")) < MIN_DESCRIPTION_LEN:
                    print(f"    [AI] Metot: {cls['name']}::{method['name']}")
                    method["description"] = enhance_description(
                        "method", method["name"], method.get("description", ""),
                        context=f"Inside class {cls['name']} of module {module}"
                    )
                    # Kisa ornek ekle
                    method["example"] = enhance_function_example(
                        method["name"], method.get("return_type", ""),
                        method.get("params", []), method["description"]
                    )
                    enhanced_count += 1
                    time.sleep(DELAY_SECONDS)

        # ── Serbest Fonksiyonlar ──────────────────────────────
        for fn in file_data.get("free_functions", []):
            if len(fn.get("description", "")) < MIN_DESCRIPTION_LEN:
                print(f"  [AI] Fonksiyon: {module}::{fn['name']}")
                fn["description"] = enhance_description(
                    "function", fn["name"], fn.get("description", ""),
                    context=f"Module: {module}"
                )
                fn["example"] = enhance_function_example(
                    fn["name"], fn.get("return_type", ""),
                    fn.get("params", []), fn["description"]
                )
                enhanced_count += 1
                time.sleep(DELAY_SECONDS)

        # ── Enum'lar ──────────────────────────────────────────
        for enum in file_data.get("enums", []):
            if len(enum.get("description", "")) < MIN_DESCRIPTION_LEN:
                print(f"  [AI] Enum: {module}::{enum['name']}")
                enum["description"] = enhance_description(
                    "enum", enum["name"], enum.get("description", ""),
                    context=f"Module: {module}"
                )
                enhanced_count += 1
                time.sleep(DELAY_SECONDS)

    with open(out, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print(f"\n[Enhancer] Tamamlandi! {enhanced_count} item zenginlestirildi.")
    print(f"  Cikti: {out}")
    return all_data


if __name__ == "__main__":
    model_arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(model=model_arg)
