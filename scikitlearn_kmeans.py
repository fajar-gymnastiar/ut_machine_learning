import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = {
    'X': [1, 2, 3, 4, 5, 1.5, 3.5, 4.5],
    'Y': [1, 2, 3, 4, 5, 1.5, 3.5, 4.5]
}
df = pd.DataFrame(data)
X = df[['X', 'Y']]
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
print("Cluster Centers:\n", kmeans.cluster_centers_)
print("Labels:\n", kmeans.labels_)

# Visualisasi hasil clustering
plt.scatter(X['X'], X['Y'], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()