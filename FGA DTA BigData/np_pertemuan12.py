# import numpy as np

# temp = np.array([29.3, 42.1, 18.8, 16.1, 38.0, 12.5, 12.6, 49.9, 38.6, 31.3, 9.2, 22.2]).reshape(2,2,3)

# print(f"Ini adalah temp.shape =", temp.shape)
# print(f"Ini adalah temp =\n", temp)
# print(f"Ini adalah np.swapaxes =\n", np.swapaxes(temp,1,2))

# import numpy as np

# table = np.array([
#     [5,3,7,1],
#     [2,6,7,9],
#     [1,1,1,1],
#     [4,3,2,0],
# ])

# print(table.max())
# print(table.max(axis=0))
# print(table.max(axis=1))
import numpy as np

def status(angka):
    return angka % 2 != 0

random_array = np.random.randint(1, 101, size=(4, 5))
status_array = np.vectorize(status)(random_array)

print("Array Nilai Random:")
print(random_array)

print("\nArray Status (True jika ganjil, False jika genap):")
print(status_array)