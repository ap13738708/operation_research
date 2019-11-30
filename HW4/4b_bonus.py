import numpy as np


def pivot(A, BV, r, c):
    A = np.array(A)
    A = A.astype(float)
    A[r, :] = A[r, :] / A[r, c]
    rows = len(A)
    for i in range(rows):
        if i != r:
            A[i, :] = A[i, :] - A[i, c] * A[r, :]
    BV[r - 1] = c
    return A, BV


# z x1, x2, x3, s1, s2, s3 = bi
A = [
    [1, -5, -4, -3, 0, 0, 0, 0],
    [0, 2, 3, 1, 1, 0, 0, 5],
    [0, 4, 1, 2, 0, 1, 0, 11],
    [0, 3, 4, 2, 0, 0, 1, 8]
]

BV = [4, 5, 6]


def simplex_method(A, BV):
    matrix = np.array(A)
    matrix = matrix.astype(float)
    print matrix
    basic_var_pos = BV[:]

    while True:

        temp = matrix[0][matrix[0] != 0]
        if all(i > 0 for i in temp[1: len(temp)]):
            break

        idx_min = np.argmin(matrix[0])
        print 'index : {}'.format(idx_min)

        check_pivot = map(lambda row: row[-1] / row[idx_min], matrix[1: len(matrix)])
        check_pivot = np.array(check_pivot)
        print 'check pivot : {}'.format(check_pivot)

        row_to_pivot = np.where(check_pivot == min(check_pivot[check_pivot >= 0]))[0][0] + 1
        print 'row: {}'.format(row_to_pivot)

        matrix, basic_var_pos = pivot(matrix, basic_var_pos, row_to_pivot, idx_min)

        print matrix, basic_var_pos


simplex_method(A, BV)
