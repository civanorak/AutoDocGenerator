# Gorgon Auto-Doc Generator

> Gorgon C++ oyun kütüphanesi için otomatik dokümantasyon üretici.

Üç aşamalı pipeline:

| Aşama | Betik | Görev |
|---|---|---|
| 1 | `1_extractor.py` | `.h` / `.cpp` dosyalarını tarar, JSON çıkarır |
| 2 | `2_enhancer.py` | Ollama ile boş açıklamaları zenginleştirir |
| 3 | `3_generator.py` | JSON → VitePress uyumlu Markdown dosyaları |

## Gereksinimler

- Python 3.10+
- [Ollama](https://ollama.com) (çalışıyor olmalı)
- Node.js (VitePress için)

```bash
# Python bağımlılıkları
pip install -r requirements.txt

# VitePress
npm install -g vitepress
```

## Kullanım

### Tek seferde çalıştır (önerilen)

```bash
cd AutoDocGenerator
python run_all.py "C:/Users/.../Gorgon-main/Source/Gorgon" llama3
```

### Adım adım çalıştır

```bash
# 1. C++ dosyaları tara
python 1_extractor.py

# 2. Ollama ile zenginleştir
python 2_enhancer.py

# 3. Markdown üret
python 3_generator.py
```

## Yerel Önizleme

```bash
cd docs
vitepress dev
# → http://localhost:5173 adresine git
```

## GitHub Pages ile Yayınlama

```bash
# 1. Siteyi derle
cd docs
vitepress build

# 2. GitHub reposuna yükle
git init
git add .
git commit -m "docs: initial release"
git push origin main

# 3. GitHub → Settings → Pages → Source: /docs klasörünü seç
# → https://kullaniciadi.github.io/gorgon-docs/ adresinde yayına girer!
```

## Çıktı Yapısı

```
docs/
├── index.md         ← Ana sayfa
├── Graphics/
│   └── index.md
├── Audio/
│   └── index.md
├── ... (her modül için)
└── .vitepress/
    └── config.mjs   ← VitePress yapılandırması
```
