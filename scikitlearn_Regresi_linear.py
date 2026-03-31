import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 4, 5, 4, 5]
}
df = pd.DataFrame(data)

X = df[['X']]
y = df['Y']

# Membagi data menjadi training dan testing
X_train, X_test, y_train, Y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=0
)

# Membuat dan melatih model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediksi dan evaluasi
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(Y_test, y_pred))

# Visualisasi
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()