import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
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

# Encode categorical columns
le_kategori = LabelEncoder()
le_lokasi = LabelEncoder()
df['Kategori produk'] = le_kategori.fit_transform(df['Kategori produk'])
df['Lokasi cabang'] = le_lokasi.fit_transform(df['Lokasi cabang'])

# Menggunakan PCA untuk mengurangi dimensi
# Select only numeric columns (excluding Tanggal which is datetime)
numeric_cols = df.select_dtypes(include=['number']).columns
df_numeric = df[numeric_cols]
# n_components must be min(n_samples, n_features)
n_pca_components = min(5, df_numeric.shape[0], df_numeric.shape[1])
pca = PCA(n_components=n_pca_components)
df_pca = pca.fit_transform(df_numeric)

# Model untuk seleksi fitur
model = LinearRegression()

# Recursive Feature Elimination (RFE)
# n_features_to_select must be less than or equal to n_features
n_rfe_features = min(5, df_pca.shape[1])
rfe = RFE(model, n_features_to_select=n_rfe_features)
X_rfe = rfe.fit_transform(df_pca, df['Total penjualan'])

# Fitur yang dipilih
selected_features = rfe.support_

print(df)