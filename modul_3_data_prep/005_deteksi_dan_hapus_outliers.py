data = [10, 12, 14, 15, 15, 15, 16, 18, 20, 100]

# Menghitung mean & standar deviasi
mean = sum(data) / len(data)
std_dev = (sum((x-mean) ** 2 for x in data) / len(data)) ** 0.5

# Menghitung z-score
z_scores = [(x - mean) / std_dev for x in data]

# Menentukan ambang batas z_score untuk outliers
threshold = 2

# Identifikasi dan hapus outliers
cleaned_data = [x for x, z in zip(data, z_scores) if abs(z) < threshold]

print("Data asli:", data)
print("Z-score:", z_scores)
print("Data cleaned:", cleaned_data)