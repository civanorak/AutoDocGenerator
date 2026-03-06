# Gorgon Game Engine & Auto-Doc Generator

Bu depo, **Gorgon C++ Oyun Kütüphanesi** ve bu kütüphane için geliştirilmiş olan **AutoDocGenerator** aracını içermektedir.

## Proje Yapısı

- `AutoDocGenerator/`: C++ kodlarından otomatik olarak tamamen offline çalışabilen, kendi başına yeten (standalone) HTML dokümantasyon siteleri üreten Python tabanlı araç.
- `AutoDocGenerator/site/`: Üretilen saf HTML/CSS/JS tabanlı dokümantasyon projesi çıktısı.

## AutoDocGenerator Kullanımı

Bu araç, C++ header (`.h`) ve kaynak (`.cpp`) dosyalarınızı tarayarak:
1. Sınıf, fonksiyon ve enum yapılarını yakalar.
2. **Ollama (AI)** kullanarak eksik döküman yorumlarını tamamlar.
3. Node.js veya sunucu gerektirmeyen, doğrudan tarayıcı ile açılabilen **modern, responsive bir stand-alone HTML site** oluşturur.

Detaylı kullanım talimatları için [AutoDocGenerator/README.md](./AutoDocGenerator/README.md) dosyasını inceleyebilirsiniz.

## Lisans
ISC
