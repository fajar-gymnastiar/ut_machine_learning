import numpy as py
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = [10, 12, None, 15, 15, None, 16, 18, 20, None]

# Mean imputation
mean = sum(x for x in data if x is not None) / sum(1 for x in data if x is not None)
mean_imputed_data = [x if x is not None else mean for x in data]
print("Data Asli: ", data)
print("Mean: ", mean)
print("Data setelah mean imputation:", mean_imputed_data)

# Median imputation
sorted_data = sorted(x for x in data if x is not None)
n = len(sorted_data)
median = (sorted_data[n // 2]) if n % 2 == 1 else (sorted_data[ n // 2 - 1] + sorted_data[n // 2] / 2)
median_imputed = [x if x is not None else median for x in data]
print("Median: ", median)
print("Data setelah median imputattion: ", median_imputed)

# Mode imputation
mode = Counter(x for x in data if x is not None).most_common(1)[0][0]
mode_imputed = [x if x is not None else mode for x in data]
print("Mode: ", mode)
print("Data setelah mode imputation: ", mode_imputed)