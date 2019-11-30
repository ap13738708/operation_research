import numpy as np


# A --> matrix problem
# BV --> column indices for basic variables
# r --> indices of constraints
# c --> column in matrix problem
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


dual_problem = np.array([
    [1, 10, 6, 15, 0, 0, 0, 0],  # --> objective function
    [0, 1, 1, 3, 1, 0, 0, 2],  # --> constraint 1
    [0, -1, -2, -4, 0, 1, 0, 3],  # --> constraint 2
    [0, 1, 3, 5, 0, 0, 1, 4]  # --> constraint 3
])

basic_var_pos = [4, 5, 6]

pivot_y3, basic_var_pos = pivot(dual_problem, basic_var_pos, 1, 3)
print 'After pivot y3: {} {}'.format(pivot_y3, basic_var_pos)

pivot_y1, basic_var_pos = pivot(pivot_y3, basic_var_pos, 1, 1)
print 'After pivot y1: {} {}'.format(pivot_y1, basic_var_pos)
