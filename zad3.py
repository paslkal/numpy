import numpy as np
arr = [[10, 15, 20],
 [5, 25, 15],
 [30, 10, 5]]

arr = np.array(arr)

total_sales = arr.sum(axis=1)

print(total_sales)