import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

data = {
    'Tanggal': ['2024-01-01', '2024-01-08', '2024-01-15'],
    'Jumlah produk terjual': [120, 150, 130],
    'Harga satuan': [10, 15, 20],
    'Kategori produk': ['A', 'B', 'A'],
    'Lokasi cabang': ['Jakarta', 'Bandung', 'Surabaya'],
    'Populasi daerah': [1000000, 2000000, 1500000],
    'Penghasilan rata-rata daerah': [5000000, 6000000, 5500000]
}

df = pd.DataFrame(data)

# Ekstraksi fitur dari tanggal
df['Tanggal'] = pd.to_datetime(df['Tanggal'])
df['Hari'] = df['Tanggal'].dt.dayofweek
df['Bulan'] = df['Tanggal'].dt.month
df['Kuartal'] = df['Tanggal'].dt.quarter
df['Tahun'] = df['Tanggal'].dt.year

# Pembuatan variable baru
df['Total penjualan'] = df['Jumlah produk terjual'] * df['Harga satuan']

# Contoh pembuatan fitur ekstraksi
df['Potensi pasar'] = df['Populasi daerah'] * df['Penghasilan rata-rata daerah']

# Normalisasi fitur
scaler = MinMaxScaler()
df[['Jumlah produk terjual', 'Total penjualan']] = scaler.fit_transform(df[['Jumlah produk terjual', 'Total penjualan']])

# Menggunakan PCA untuk mengurangi dimensi
pca = PCA(n_components=5)
df_pca = pca.fit_transform(df.drop(columns=['Tanggal']))

# Model untuk seleksi fitur
model = LinearRegression()

# Recursive Feature Elimination (RFE)
rfe = RFE(model, n_features_to_select=5)
X_rfe = rfe.fit_transform(df_pca, df['Total penjualan'])

# Fitur yang dipilih
selected_features = rfe.support_

print(df)