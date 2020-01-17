import math
import numpy

class KnapsackDPResult(object):
    def __init__(self, f, result):
        # instance variables
        # optimal objective value
        self.f = f
        # optimal combination of goods in knapsack 
        self.result = result
        
def knapsackDP(C,W,V):
    # C is the capacity, which is a constant
    # W is the weight vector
    # V is the value vector
    
    # fill in the logic for Dynamic Programming here: 
    items = len(W)
    
    f = numpy.zeros((items+1, C+1))
    
    optM = numpy.zeros((items+1, C+1))
    result = numpy.zeros(items)
    
    iSet = range(items)
    iSet.reverse()
   
    for i in iSet:
        for j in range(C+1):
            m = numpy.zeros(C+1)
            for k in range(int(math.floor(C/W[i]))+1):
                if(j-W[i]*k >= 0): 
                    m[k] = V[i]*k + f[i+1][j-W[i]*k]
            f[i][j] = m[numpy.argmax(m)]
            optM[i][j] = numpy.argmax(m)
    
    optIndex = numpy.unravel_index(numpy.argmax(f, axis=None), f.shape)
    optf = f[optIndex]

    print optM
    x = 0
    for i in range(items):
        if(i==0):
            x = optIndex[1]
            result[i] = int(optM[i][x])
        else:
            x = int(x-W[i-1]*result[i-1])
            result[i] = int(optM[i][x])
    
    return KnapsackDPResult(optf, result)

