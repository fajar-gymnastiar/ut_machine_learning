import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(24)
X_new = 3 * np.random.rand(100, 1)
y_new = 5 + 2 * X_new**2 + 0.5 * X_new**3 + np.random.randn(100, 1)

# Menggunakan derajat 2 untuk regresi polinomial pada data baru
poly_features_degree2 = PolynomialFeatures(degree=2)
X_poly_d2 = poly_features_degree2.fit_transform(X_new)

# memebuat model regresi polinomial derajat 2
model_poly_d2 = LinearRegression()
model_poly_d2.fit(X_poly_d2, y_new)
# Mengurutkan data untuk hasil prediksi yang lebih halus
X_new_sorted = np.sort(X_new, axis=0)
X_poly_new_sorted = poly_features_degree2.transform(X_new_sorted)
# Memprediksi hasil dengan data yang sudah diurutkan
y_poly_pred_new_sorted = model_poly_d2.predict(X_poly_new_sorted)

# Plot hasil regresi polinomial derajat 2 dengan garis yang lebih halus
plt.scatter(X_new,y_new, color='blue', label='Titik data baru')
plt.plot(X_new_sorted, y_poly_pred_new_sorted, color='green', label='Regresi Polinomial derajat 2')
plt.title('Regresi Polinomial Derajat 2 dengan data acak baru (Garis Halus)')
plt.xlabel('Fitur (X)')
plt.ylabel('Target (Y)')
plt.legend()
plt.show()