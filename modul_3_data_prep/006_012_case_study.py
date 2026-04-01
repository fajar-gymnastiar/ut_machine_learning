import pandas as pd
import numpy as np
from io import StringIO

data = """id,date,product,price,quantity
1,2021/01/01,Product A,100,10
2,01-02-2021,product a,150,20
3,2021.03.03,Product B,200,30
4,04/04/2021,product b,250,40
5,2021/05/05,Product A,,50
6,06-06-2021,Product A,350,
7,2021.07.07,Product B,400,70
8,08/08/2021,product b,450,80
9,2021/09/09,Product A,500,90
10,10-10-2021,Product A,1000,100
11,2021.11.11,product b,1100,110
12,12/12/2021,Product B,1200,120
"""

df = pd.read_csv(StringIO(data))

# --- BAGIAN 1: Menampilkan Missing Values ---
print("Missing values per kolom (Sebelum dibersihkan):")
print(df.isnull().sum())
print("-" * 30)

# --- BAGIAN 2: Perbaikan Tanggal (Solusi NaN) ---
# Mengubah ke format string standar YYYY-MM-DD
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

# --- BAGIAN 3: Penanganan Missing Values & Outliers ---
# Isi quantity dengan mean
df['quantity'] = df['quantity'].fillna(df['quantity'].mean())

# Isi price dengan median agar perhitungan Z-score tidak menghasilkan NaN
df['price'] = df['price'].fillna(df['price'].median())

# Deteksi Outlier
mean_price = df['price'].mean()
std_price = df['price'].std()
df['z_score'] = (df['price'] - mean_price) / std_price

# Hapus outlier (threshold 3)
df = df[np.abs(df['z_score']) < 3].copy()
df.drop(columns=['z_score'], inplace=True)

# Standarisasi Produk & Duplikat
df['product'] = df['product'].str.upper()
df = df.drop_duplicates()

print("Data setelah pembersihan:")
print(df)