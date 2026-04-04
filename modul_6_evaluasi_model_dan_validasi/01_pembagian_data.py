from sklearn.model_selection import train_test_split
import numpy as np

X = np.random.rand(100, 10)
y = np.random.randint(0, 2, 100)

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=2024, stratify=y)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

print("training target distribution:", np.bincount(y_train))
print("Testing target distibution:", np.bincount(y_test))