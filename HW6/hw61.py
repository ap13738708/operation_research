from gurobipy import *


def merge_two_dicts(x, y):
    z = x.copy()
    z.update(y)
    return z


nodes = range(1, 7)
cost_dict = {
    (1, 2): 2429, (1, 3): 1967, (1, 4): 1497, (1, 5): 1650, (1, 6): 2392,
    (2, 3): 1105, (2, 4): 1674, (2, 5): 1320, (2, 6): 5566,
    (3, 4): 2023, (3, 5): 9527, (3, 6): 560,
    (4, 5): 1999, (4, 6): 1273,
    (5, 6): 778
}

temp = {}

for k1, k2 in cost_dict:
    temp[k2, k1] = cost_dict[k1, k2]
cost_dict = merge_two_dicts(temp, cost_dict)
print cost_dict
# -------------------------------------------->

keys, cost = multidict(cost_dict)

m = Model('TSP')

x, u = {}, {}

for start, dest in keys:
    x[start, dest] = m.addVar(obj=cost[start, dest], vtype='B', name='x_{}{}'.format(start, dest))

N = len(nodes)
for node in nodes:
    if node != nodes[N - 1]:
        u[node] = m.addVar(obj=0, name='u_{}'.format(node))
m.update()

# Constraint for sum of incoming links to 'dest'
for dest in nodes:
    m.addConstr(quicksum(x[start, dest] for start in nodes if start != dest) == 1, 'incom_{}'.format(dest))

# Constraint for sum of outgoing links from 'start'
for start in nodes:
    m.addConstr(quicksum(x[start, dest] for dest in nodes if start != dest) == 1, 'outgo_{}'.format(start))

# Sub-tour elimination constraints
for start, dest in keys:
    if start != nodes[N - 1] and dest != nodes[N - 1]: m.addConstr(u[start] - u[dest] + N * x[start, dest] <= N - 1,
                                                                   'subtour_{}{}'.format(start, dest))

# Compute optimal solution
m.optimize()
# Print solution
if m.status == GRB.Status.OPTIMAL:
    print 'objective: %f' % m.ObjVal
    solution = m.getAttr('x', x)
    for i, j in keys:
        if solution[i, j] > 0:
            print('%s -> %s: %g' % (i, j, solution[i, j]))