import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO

data = """id,value1,value2,value3
1,10,20,30
2,12,,35
3,14,25
4,15,30,40
5,15,,
6,16,32,45
7,18,34,
8,20,36,50
9,,38,55
10,22,40"""

# Membaca dataset dari string
df = pd.read_csv(StringIO(data))

# Identifikasi missing value
missing_values = df.isnull().sum()
print("Missing value per column:\n", missing_values)
# Visualisasi
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.show()