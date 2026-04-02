import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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

# Identifikasi missing values
print("Missing values per column:\n", df.isnull().sum())

# Visualisasi missing values
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.show()

# Penanganan missing values
# Mean imputation untuk kolom quantity
df['quantity'] = df['quantity'].fillna(df['quantity'].mean())

# Litwise deletion untuk baris dengan banyak missing values (dalam kasus ini kita anggap ada lebih dari 1 missing value sebagai banyak)
df.dropna(thresh=len(df.columns) - 1, inplace=True)

df['price'] = df['price'].fillna(df['price'].median())

# Deteksi dan penghapusan outliers
mean_price = df['price'].mean()
std_price = df['price'].std()
df['z_score'] = (df['price'] - mean_price) / std_price

threshold = 3
df = df[np.abs(df['z_score']) < threshold].copy()
df.drop(columns=['z_score'], inplace=True)

# Standarisasi format tanggal
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)

# Pengabungan kategori produk
df['product'] = df['product'].str.upper()

df = df.drop_duplicates() # hapus duplikasi

print("Data setelah pembersihan:\n", df)