import numpy as np
from matplotlib import pyplot as plt

# # Membuat plot sederhana
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.title("Grafik Sin Wave")
# plt.show()


# # Menambahkan elemen pada plot
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, label='Sine Wave')
# plt.plot(x, y2, label='Cosine Wave')

# plt.title("Grafik Sine dan Cosine Wave")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")

# plt.grid(True)  # menambahkan grid
# plt.legend()    # menambahkan legenda
# plt.show()      # menampilkan plot

# # plt.savefig('plottt.png')    # Untuk menyimpan plot ke file


# # Line Plot
# x = np.linspace(0, 10, 100)
# y = (x-2)**2 + 2*x + 2
# plt.plot(x,y)
# plt.title("Line Plot")
# plt.show()


# # Bar plot
# categories = ['Apple', 'Banana', 'Cherry', 'Date']
# values = [10, 15, 7, 5]
# plt.bar(categories, values)
# plt.title("Fruits Store sales")
# plt.show()


# # Histogram
# data = np.random.randn(1000)
# plt.hist(data, bins=20)
# plt.title("Histogram")
# plt.show()


# # Scatter plot
# x = np.random.rand(100)
# y = np.random.rand(100)

# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.show()


# Pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 50, 75]

plt.pie(sizes, labels=labels, autopct='%1.1f')
plt.title('Pie Chart')
plt.show()