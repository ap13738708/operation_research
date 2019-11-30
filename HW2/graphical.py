import numpy as np
import matplotlib.pyplot as plt


def cal_max(x_1, x_2):
    return 5 * x_1 + 4 * x_2


x1 = np.linspace(0, 6, num=100, endpoint=False)

constraint_1 = 6.0 - ((3.0 * x1) / 2.0)
constraint_2 = (6.0 - x1) / 3
constraint_3 = 1.0 + x1
constraint_4 = [2.0] * x1.shape[0]

e1 = np.minimum(constraint_3, constraint_4)
e2 = np.minimum(constraint_2, constraint_3)
e3 = np.minimum(constraint_1, constraint_2)

e4 = np.minimum(e1, e2)
e5 = np.minimum(e2, e3)

e6 = np.minimum(e4, e5)

plt.figure(figsize=(5, 5))
plt.title('Graphical Solution')
plt.plot(x1, constraint_1, 'red', label='6*x1 + 4*x2 = 24')
plt.plot(x1, constraint_2, 'blue', label='x1 + 2*x2 = 6')
plt.plot(x1, constraint_3, 'green', label='-x1 + x2 = 1')
plt.plot(x1, constraint_4, 'black', label='x = 2')
plt.legend()
plt.xlabel('x1')
plt.ylabel('x2')
plt.grid()
plt.ylim(0, 4)

plt.fill_between(x1, e6)

idx1 = np.argwhere(np.diff(np.sign(constraint_2 - constraint_3))).flatten()
plt.plot(x1[idx1], constraint_2[idx1], 'ro')

idx2 = np.argwhere(np.diff(np.sign(constraint_2 - constraint_1))).flatten()
plt.plot(x1[idx2], constraint_2[idx2], 'ro')

plt.plot(x1[0], constraint_3[0], 'ro')
plt.plot(4, 0, 'ro')

plt.show()


print '({}, {}), z = {}'.format(x1[idx1[0]], constraint_2[idx1[0]], cal_max(x1[idx1], constraint_2[idx1]))
print '({}, {}), z = {}'.format(x1[idx2[0]], constraint_2[idx2[0]], cal_max(x1[idx2], constraint_2[idx2]))
print '(0, 1), z = {}'.format(cal_max(x1[0], constraint_3[0]))
print '(4, 0), z = {}'.format(cal_max(4.0, 0))
