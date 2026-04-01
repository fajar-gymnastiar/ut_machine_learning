import numpy as np

# Operasi aritmatika, statistik dasar, dan masking menggunakan numpy
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(np.add(x, y)) # penjumlahan
print(np.subtract(x, y)) # pengurangan
print(np.multiply(x, y)) # perkalian
print(np.divide(x, y)) # pembagian

arr = np.array([1, 2, 3, 4, 5])
mean_val = np.mean(arr)  # rata-rata (mean)
std_val = np.std(arr)    # standar deviasi
var_val = np.var(arr)    # varians

print(mean_val, std_val, var_val)

#masking
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mask = arr2 > 5   # membuat mask dengan kondisi > 5
filtered_arr = arr2[mask]
arr2[mask] = 0 # mengubah elemen  berdasarkan mask
print(filtered_arr)
print(arr2)