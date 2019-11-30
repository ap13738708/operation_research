import numpy as np
import matplotlib.pyplot as plt


def cal_max(x_1, x_2):
    return 5 * x_1 + 4 * x_2


x1 = np.linspace(0, 6, num=100, endpoint=False)

constraint_1 = 6.0 - ((3.0 * x1) / 2.0)
constraint_2 = 6.0 - x1
constraint_3 = 1.0 + x1
constraint_4 = [2.0] * x1.shape[0]

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

x = [0, 0, 1, 2.67, 4]
y = [0, 1, 2, 2, 0]
plt.fill(x, y)
plt.show()

print '(0,1), z = {}'.format(cal_max(0, 1.0))
print '(1,2), z = {}'.format(cal_max(1.0, 2.0))
print '(8/3,2), z = {}'.format(cal_max(8.0 / 3, 2.0))
print '(4,0), z = {}'.format(cal_max(4.0, 0))
