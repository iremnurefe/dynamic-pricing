# 🏷️ Kişiselleştirilmiş Dinamik Fiyatlandırma ve Talep Tahmini

## 📌 Proje Özeti
Bu proje, Brezilya e-ticaret platformu Olist'in gerçek satış verilerini kullanarak **optimum ürün fiyatını tahmin eden** bir makine öğrenmesi sistemi geliştirmeyi amaçlamaktadır.

## 🎯 Problem
E-ticaret platformlarında satıcılar fiyatlarını genellikle sezgisel olarak belirler. Bu proje şu soruyu yanıtlar:
> *"Rakip fiyatları, ürün özellikleri ve geçmiş satış trendleri göz önüne alındığında, bir ürün için optimum fiyat nedir?"*

## 📊 Veri Seti
- **Kaynak:** [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)
- **Boyut:** 105.509 satır, 51 özellik
- **Kapsam:** Ocak 2017 - Ağustos 2018

## 🔧 Kullanılan Teknolojiler
- **Python:** pandas, numpy, matplotlib, seaborn
- **Model:** LightGBM
- **Validasyon:** TimeSeriesSplit (5-fold)

## 📁 Proje Yapısı
dynamic-pricing/
├── data/
│   └── processed/        ← Temizlenmiş ve özellik mühendisliği yapılmış veri
├── notebooks/
│   ├── 01_EDA.ipynb              ← Keşifsel veri analizi
│   ├── 02_preprocessing.ipynb   ← Veri ön işleme
│   ├── 03_feature_engineering.ipynb  ← Özellik mühendisliği
│   └── 04_modeling.ipynb        ← Model geliştirme
├── outputs/
│   ├── figures/          ← Grafikler
│   └── lgbm_model.pkl    ← Eğitilmiş model
└── requirements.txt

## 🚀 Öne Çıkan Adımlar

### 1. Veri Ön İşleme
- 9 farklı tablo birleştirildi
- Kategori bazlı IQR yöntemiyle aykırı değerler temizlendi
- Zaman serisi için uygun eksik veri doldurma

### 2. Özellik Mühendisliği (22 yeni özellik)
- **Zaman bazlı:** `is_weekend`, `is_holiday`, `quarter`, `week_of_year`
- **Fiyat bazlı:** `price_to_category_ratio`, `freight_to_price_ratio`, `price_vs_competitor`
- **Satıcı bazlı:** `seller_experience`, `seller_mean_delay`
- **Trend bazlı:** `rolling_7_orders`, `rolling_14_orders`

### 3. Model
- **Algoritma:** LightGBM (Gradient Boosting)
- **Validasyon:** TimeSeriesSplit — geçmişle train, gelecekle test

## 📈 Sonuçlar

| Metrik | Değer |
|--------|-------|
| Ortalama MAE | 1.64 BRL |
| Ortalama RMSE | 15.12 BRL |
| Ortalama R² | 0.97 |

## ⚙️ Kurulum

```bash
git clone https://github.com/iremnurefe/dynamic-pricing.git
cd dynamic-pricing
pip install -r requirements.txt
```

## 👩‍💻 Geliştirici
**İremnur Efe**