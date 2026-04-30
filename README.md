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

<img width="1240" height="1754" alt="1" src="https://github.com/user-attachments/assets/54be272a-5674-4fbb-a5a1-e5c98b32a3d9" />
<img width="1240" height="1754" alt="2" src="https://github.com/user-attachments/assets/199e8448-a020-4070-8256-5003580439e4" />
<img width="1240" height="1754" alt="3" src="https://github.com/user-attachments/assets/d9a8fa15-ac60-4342-b0da-811445a92d59" />
<img width="1240" height="1754" alt="4" src="https://github.com/user-attachments/assets/0c16e46d-62d1-422f-82bd-0f28e38bca9c" />


