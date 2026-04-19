# 🏷️ Dinamik Fiyatlandırma ve Fiyat Optimizasyon Sistemi

## 📌 Proje Özeti
Brezilya e-ticaret platformu Olist'in gerçek satış verilerini kullanarak **optimum ürün fiyatını tahmin eden ve öneren** uçtan uca bir makine öğrenmesi sistemi.

🔗 **[Canlı Demo](https://dynamic-pricing-rxkf3r54bvp9bdwgtinryf.streamlit.app)**

## 🎯 Problem
E-ticaret platformlarında satıcılar fiyatlarını genellikle sezgisel olarak belirler. Bu proje şu soruları yanıtlar:
> - *Rakip fiyatları ve ürün özellikleri göz önüne alındığında optimum fiyat nedir?*
> - *Fiyatı artırırsam ne kadar müşteri kaybederim?*
> - *Model neden bu fiyatı öneriyor?*

## 🚀 Özellikler
- ✅ **Fiyat Tahmini** — LightGBM ile R²=0.97 başarısı
- ✅ **Fiyat Elastikiyeti** — Kategori bazında fiyat-talep ilişkisi
- ✅ **Optimizasyon Motoru** — Kar maksimizasyonu için optimum fiyat önerisi
- ✅ **SHAP Analizi** — Model kararlarının açıklanabilirliği
- ✅ **Canlı Dashboard** — Streamlit ile interaktif web uygulaması

## 📊 Veri Seti
- **Kaynak:** [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)
- **Boyut:** 105.509 satır, 51 özellik
- **Kapsam:** Ocak 2017 - Ağustos 2018
- **İçerik:** 9 tablo — siparişler, ürünler, müşteriler, satıcılar, yorumlar

## 🔧 Kullanılan Teknolojiler
| Kategori | Araçlar |
|---|---|
| Dil | Python 3.13 |
| Veri İşleme | Pandas, NumPy |
| Görselleştirme | Matplotlib, Seaborn |
| Model | LightGBM |
| Açıklanabilirlik | SHAP |
| Arayüz | Streamlit |
| Versiyon Kontrol | Git, GitHub |

## 📁 Proje Yapısı
dynamic-pricing/
├── data/
│   └── processed/        ← Temizlenmiş ve özellik mühendisliği yapılmış veri
├── notebooks/
│   ├── 01_EDA.ipynb                  ← Keşifsel veri analizi
│   ├── 02_preprocessing.ipynb        ← Veri ön işleme
│   ├── 03_feature_engineering.ipynb  ← Özellik mühendisliği
│   ├── 04_modeling.ipynb             ← Model geliştirme ve fiyat optimizasyonu
│   └── 05_shap_analysis.ipynb        ← Model açıklanabilirliği
├── outputs/
│   ├── figures/          ← Grafikler
│   └── lgbm_model.pkl    ← Eğitilmiş model
├── app.py                ← Streamlit uygulaması
└── requirements.txt

## 🔬 Metodoloji

### Veri Ön İşleme
- 9 farklı tablo birleştirildi
- Kategori bazlı IQR yöntemiyle aykırı değerler temizlendi
- Zaman serisi için uygun eksik veri doldurma

### Özellik Mühendisliği (22 yeni özellik)
- **Zaman bazlı:** `is_weekend`, `is_holiday`, `quarter`, `week_of_year`
- **Fiyat bazlı:** `price_to_category_ratio`, `freight_to_price_ratio`, `price_vs_competitor`
- **Satıcı bazlı:** `seller_experience`, `seller_mean_delay`
- **Trend bazlı:** `rolling_7_orders`, `rolling_14_orders`

### Model
- **Algoritma:** LightGBM (Gradient Boosting)
- **Validasyon:** TimeSeriesSplit — geçmişle train, gelecekle test

### Fiyat Optimizasyonu
- Kategori bazında fiyat elastikiyeti hesaplandı
- Kar maksimizasyonu için optimum fiyat senaryoları üretildi

### SHAP Analizi
- Global özellik önemi görselleştirildi
- Tekil tahminler için açıklama grafiği oluşturuldu

## 📈 Sonuçlar

| Metrik | Değer |
|--------|-------|
| Ortalama MAE | 1.64 BRL |
| Ortalama RMSE | 15.12 BRL |
| Ortalama R² | 0.97 |
| Hata Ortalaması | 0.04 BRL |

## 🖥️ Uygulamayı Çalıştırma

```bash
git clone https://github.com/iremnurefe/dynamic-pricing.git
cd dynamic-pricing
pip install -r requirements.txt
streamlit run app.py
```

## 👩‍💻 Geliştirici
**İremnur Efe**
- GitHub: [iremnurefe](https://github.com/iremnurefe)
