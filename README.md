# Öğrenci Verimlilik ve Memnuniyet Analizi Dashboard

Bu proje, lisans öğrencilerinin günlük çalışma alışkanlıkları ile genel yaşam memnuniyetleri arasındaki korelasyonu incelemek üzere geliştirilmiş bir veri analizi ve görselleştirme platformudur. 

## Proje Kapsamı ve Özellikler
* **Dinamik Veri Filtreleme:** Kullanıcılar; bölüm, günlük çalışma süresi ve memnuniyet düzeyi değişkenlerine göre veri kümesini özelleştirebilirler.
* **İstatistiksel Göstergeler:** Seçilen kriterlere uyan toplam örneklem büyüklüğü, ortalama çalışma süresi ve ortalama memnuniyet puanı anlık olarak hesaplanmaktadır.
* **Veri Görselleştirme:** Bölüm bazlı ortalama çalışma sürelerinin karşılaştırmalı analizi için sütun grafikleri.
                      Örneklem içindeki bölüm dağılımlarının tespiti için pasta grafikleri.
* **Nitel Analiz Girişi:** Analiz edilen bulguların belgelenmesi amacıyla kullanıcıya özel yorum ve not giriş alanları mevcuttur.

# Proje Yayın Süreci ve Teknik Notlar #
* **Veri Hazırlığı:** Ham veriler analiz edilmeden önce Excel üzerinde titizlikle incelenmiştir. Bu aşamada hatalı girişler düzeltilmiş, eksik bilgiler tamamlanmış ve tüm veriler birbirine uyumlu hale getirilmiştir.
* **Dosya Formatı:** Temizlenen veriler, analiz kodlarımızın hatasız çalışabilmesi için en yaygın ve güvenilir format olan CSV (UTF-8) olarak kaydedilmiştir.
* **Web Üzerinde Yayınlama:** Hazırlanan bu çalışma, herkesin erişebilmesi için Streamlit Cloud aracılığıyla internete taşınmıştır. Kodda yapılan her güncelleme anında web sitesine yansıyacak şekilde bir sistem kurulmuştur.
* **Gerekli Araçlar:** Uygulamanın internet ortamında sorunsuz çalışması için ihtiyaç duyduğu tüm kütüphane ve araçlar (requirements.txt), sistem tarafından otomatik olarak algılanıp kurulacak şekilde yapılandırılmıştır.

## Canlı Uygulama Linki
Projeyi tarayıcı üzerinden interaktif olarak denemek için aşağıdaki bağlantıyı kullanabilirsiniz:
* [Öğrenci Verimlilik Analizi Dashboard](https://cmskvjt9crihybu2bkxfug.streamlit.app/)

## Teknik Altyapı ve Kütüphaneler
Proje, Python ekosistemindeki modern veri analizi kütüphaneleri kullanılarak geliştirilmiştir:
* Python: Temel programlama dili.
* Streamlit: Dashboard arayüz tasarımı ve web tabanlı sunum.
* Pandas: Veri manipülasyonu, filtreleme ve tanımlayıcı istatistiksel işlemler.
* Matplotlib: Verilerin görselleştirilmesi ve grafik üretimi.

<img width="525" height="742" alt="image" src="https://github.com/user-attachments/assets/a22a268e-7682-4b58-9a8e-a26485d43b9a" />
<img width="541" height="763" alt="image" src="https://github.com/user-attachments/assets/ff489d1f-c4a4-4e2a-ba5c-b0a5edc2a4b3" />
<img width="513" height="738" alt="image" src="https://github.com/user-attachments/assets/330d0df6-8f64-4960-b2b0-b638b4e83b5c" />
<img width="535" height="759" alt="image" src="https://github.com/user-attachments/assets/bd832430-5616-40ac-a563-5d02f2099398" />

