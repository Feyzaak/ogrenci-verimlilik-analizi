# Öğrenci Verimlilik ve Memnuniyet Analizi Dashboard

Bu proje, lisans öğrencilerinin günlük çalışma alışkanlıkları ile genel yaşam memnuniyetleri arasındaki korelasyonu incelemek üzere geliştirilmiş bir veri analizi ve görselleştirme platformudur. 

## Proje Kapsamı ve Özellikler
* **Dinamik Veri Filtreleme:** Kullanıcılar; bölüm, günlük çalışma süresi ve memnuniyet düzeyi değişkenlerine göre veri kümesini özelleştirebilirler.
* **İstatistiksel Göstergeler:** Seçilen kriterlere uyan toplam örneklem büyüklüğü, ortalama çalışma süresi ve ortalama memnuniyet puanı anlık olarak hesaplanmaktadır.
* **Veri Görselleştirme:** Bölüm bazlı ortalama çalışma sürelerinin karşılaştırmalı analizi için sütun grafikleri.
                      Örneklem içindeki bölüm dağılımlarının tespiti için pasta grafikleri.
* **Nitel Analiz Girişi:** Analiz edilen bulguların belgelenmesi amacıyla kullanıcıya özel yorum ve not giriş alanları mevcuttur.

# Proje Yayın Süreci ve Teknik Notlar #
* **Veri Hazırlama Süreci:** 
*Veri Temizliği:* Ham veri seti, analiz öncesinde Excel kullanılarak yapısal hatalardan arındırılmış, eksik veriler tamamlanmış ve veri tutarlılığı sağlanarak işleme hazır hale getirilmiştir.
*Format Dönüşümü:* Temizlenen veriler, Python/Pandas ekosistemiyle tam uyumlu çalışması amacıyla UTF-8 kodlamasına sahip CSV formatına dönüştürülmüştür.
* **Canlı Yayın (Deployment):** Uygulama, sürekli entegrasyon (CI/CD) prensipleri doğrultusunda **Streamlit Cloud** platformu üzerinde yayına alınmıştır. GitHub üzerindeki ana dal (main branch) ile senkronize çalışmaktadır.
* **Bağımlılık Yönetimi:** Sunucu tarafındaki kütüphane gereksinimleri `requirements.txt` dosyası aracılığıyla otomatik olarak yapılandırılmıştır.

## Canlı Uygulama Linki
Projeyi tarayıcı üzerinden interaktif olarak denemek için aşağıdaki bağlantıyı kullanabilirsiniz:
* [Öğrenci Verimlilik Analizi Dashboard](https://cmskvjt9crihybu2bkxfug.streamlit.app/)

## Teknik Altyapı ve Kütüphaneler
Proje, Python ekosistemindeki modern veri analizi kütüphaneleri kullanılarak geliştirilmiştir:
* Python: Temel programlama dili.
* Streamlit: Dashboard arayüz tasarımı ve web tabanlı sunum.
* Pandas: Veri manipülasyonu, filtreleme ve tanımlayıcı istatistiksel işlemler.
* Matplotlib: Verilerin görselleştirilmesi ve grafik üretimi.
