import numpy as np
import itertools


def ismagicrectangle(rect):
    magic_rect = rect.reshape(3, 3)
    sum_line = set(magic_rect.sum(axis=0))
    sum_column = set(magic_rect.sum(axis=1))
    sum_diag1 = magic_rect.trace()
    sum_diag2 = magic_rect[::-1].trace()
    if len(sum_line) == len(sum_column) == 1:
        if sum_diag1 == sum_diag2 and sum_diag1 in sum_line and sum_diag2 in sum_column:
            return True
    else:
        return False


count = 0  # счетчик магических квадратов
for i in np.array(list(itertools.permutations(range(1, 10), 9))):
    if ismagicrectangle(i):
        print(f'{i} - True')
        count += 1
print(f'Всего - {count} магических квадратов')
