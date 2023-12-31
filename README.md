# Kriptografi Projesi

Bu proje, güvenli veri şifreleme ve çözme işlemlerini gerçekleştiren bir Python uygulamasını içermektedir. Proje, AES (Advanced Encryption Standard) şifreleme algoritmasını kullanarak metinleri şifrelemek ve çözmek için tasarlanmıştır.

## Kullanım

Proje, basit bir grafik arayüz ile birlikte gelir. Aşağıdaki adımları izleyerek şifreleme ve çözme işlemlerini gerçekleştirebilirsiniz:

1. Anahtar Üretme:
   - "Anahtar Üret" düğmesine tıklayarak rastgele bir şifreleme anahtarı üretebilirsiniz.
   - Anahtar, otomatik olarak anahtar giriş alanına eklenir.

2. Metin Girme:
   - Şifrelemek veya çözmek istediğiniz metni ilgili giriş alanına girin.

3. Şifreleme:
   - Metni şifrelemek için "Şifrele" düğmesine tıklayın.
   - Şifrelenmiş metin, "Şifrelenmiş Metin" giriş alanında görüntülenecektir.

4. Şifre Çözme:
   - Şifreli metni çözmek için "Şifre Çöz" düğmesine tıklayın.
   - Orijinal metin, "Çözülmüş Metin" giriş alanında görüntülenecektir.

5. Performans Ölçümleri:
   - "Performans Ölçümleri" düğmesine tıklayarak şifreleme ve çözme işlemlerinin sürelerini ve bellek kullanımını ölçebilirsiniz.

## Gereksinimler

Bu projenin çalıştırılabilmesi için aşağıdaki gereksinimlerin karşılanmış olması gerekmektedir:
- Python 3.x
- Crypto kütüphanesi (pip install pycryptodome ile yüklenebilir)