import pandas as pd
from datetime import datetime

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Mike', 'Pepper'],
    'Age': [28, 24, 35, 32, 28, 26],
    'City': ['Berlin', 'Paris', 'London', 'New York', 'Paris', 'New York']
}

custom_index = ['a', 'b', 'c', 'd', 'e', 'f']
df = pd.DataFrame(data)

# # Slicing baris dan kolom menggunakan iloc dan loc
# subset_iloc = df.iloc[0:3, [0]]
# print(subset_iloc)

# subset_loc = df.loc['a':'c', ['City']]
# print(subset_loc)

# Menambah kolom baru
df['Salary'] = [50000, 60000, 70000, 80000, 85000, 90000]

# Mengubah nilai kolom
df['Age'] = df['Age'] + 1

# Menghapus kolom, harus menggunakan argumen axis=1
# df = df.drop('City', axis=1)

# menghapus baris, harus menggunakan argumen axis=0
# df = df.drop(0, axis=0)

print(df)

now = datetime.now()
print("Sekarang: ", now)

# Belajar konversi datetime dari data string
data2 = {
    'date': ['2024-08-09', '2024-08-10', '2024-08-11'],
    'value': [10, 20, 30]
}
df_date = pd.DataFrame(data2)
df_date['date'] = pd.to_datetime(df_date['date'])
df_date['year'] = df_date['date'].dt.year
df_date['month'] = df_date['date'].dt.month
print(df_date)

data3 = pd.DataFrame({
    'Kolom1': [1, 2, None, None],
    'Kolom2': [None, 6, 7, 8]
})
print(data3.isna().sum())

# Mengganti nilai null
data_fill = data3.fillna(0)  #dengan angka 0
data_fill_mean = data3.fillna(data3.mean())  # dengan rata-rata kolom
print(data_fill_mean)

grouped = df.groupby('City').count()
grouped2 = df.groupby('City').describe()
print(grouped2)