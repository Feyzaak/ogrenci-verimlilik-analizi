import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/afked/Downloads/25.26guzdonemidersleri/OgrenciYasam.csv", encoding="utf-8-sig")

st.title("ÖĞRENCİ VERİMLİLİK ANALİZİ")
st.write("Bu dashboard farklı bölümlerdeki öğrencilerin günlük çalışma saatleri ve memnuniyet düzeyleri arasındaki ilişkiyi incelemek amacıyla hazırlanmıştır.")
st.subheader("Veri Setinin İlk 5 Satırı")
st.dataframe(df.head())


st.sidebar.header("Filtreler")
bolumler = sorted(df["Bolum"].dropna().unique())
secili_bolum = st.sidebar.multiselect("Bölüm Seçin:", bolumler)

saat_etiketleri = ["Az (1-2 Saat)", "Orta (3-4 Saat)", "Çok (5-6 Saat)"]
secili_calisma_saat_araligi = st.sidebar.multiselect("Saat Aralığı Seçin:", saat_etiketleri)

puan_etiketleri = ["Düşük (1-2)", "Orta (3-4)", "Yüksek (5-6)"]
secili_kategori = st.sidebar.multiselect("Memnuniyet Düzeyi Seçin:", puan_etiketleri)

df_filtreli = df.copy()

if secili_bolum:
    df_filtreli = df_filtreli[df_filtreli["Bolum"].isin(secili_bolum)]
 
###Aralıklı vermem gerekiyordu çünkü tek tek seçmek multiselectte çok uzun listeler yaratıyordu ve seçimi zorlaştırıyordu.
if secili_calisma_saat_araligi:

    kosul = pd.Series(False, index=df_filtreli.index)
    
    if "Az (1-2 Saat)" in secili_calisma_saat_araligi:
        kosul |= df_filtreli["Gunluk_Calisma_Saat"].between(1, 2)
    if "Orta (3-4 Saat)" in secili_calisma_saat_araligi:
        kosul |= df_filtreli["Gunluk_Calisma_Saat"].between(3, 4)
    if "Çok (5-6 Saat)" in secili_calisma_saat_araligi:
        kosul |= df_filtreli["Gunluk_Calisma_Saat"].between(5, 6)
    
    df_filtreli = df_filtreli[kosul]

if secili_kategori:
    kosul_puan = pd.Series(False, index=df_filtreli.index)
    
    if "Düşük (1-2)" in secili_kategori:
        kosul_puan |= df_filtreli["Memnuniyet_Puani"].between(1, 2)
    if "Orta (3-4)" in secili_kategori:
        kosul_puan |= df_filtreli["Memnuniyet_Puani"].between(3, 4)
    if "Yüksek (5-6)" in secili_kategori:
        kosul_puan |= df_filtreli["Memnuniyet_Puani"].between(5, 6)
        
    df_filtreli = df_filtreli[kosul_puan]

st.subheader("Filtrelenmiş Veri Özeti")

if df_filtreli.empty:
    st.warning("Bu filtrelerle hiç veri bulunamadı. Lütfen filtreleri değiştirip tekrar deneyiniz.")
else:
    st.write(f"Seçilen kriterlere uyan toplam öğrenci sayısı: **{len(df_filtreli)}**")
    st.dataframe(df_filtreli)

    st.subheader("Özet Göstergeler")
    bolumdeki_ogrenci_sayisi = len(df_filtreli)
    ort_gunluk_calisma_saati = df_filtreli["Gunluk_Calisma_Saat"].mean()
    ort_memnuniyet_puani = df_filtreli["Memnuniyet_Puani"].mean()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Toplam Öğrenci Sayısı", f"{bolumdeki_ogrenci_sayisi}")
    col2.metric("Ortalama Çalışma Saati", f"{ort_gunluk_calisma_saati:.1f}")
    col3.metric("Ortalama Memnuniyet Puanı", f"{ort_memnuniyet_puani:.1f}")

    st.subheader("**Grafikler**")    
    grup_veri = df_filtreli.groupby("Bolum")["Gunluk_Calisma_Saat"].mean()
    fig1, ax1 = plt.subplots()
    bars = ax1.bar(grup_veri.index, grup_veri.values, color="salmon")
    ax1.bar_label(bars, fmt='%.2f')
    ax1.set_xlabel("Bölümler")
    ax1.set_ylabel("Saat")
    ax1.set_title("Bölümlere Göre Ortalama Çalışma Saatleri")
    st.pyplot(fig1)
    
    
    yorum_bar = st.text_area(
        label="Bar Grafiği Yorumunuzu buraya yazın:",
        placeholder="...",
        height=150
    )

    if st.button("Bar Grafiği Yorumunu Gönder"):
        if yorum_bar.strip() == "":
            st.warning("Yorum alanı boş bırakılamaz. Lütfen bir şeyler yazınız")
        else:
            st.success("Yorumunuz başarıyla kaydedildi")
            st.write("Yazdığınız Yorum:")
            st.info(yorum_bar)

    pasta_veri = df_filtreli["Bolum"].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(pasta_veri, 
            labels=pasta_veri.index, 
            autopct='%1.0f%%', 
            colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0']
            )
    ax2.set_title("Bölümlere Göre Öğrenci Dağılımı")
    st.pyplot(fig2)

    
    yorum_pasta = st.text_area(
        label="Pasta Grafiği Yorumunuzu buraya yazın:",
        placeholder="...",
        height=150
    )

    if st.button("Pasta Grafiği Yorumunu Gönder"):
        if yorum_pasta.strip() == "":
            st.warning("Yorum alanı boş bırakılamaz. Lütfen bir şeyler yazınız")
        else:
            st.success("Yorumunuz başarıyla kaydedildi")
            st.write("Yazdığınız Yorum:")
            st.info(yorum_pasta)