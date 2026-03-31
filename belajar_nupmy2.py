import numpy as np

# Studi kasus : Analisis suhu harian selama setahun

np.random.seed(0)   # Menggunakan seed untuk memastikan hasil yang sama setiap kali dijalankan

# Membuat data random suhu harian selama 1 tahun
temperatures = np.random.uniform(low = -10, high = 35, size = 365)
# print("Dataset suhu harian: \n", temperatures)

# Menghitung rata-rata
mean_temp = np.mean(temperatures)
print(f"Rerata suhu : {mean_temp:.2f} derajat celcius")

# Menghitung median
median_temp = np.median(temperatures)
print(f"Median suhu: {median_temp:.2f} derajat celcius")

# Menghiutung standar deviasi
std_temp = np.std(temperatures)
print(f"Standar deviasi suhu: {std_temp:.2f}")

# Menghitung varians
var_temp = np.var(temperatures)
print(f"Varians suhu: {var_temp:.2f}")

# Mencari max min suhu
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
print(f"Suhu Max: {max_temp:.2f} \n Suhu terendah: {min_temp:.2f}")

# Mencari indeks hari dengan suhu maksimum dan minimum
max_temp_day = np.argmax(temperatures)
min_temp_day = np.argmin(temperatures)
print(f"Hari dengan sushu tertinggi: Hari ke-{max_temp_day + 1}")
print(f"Hari dengan sushu terendah: Hari ke-{min_temp_day + 1}")