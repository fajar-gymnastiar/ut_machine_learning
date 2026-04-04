from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Contoh data
y_true = np.array([0, 1, 0, 1, 0, 1, 0, 1])
y_pred = np.array([0, 0, 0, 1, 0, 1, 1, 1])

# Mencetak classification report pada library scikit-learn
report = classification_report(y_true, y_pred, target_names=['Class 0', 'Class 1'])
print("Classification report:\n", report)

# Membuat confussion matrix
conf_matrix = confusion_matrix(y_true, y_pred)

# plotting confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel('Predicted Labels')
plt.ylabel('Actual Labels')
plt.title('Confussion matrix')
plt.show()