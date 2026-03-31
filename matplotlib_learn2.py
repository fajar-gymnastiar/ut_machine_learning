import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.DataFrame({
    'Category': ['A'] * 50 + ['B'] * 50,
    'Values': np.concatenate([np.random.randn(50), np.random.randn(50) + 2])
})
#Box Plot
sns.boxplot(x="Category", y='Values', data=data)
plt.title("Box Plot")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# Heat map
data2 = np.random.rand(10, 12)

sns.heatmap(data2, annot=True, cmap='viridis')
plt.title("Heatmap")
plt.show()