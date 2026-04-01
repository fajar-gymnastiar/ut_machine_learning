data = [10, 12, None, 15, 15, None, 16, 18, 20, None]

litwise_delete = [x for x in data if x is not None]

print("data asli:", data)
print("Litewise deletion data:", litwise_delete)