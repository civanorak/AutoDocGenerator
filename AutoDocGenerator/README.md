# Gorgon Auto-Doc Generator

> Gorgon C++ oyun kütüphanesi için otomatik dokümantasyon üretici (Stand-alone HTML).

Dört aşamalı pipeline:

| Aşama | Betik | Görev |
|---|---|---|
| 1 | `1_extractor.py` | `.h` / `.cpp` dosyalarını tarar, JSON çıkarır |
| 2 | `2_enhancer.py` | Ollama ile boş açıklamaları zenginleştirir |
| 3 | `3_generator.py` | JSON → Markdown dosyaları oluşturur (`docs/` klasörü) |
| 4 | `build_site.py` | Markdown → Standalone HTML sitesine dönüştürür (`site/` klasörü) |

## Gereksinimler

- Python 3.10+
- [Ollama](https://ollama.com) (Aşama 2 için çalışıyor olmalı)

```bash
# Python bağımlılıklarını yükle
pip install -r requirements.txt
```

*(Not: Bu yeni sistemde Node.js, npm, VitePress veya Electron'a ihtiyaç yoktur. Çıktı tamamen saf HTML/CSS/JS içerir.)*

## Kullanım

### Tek seferde çalıştır (önerilen)

```bash
cd AutoDocGenerator
python run_all.py "C:/Users/.../Gorgon-main/Source/Gorgon" llama3
```

Kendi başına çalıştırdığında `site/` isimli bir klasör oluşturulacak. Bu klasörün içindeki `index.html` dosyasını herhangi bir web tarayıcısıyla açarak dökümantasyona ulaşabilirsin.

### Adım adım çalıştır

```bash
# 1. C++ dosyaları tara
python 1_extractor.py

# 2. Ollama ile zenginleştir
python 2_enhancer.py

# 3. Markdown üret
python 3_generator.py

# 4. HTML Sitesini Üret
python build_site.py
```

## Çıktı Yapısı & Yayınlama (Hosting)

Sistem `site/` klasörü içerisine tamamen kendi kendine yeten (stand-alone) bir yapı inşa eder:

```
site/
├── index.html              ← Ana sayfa (Tüm modüllerin grid görünümü)
├── getting-started.html    ← Başlangıç rehberi
├── css/
│   └── style.css           ← Tamamen karanlık mod (dark theme) CSS tasarımı
├── js/
│   ├── app.js              ← Animasyonlar, sidebar etkileşimi
│   └── search.js           ← İstemci taraflı arama filtresi motoru
└── modules/
    ├── Animation.html      ← Her bir C++ modülü için üretilmiş detay sayfası
    ├── Audio.html
    └── ...
```

Oluşan `site/` klasörünü bir `.zip` dosyası yapıp başkalarına gönderebilir ya da içerisindeki dosyaları doğrudan **Vercel**, **Netlify** veya **GitHub Pages**'a yükleyerek hiçbir ayar yapmadan internette canlı yayına alabilirsin.
