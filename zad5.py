import numpy as np

arr = [
    [1,2,1],
    [10,20,3],
    [15,20,4]
]

arr = np.array(arr)

m = arr.min()

freq = np.unique(arr, return_counts=True)

min_height, frequency = freq[0][0], freq[1][0]
print(f'Самая низкая высота на ландшавте равна {min_height}. Она встречается {frequency} раз')