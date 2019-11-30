import numpy as np


def objective_func(x1, x2):
    return 500 * x1 + 450 * x2


a = np.array([[6, 5], [10, 20]])
new_b = np.array([62, 150])
x = np.linalg.solve(a, new_b)

z = objective_func(x[0], x[1])
shadow_price = z - 5221 + (3.0 / 7.0)
print 'x1 = {}, x2 = {}, z = {}, Shadow price = {}'.format(x[0], x[1], z, shadow_price)
