# Belajar tentang modul & package
from my_package import module1, module2
print (module1.func1())
print (module2.func2())

import numpy as np

array = np.array([1, 2, 3, 4, 5])
print (array.mean())

import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'], 'age' : [25, 30, 35]}
df = pd.DataFrame(data)
print(df)

#belajar exception handling
try:
    hasil = 10 / 0
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol")