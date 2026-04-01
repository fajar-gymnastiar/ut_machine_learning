import numpy as py
import pandas as pd

# contoh sederhana menggunakan rata2 tetangga terdekat sebagai prediktor
data = [10, 12, None, 15, 15, None, 16, 18, 20, None]

def predictive_imputation(data):
    imputed_data = data[:]
    for i in range(len(data)):
        if data[i] is None:
            neighbors = [data[j] for j in range(max(0, i-1), min(len(data), i+2)) if data[j] is not None]
            imputed_data[i] = sum(neighbors) / len(neighbors) if neighbors else None
    return imputed_data

predictive_imputed = predictive_imputation(data)
print("data asli:", data)
print("Data setelah predictive imputation:", predictive_imputed)