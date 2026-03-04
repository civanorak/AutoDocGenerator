# Gorgon Game Engine & Auto-Doc Generator

Bu depo, **Gorgon C++ Oyun Kütüphanesi** ve bu kütüphane için geliştirilmiş olan **AutoDocGenerator** aracını içermektedir.

## Proje Yapısı

- `AutoDocGenerator/`: C++ kodlarından otomatik olarak dokümantasyon üreten Python tabanlı araç.
- `AutoDocGenerator/docs/`: Üretilen dokümantasyonun VitePress ile sunulan web sitesi içeriği.

## AutoDocGenerator Kullanımı

Bu araç, C++ header (`.h`) ve kaynak (`.cpp`) dosyalarınızı tarayarak:
1. Sınıf, fonksiyon ve enum yapılarını yakalar.
2. **Ollama (AI)** kullanarak eksik döküman yorumlarını tamamlar.
3. Modern bir **VitePress** sitesi oluşturur.

Detaylı kullanım talimatları için [AutoDocGenerator/README.md](./AutoDocGenerator/README.md) dosyasını inceleyebilirsiniz.

## Lisans
ISC
