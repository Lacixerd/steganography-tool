# Steganografi Projesi

Bu proje, görüntü dosyaları içerisine gizli mesajlar yerleştirmenize ve bu mesajları okumanıza olanak sağlayan bir steganografi uygulamasıdır.

## 🚀 Özellikler

- Gri tonlamalı görüntülere metin mesajları gizleme
- Gizlenmiş mesajları görüntülerden okuma
- Kullanıcı dostu komut satırı arayüzü

## 📋 Gereksinimler

- Python 3.x
- OpenCV (cv2)
- NumPy

## 🛠️ Kurulum

1. Projeyi klonlayın:
```
git clone https://github.com/Clrrus/steganography-tool.git
cd steganography-tool
```

2. Gerekli kütüphaneleri yükleyin:
```
pip install -r requirements.txt
```

## 💻 Kullanım

Programı çalıştırmak için:

```
python src/main.py
```

Program size iki seçenek sunacaktır:
1. Bir fotoğrafa mesaj gizlemek
2. Gizlenmiş mesajı okumak

### Mesaj Gizleme
- '1' seçeneğini seçin
- Gizlemek istediğiniz mesajı girin
- Kaynak görüntü dosyasının yolunu girin
- Çıktı görüntüsünün kaydedileceği yolu girin

### Gizli Mesajı Okuma
- '2' seçeneğini seçin
- Gizli mesaj içeren görüntü dosyasının yolunu girin

## 🔍 Teknik Detaylar

Bu uygulama, LSB (Least Significant Bit) steganografi tekniğini kullanır. Her piksel değerinin en az önemli bitini değiştirerek mesajı görüntüye gizler. Bu sayede görüntüde gözle görülür bir değişiklik olmadan mesajlar saklanabilir.

## ⚠️ Sınırlamalar

- Şu an için sadece elde edilen fotoğraflar, gri tonlamalı görüntüler olarak çıkar. Renkli fotoğraf çıkışı desteklenmemektedir
- Mesaj uzunluğu, görüntü boyutuyla sınırlıdır
- Görüntü formatı değiştirildiğinde gizli mesaj kaybolabilir

## 👥 Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Dalınıza push yapın (`git push origin yeni-ozellik`)
5. Bir Pull Request oluşturun
