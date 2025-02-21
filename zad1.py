import numpy as np

n = int(input())
random_matrix = np.random.randint(1, 10, size=(n,n))
print(random_matrix.max(axis=0))