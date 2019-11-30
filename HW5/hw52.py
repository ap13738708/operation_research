from gurobipy import *

m = Model("lp1")
x1a = m.addVar(name="x1a")
x1b = m.addVar(name="x1b")
x1c = m.addVar(name="x1c")
x11 = m.addVar(name="x11")
x12 = m.addVar(name="x12")

x2a = m.addVar(name="x2a")
x2b = m.addVar(name="x2b")
x2c = m.addVar(name="x2c")
x21 = m.addVar(name="x21")
x22 = m.addVar(name="x22")

xa1 = m.addVar(name="xa1")
xb1 = m.addVar(name="xb1")
xc1 = m.addVar(name="xc1")
xa2 = m.addVar(name="xa2")
xb2 = m.addVar(name="xb2")
xc2 = m.addVar(name="xc2")

y1 = m.addVar(name="y1")
y2 = m.addVar(name="y2")
y3 = m.addVar(name="y3")
m.update()

equation = 50 * y1 + 60 * y2 + 68 * y3 + \
           1 * x1a + 2 * x1b + 8 * x1c + 4 * x11 + 8 * x12 + \
           6 * x2a + 3 * x2b + 1 * x2c + 7 * x21 + 6 * x22 + \
           4 * xa1 + 3 * xb1 + 5 * xc1 + \
           6 * xa2 + 4 * xb2 + 3 * xc2

M = 1000
m.setObjective(equation, GRB.MINIMIZE)

m.addConstr(y1 + y2 + y3 == 1, "choose_warehouse")

m.addConstr(x1a + x2a <= M * y1, "capacity_a")
m.addConstr(x1b + x2b <= 60 * y2, "capacity_b")
m.addConstr(x1c + x2c <= 70 * y3, "capacity_c")

m.addConstr(x1a + x1b + x1c + x11 + x12 <= 50, "supply_1")
m.addConstr(x2a + x2b + x2c + x21 + x22 <= 75, "supply_2")

m.addConstr(x1a + x2a >= xa1 + xa2, "in_out_a")
m.addConstr(x1b + x2b >= xb1 + xb2, "in_out_b")
m.addConstr(x1c + x2c >= xc1 + xc2, "in_out_c")

m.addConstr(x11 + x21 + xa1 + xb1 + xc1 >= 75, "demand_1")
m.addConstr(x12 + x22 + xa2 + xb2 + xc2 >= 50, "demand_2")

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))

print('Obj: %f' % m.objVal)

print 'reduced costs: '
print ' ', m.getAttr('rc', m.getVars())
print 'shadow prices: '
print ' ', m.getAttr('pi', m.getConstrs())
