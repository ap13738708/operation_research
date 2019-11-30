from gurobipy import *
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

m.optimize()

show_result('of root node (root)')
root = bn.BBNode(None, '', '', 0)

# Branch x1 <= 3 (Left of branch of root node)

m.addConstr(x1 <= 3, 'x1 <= 3')

m.update()
m.optimize()
show_result('when x1 <= 3 and x2 >= 0 (node1)')

m.remove(m.getConstrs()[-1])
node1 = bn.BBNode(root, 'x1', 'ub', 3)

# Branch x1 >= 4 (Right branch of root node)

m.addConstr(x1 >= 4, 'x1 >= 4')

m.update()
m.optimize()
show_result('when x1 >= 4 and x2 >= 0 (node2)')

m.remove(m.getConstrs()[-1])
node2 = bn.BBNode(root, 'x1', 'lb', 4)

# Branch x1 >= 4 and x2 <= 1

m.addConstr(x1 >= 4, 'x1 >= 4')
m.addConstr(x2 <= 1, 'x2 <= 1')

m.update()
m.optimize()
show_result('when x1 >= 4 and x2 <= 1 (node21)')

m.remove(m.getConstrs()[-2:])
node21 = bn.BBNode(node2, 'x2', 'ub', 1)

# Branch x1 <= 4 and x2 <= 1

m.addConstr(x1 <= 4, 'x1 <= 4')
m.addConstr(x2 <= 1, 'x2 <= 1')

m.update()
m.optimize()
show_result('when x1 <= 4 and x2 <= 1 (node211)')

m.remove(m.getConstrs()[-2:])
node211 = bn.BBNode(node21, 'x1', 'ub', 4)

# Branch x1 >= 5 and x2 <= 1

m.addConstr(x1 >= 5, 'x1 >= 5')
m.addConstr(x2 <= 1, 'x2 <= 1')

m.update()
m.optimize()
show_result('when x1 >= 5 and x2 <= 1 (node212)')

m.remove(m.getConstrs()[-2:])
node212 = bn.BBNode(node21, 'x1', 'lb', 5)

# Branch x1 >= 4 and x2 >= 2

m.addConstr(x1 >= 4, 'x1 >= 4')
m.addConstr(x2 >= 2, 'x2 >= 2')

m.update()
m.optimize()
show_result('when x1 >= 4 and x2 >= 2 (node22)')

m.remove(m.getConstrs()[-2:])
node22 = bn.BBNode(node2, 'x2', 'lb', 2)

m.update()


dv_node = node212
print
print 'Showing bounds from node 212 to root'
while dv_node != root:
    print dv_node.dv, dv_node.bound_sense, dv_node.bound
    dv_node = dv_node.parent

# print 'The maximize output of the problem is 40 when x1 = 5, x2 = 0'
# print m.getConstrs()
