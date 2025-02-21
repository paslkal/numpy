import numpy as np
arr = np.array([1,2,3, 1, 2, 2, 1, 5])
freq = np.bincount(arr)
max_frequency = max(freq)
print('Наиболее часто встречающиеся числа:')
for index, value in enumerate(freq):
    if value == max_frequency:
        print(index, end=' ')