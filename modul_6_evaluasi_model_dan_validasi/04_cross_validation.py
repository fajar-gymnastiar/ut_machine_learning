from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np

data = load_iris()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2024, stratify=y)

model = RandomForestClassifier(random_state=2024)

# Cross-validation dengan StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=2024)

# Melakukan cross validation menggunakan stratified k-fold
cv_scores = cross_val_score(model, X_train, y_train, cv=skf, scoring='accuracy')

# Melatih model pada training set
model.fit(X_train, y_train)

# Evaluasi model
y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)

print("Stratified K-Fold Cross-Validation Scores:", cv_scores)
print("Mean CV Accuracy:", np.mean(cv_scores))
print("Standard Deviation of CV Scores:", np.std(cv_scores))
print("Test Set Accuracy:", test_accuracy)