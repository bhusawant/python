# Q.1) Return the array of even rows and odd columns for following:
# a = [[2, 4, 6, 8, 6], [23, 56, 45, 10,  83], [98, 12, 34, 78, 78], [21, 63, 78, 84, 53]]
"""
import numpy
a = numpy.array([[2, 4, 6, 8, 6], [23, 56, 45, 10,  83], [98, 12, 34, 78, 78], [21, 63, 78, 84, 53]])
# even_rows_odd_cols = [[row[col] for col in range(1, len(row), 2)] for row-idx, row in enumerate(a) if row-idx%2==0]

print("Input array:")
print(a)

print("array of even rows and odd columns")

a2 = a[::2, 1::2]
print(a2)
"""

# Q.2) Create aa 8x3 array for numbers from 10 to 34. Split the array into 4 equal parts.

import numpy as np

arr = np.arange(10, 34).reshape(8, 3)
split_arr = np.array_split(arr, 4)

for i, sub_arr in enumerate(split_arr):
    print(f"Split array{i}:\n{sub_arr}\n")





