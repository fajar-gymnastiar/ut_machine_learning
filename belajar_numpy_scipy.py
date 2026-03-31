import numpy as np
from scipy.optimize import minimize # optimasi

# Fungsi yang akan diminimalkan
def f (x):
    return (x - 3)**2

# Titik awal untuk optimasi
x0 = 0

# Melakukan Optimasi
result = minimize(f, x0)
print("Nilai optimal [x]: ", result.x)
print("Nilai minimum [f(x)]: ", result.fun)