import numpy as np


def ismagicrectangle(rect):
    sum_line = np.sum(rect.sum(axis=0))
    sum_column = np.sum(rect.sum(axis=1))
    sum_diag1 = rect.trace()
    sum_diag2 = rect[::-1].trace()
    size = rect.shape()
    print(f'сумма строк: {rect.sum(axis=0)}')
    print(f'сумма столбцов: {rect.sum(axis=1)}')
    print(f'сумма диагоналей {sum_diag1}, {sum_diag2}')
    return True if sum_line == sum_column == sum_diag1 == sum_diag2 else False


# a = tuple(i for i in range(100))
arr = np.array([2, 7, 6, 9, 5, 1, 4, 3, 8])
print(arr)
print(arr.shape)
print(ismagicrectangle(arr.reshape(3, 3)))