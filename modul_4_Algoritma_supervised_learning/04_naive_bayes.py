import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

data = {
    'Usia': [30, 40, 35, 50, 25, 45, 55, 60, 28, 38, 33, 48, 23, 52, 29, 36, 43, 37, 27, 31],
    'Pendapatan': ['Rendah', 'Tinggi', 'Sedang', 'Rendah', 'Tinggi', 'Sedang', 'Tinggi', 'Rendah', 'Sedang', 'Tinggi', 'Rendah', 'Sedang', 'Tinggi', 'Rendah', 'Tinggi', 'Sedang', 'Tinggi', 'Rendah', 'Sedang', 'Tinggi'],
    'Kelayakan': ['T', 'L', 'L', 'T', 'L', 'L', 'T', 'T', 'L', 'L', 'T', 'L', 'T', 'L', 'L', 'T', 'L', 'T', 'L', 'L']
}
df = pd.DataFrame(data)

# Lebel encoding untuk data kategorikal
le_usia = LabelEncoder()
le_pendapatan = LabelEncoder()
le_kelayakan = LabelEncoder()

# Encoding berdasarkan data pelatihan
df['Usia'] = le_usia.fit_transform(df['Usia'])
df['Pendapatan'] = le_pendapatan.fit_transform(df['Pendapatan'])
df['Kelayakan'] = le_kelayakan.fit_transform(df['Kelayakan'])

# Memisahkan fitur dan target
X_nb = df[['Usia', 'Pendapatan']]
y_nb = df['Kelayakan']

# Membuat model naive bayes untuk kategori
model_nb = CategoricalNB()
model_nb.fit(X_nb, y_nb)

# Nasabah baru yang ingin diprediksi kelayakannya
nasabah_new = pd.DataFrame({
    'Usia' : [45],
    'Pendapatan': ['Sedang']
})

# Encoding nasabah baru berdasarkan encoder dari data pelatihan
nasabah_new['Usia'] = le_usia.transform([45])
nasabah_new['Pendapatan'] = le_pendapatan.transform(['Sedang'])

# Memprediksi kelayakan nasabah baru
pred_kelaykan_nasabah = model_nb.predict(nasabah_new)

# Menampilkan hasil prediksi
text = 'Layak' if pred_kelaykan_nasabah[0] == 1 else 'Tidak Layak'
print(f"Hasil prediksi kelayakan nasabah baru: {text}")