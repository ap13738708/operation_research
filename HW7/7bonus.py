from gurobi import *
import BBNode as bn

status = {1: 'LOADED', 2: 'OPTIMAL', 3: 'INFEASIBLE', 4: 'INF_OR_UNBD', 5: 'UNBOUNDED'}


def show_result(text):
    global m
    if m.status == GRB.Status.OPTIMAL:
        print('Optimal from solver {}: '.format(text))
        for v in m.getVars():
            print('%s: %f' % (v.varName, v.x))
        print('Obj: %f' % m.objVal)
        print('-------------------------------------')
    else:
        print('Optimal from solver {}: '.format(text))
        print status[m.status]


m = Model('BranchBound')

x1 = m.addVar(vtype=GRB.CONTINUOUS, name='x1', obj=8)
x2 = m.addVar(vtype=GRB.CONTINUOUS, name='x2', obj=5)

m.setAttr('ModelSense', GRB.MAXIMIZE)

m.update()

m.addConstr(1 * x1 + 1 * x2 <= 6, 'c0')
m.addConstr(9 * x1 + 5 * x2 <= 45, 'c1')

m.setParam('OutputFlag', False)


def branch_and_bound():
    global m
    m.optimize()

    x1, x2 = [v.x for v in m.getVars()]
    obj = m.objVal
    show_result('of node (P0)')

    root = bn.BBNode(None, '', '', 0)

    while True:
        pass
