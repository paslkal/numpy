import numpy as np

arr = [[8, 7, 9],
 [6, 8, 7],
 [9, 9, 8],
 [7, 6, 8]]
arr = np.array(arr)
average_grades = np.average(arr, axis=1)
print(average_grades)