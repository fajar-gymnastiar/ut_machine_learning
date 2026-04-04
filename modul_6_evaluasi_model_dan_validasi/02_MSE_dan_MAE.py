from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

y_true = np.array([3.0, -0.5, 2.0, 7.0])
y_pred = np.array([2.5, 0.0, 2.1, 7.8])

def calculate_mse(y_true, y_pred): 
    return np.mean((y_true - y_pred) ** 2)

# perhitungan MSE menggunakan implementasi numpy
mse_custom = calculate_mse(y_true, y_pred)
print("MSE (custom function):", mse_custom)

# perhitungan MSE menggunakan fungsi pada library scikit-learn
mse_sklearn = mean_squared_error(y_true, y_pred)
print("MSE (scikit-learn):", mse_sklearn)

# Perhitungan MAE menggunakan fungsi scikit-learn
mae = mean_absolute_error(y_true, y_pred)
print("MAE (scikit-learn):", mae)