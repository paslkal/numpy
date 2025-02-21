import numpy as np
arr = [
    [2,7,6],
    [9,5,1],
    [4,3,8]
]

arr = np.array(arr)

sum_column = arr.sum(axis=0)
sum_rows = arr.sum(axis=1)

print(sum_column)
print(sum_rows)
is_magic_square = True
value_of_magic_square = sum_column[0]
for val in sum_column:
    if val != value_of_magic_square:
        is_magic_square = False

for val in sum_rows:
    if val != value_of_magic_square:
        is_magic_square = False

if is_magic_square:
    print('Двумерный массив является магических квадратом')
else:
    print('Двумерный массив НЕ является магических квадратом')