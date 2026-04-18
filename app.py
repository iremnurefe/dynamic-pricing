import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

# Sayfa ayarları
st.set_page_config(
    page_title="Dinamik Fiyatlandırma Sistemi",
    page_icon="🏷️",
    layout="wide"
)

# Veri ve model yükle
@st.cache_data
def load_data():
    import os
    base_path = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(os.path.join(base_path, 'data/processed/app_data.csv'))
    elasticity = pd.read_csv(os.path.join(base_path, 'data/processed/price_elasticity.csv'))
    return df, elasticity

df, elasticity_df = load_data()

# Optimizasyon fonksiyonu
def optimize_price(category, current_price, cost, target_margin=0.20):
    cat_elasticity = elasticity_df[elasticity_df['category'] == category]['elasticity'].values
    elasticity = cat_elasticity[0] if len(cat_elasticity) > 0 else -0.5
    
    cat_data = df[df['product_category_name_english'] == category]
    competitor_avg = cat_data['competitor_avg_price'].median()
    category_avg = cat_data['price'].median()
    min_price = cost * (1 + target_margin)
    
    scenarios = []
    for price_factor in [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]:
        test_price = current_price * price_factor
        if test_price < min_price:
            continue
        price_change = (test_price - current_price) / current_price
        demand_change = elasticity * price_change
        expected_demand = max(100 * (1 + demand_change), 0)
        revenue = test_price * expected_demand
        profit = (test_price - cost) * expected_demand
        margin = (test_price - cost) / test_price * 100
        scenarios.append({
            'price': round(test_price, 2),
            'price_change_%': round(price_change * 100, 1),
            'expected_demand': round(expected_demand, 1),
            'revenue': round(revenue, 2),
            'profit': round(profit, 2),
            'margin_%': round(margin, 1)
        })
    
    scenarios_df = pd.DataFrame(scenarios)
    optimal_idx = scenarios_df['profit'].idxmax()
    optimal_price = scenarios_df.loc[optimal_idx, 'price']
    return optimal_price, scenarios_df, elasticity, competitor_avg, category_avg

# Arayüz
st.title("🏷️ Dinamik Fiyatlandırma Sistemi")
st.markdown("Olist e-ticaret verisiyle eğitilmiş fiyat optimizasyon motoru")
st.divider()

# Sol panel — giriş
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("⚙️ Ürün Bilgileri")
    
    categories = sorted(df['product_category_name_english'].unique())
    category = st.selectbox("Kategori", categories, index=categories.index('health_beauty'))
    current_price = st.number_input("Mevcut Fiyat (BRL)", min_value=1.0, max_value=5000.0, value=79.90, step=0.10)
    cost = st.number_input("Maliyet (BRL)", min_value=1.0, max_value=5000.0, value=45.00, step=0.10)
    target_margin = st.slider("Minimum Kar Marjı (%)", min_value=5, max_value=50, value=20) / 100
    
    if cost >= current_price:
        st.error("⚠️ Maliyet fiyattan yüksek olamaz!")
    else:
        analyze = st.button("🔍 Fiyat Optimize Et", use_container_width=True)

# Sağ panel — sonuçlar
with col2:
    if cost < current_price and 'analyze' in locals() and analyze:
        optimal_price, scenarios, elasticity, comp_avg, cat_avg = optimize_price(
            category, current_price, cost, target_margin
        )
        
        # Metrikler
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Mevcut Fiyat", f"{current_price:.2f} BRL")
        m2.metric("Önerilen Fiyat", f"{optimal_price:.2f} BRL", 
                  f"{((optimal_price-current_price)/current_price*100):.1f}%")
        m3.metric("Rakip Ortalama", f"{comp_avg:.2f} BRL")
        m4.metric("Elastikiyet", f"{elasticity:.3f}")
        
        st.divider()
        
        # Senaryo grafiği
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        
        colors = ['green' if p == optimal_price else 'steelblue' for p in scenarios['price']]
        axes[0].bar(scenarios['price'].astype(str), scenarios['profit'], color=colors)
        axes[0].set_title('Fiyat vs Kar')
        axes[0].set_xlabel('Fiyat (BRL)')
        axes[0].set_ylabel('Kar (BRL)')
        axes[0].tick_params(axis='x', rotation=45)
        
        axes[1].plot(scenarios['price'], scenarios['expected_demand'], 
                    marker='o', color='coral', linewidth=2)
        axes[1].set_title('Fiyat vs Talep')
        axes[1].set_xlabel('Fiyat (BRL)')
        axes[1].set_ylabel('Beklenen Talep')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        # Senaryo tablosu
        st.subheader("📊 Senaryo Analizi")
        st.dataframe(scenarios, use_container_width=True)