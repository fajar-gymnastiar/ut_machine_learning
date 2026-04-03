import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# dataset nasabah sebelumnya
data = {
    'Pendapatan': [50000, 60000, 80000, 45000, 90000],
    'Usia': [25, 40, 35, 50, 28],
    'Jumlah Hutang': [5000, 15000, 10000, 3000, 2000],
    'Riwayat Kredit': [700, 650, 750, 600, 720],
    'Kelayakan': [1, 0, 1, 0, 1]
}
df= pd.DataFrame(data)

# Nasabah baru yang ingin di prediksi kelayakannya
nasabah_baru = pd.DataFrame({
    'Pendapatan': [70000],
    'Usia': [30],
    'Jumlah Hutang': [8000],
    'Riwayat Kredit': [690]
})

# Memisahkan fitur dan target
X = df[['Pendapatan', 'Usia', 'Jumlah Hutang', 'Riwayat Kredit']]
y = df['Kelayakan']

# Normalisasi fitur untuk KNN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
nasabah_baru_scaled = scaler.transform(nasabah_baru)

# Membuat model KNN
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_scaled, y)

# Memprediksi kelayakan nasabah baru
kelayakan_pred = knn_model.predict(nasabah_baru_scaled)

# Menampilkan hasil prediksi
if(kelayakan_pred[0] == 1):
    print('Layak')
else:
    print('Tidak Layak')