import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 +3 * X + np.random.randn(100, 1)

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.scatter(X, y, color='blue', label='Titik Data')
plt.plot(X, y_pred, color='red', label='Regresi Linear')
plt.title('Regresi Linear dengan data acak')
plt.xlabel('Fitur (X)')
plt.ylabel('Fitur (y)')
plt.legend()
plt.show()