from gurobipy import *
from datetime import datetime

startTime = datetime.now()

m = Model("normal")
x1 = m.addVar(name="x1", vtype=GRB.BINARY)
x2 = m.addVar(name="x2", vtype=GRB.BINARY)
x3 = m.addVar(name="x3", vtype=GRB.BINARY)
x4 = m.addVar(name="x4", vtype=GRB.BINARY)
m.update()

m.setObjective(16 * x1 + 10 * x2 + 4 * x4, GRB.MAXIMIZE)

m.addConstr(8 * x1 + 2 * x2 + x3 + 4 * x4 <= 10, "first_cons")
m.addConstr(x1 + x2 <= 1, "second_cons")
m.addConstr(x3 + x4 <= 1, "third_cons")

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))

print('Obj: %f' % m.objVal)

print datetime.now() - startTime
