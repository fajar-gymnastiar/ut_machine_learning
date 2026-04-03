import pandas as pd

# Memuat data dari file CSV dan JSON
df_transactions = pd.read_csv('data/transactions.csv')
df_customers = pd.read_csv('data/customer.csv')
df_campaigns = pd.read_json('data/campaigns.json')

# print(df_transactions.head())
# print(df_customers.head())
# print(df_campaigns.head())

# Inner join
# Menggabungkan data transaksi dengan data pelanggan berdasarka customer_id
df_inner = pd.merge(df_transactions, df_customers, on='customer_id', how='inner')
print("Hasil inner join:\n", df_inner)

# Left Join
# Menggabungkan data transaksi dengan data pelanggan menggunakan left join
df_left = pd.merge(df_transactions, df_customers, on='customer_id', how='left')
print("Hasil Left Join:\n", df_left)

# Right Join
df_right = pd.merge(df_transactions, df_customers, on='customer_id', how='right')
print("Hasil right join:\n", df_right)

# Full Join
full = pd.merge(df_transactions, df_customers, on='customer_id', how='outer')
print("Hasil full join:\n", full)

# concatenation
additional_trans = pd.DataFrame({
    'transaction_id': [6, 7],
    'customer_id': [107, 108],
    'transaction_date': ['2023-08-11', '2023-08-12'],
    'amount': [100.00, 200.00],
    'campaign_id': [1001, 1002]
})

# Concat vertikal
concat_vertical = pd.concat([df_transactions, additional_trans])
print("Hasil concat vertikal:\n", concat_vertical)

# Concat horizontal
# concat_horizontal = pd.concat([df_transactions, additional_trans], axis=1)
# print("Hasil concat horizontal:\n", concat_horizontal)

# Union
# Menggabungkan dataframe dengan struktur yang sama, minghilangkan duplikat
union = pd.concat([df_transactions, additional_trans]).drop_duplicates()
print("Hasil Union:\n", union)

# Menggunakan join dengan data campaign
df_final = pd.merge(full, df_campaigns, on='campaign_id', how='left')
print("Hasil join dengan campaign:")
print(df_final)

# identifikasi duplikat
# duplicates = df_final.duplicated()
# print("Jumlah baris duplikat: ", duplicates)