from gurobipy import *

m = Model('LP')

cost = {
    (1, 1): 3, (1, 2): 4, (1, 3): 6,
    (2, 1): 5, (2, 2): 7, (2, 3): 5
}

x = {}

for port, market in cost:
    x[port, market] = m.addVar(obj=cost[port, market], vtype=GRB.INTEGER, name='x_{}{}'.format(port, market))

m.update()

port_ls = set(port for port, _ in cost)
market_ls = set(market for _, market in cost)

m.setObjective(quicksum(x[port, market].obj * x[port, market] for port, market in x), GRB.MINIMIZE)

m.addConstr(quicksum(x[1, market] for market in market_ls) <= 15, 'supply_p1')
m.addConstr(quicksum(x[2, market] for market in market_ls) <= 20, 'supply_p2')

m.addConstr(quicksum(x[port, 1] for port in port_ls) >= 17, 'demand_m1')
m.addConstr(quicksum(x[port, 2] for port in port_ls) >= 8, 'demand_m2')
m.addConstr(quicksum(x[port, 3] for port in port_ls) >= 10, 'demand_m3')

m.optimize()

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))

print('Obj: %f' % m.objVal)
