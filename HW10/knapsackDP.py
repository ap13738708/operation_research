import math
import numpy as np


class KnapsackDPResult(object):
    def __init__(self, f, result):
        # instance variables
        # optimal objective value
        self.f = f
        # optimal combination of goods in knapsack 
        self.result = result


def knapsackDP(C, W, V):
    items = len(W)

    iSet = range(items)
    iSet.reverse()

    f = np.zeros((items + 1, C + 1))
    m_used = np.zeros((items + 1, C + 1))
    for item in iSet:
        #     print 'Item:', item
        m = int(math.floor(C / W[item]))
        #     print 'Possible unit', m
        for k in range(C + 1):
            value = []
            for j in range(m + 1):
                #             print '     Row:', k
                #             print 'Check:', k, int(m_used[item+1][k]) + j
                if k - W[item] * j >= 0:
                    temp = V[item] * j + f[item + 1][k - W[item] * j]
                    #                 print 'K:',k, 'J:', j, 'Value:', temp
                    #                 print '        Column',j
                    value.append(temp)
                else:
                    break
            #             print value
            #         print m_used
            f[item][k] = max(value)
            m_used[item][k] = value.index(max(value))

    opt_index = np.unravel_index(np.argmax(f, axis=None), f.shape)
    optf = f[opt_index]

    result = np.zeros(items, dtype=int)
    for i in range(items):
        if i == 0:
            x = opt_index[1]
            result[i] = int(m_used[i][x])
        else:
            x = int(x - W[i - 1] * result[i - 1])
            result[i] = int(m_used[i][x])

    return KnapsackDPResult(optf, result)
