from gurobipy import GRB, Model

m = Model('lagrangian_hw')
m.modelSense = GRB.MAXIMIZE
m.setParam('OutputFlag', False)

x1 = m.addVar(name="x1", vtype=GRB.BINARY)
x2 = m.addVar(name="x2", vtype=GRB.BINARY)
x3 = m.addVar(name="x3", vtype=GRB.BINARY)
x4 = m.addVar(name="x4", vtype=GRB.BINARY)

penalties = [m.addVar(), m.addVar()]

m.update()

u = [2.0] * 2

m.addConstr(8 * x1 + 2 * x2 + x3 + 4 * x4 <= 10, "first_cons")

m.addConstr(penalties[0] == 1 - x1 - x2)
m.addConstr(penalties[1] == 1 - x3 - x4)

for k in range(1, 101):
    m.setObjective(16 * x1 + 10 * x2 + 4 * x4  # Original objective function
                   # Penalties for dualized constraints
                   + u[0] * (1 - x1 - x2) + u[1] * (1 - x3 - x4))

    m.optimize()

    print 'iteration', k, 'obj =', m.objVal, \
        'u =', u, 'penalties =', [p.x for p in penalties]

    stop = True
    eps = 10e-6

    for u_i, p_i in zip(u, penalties):
        # print 'out: u={}, p={}'.format(u_i, p_i.x)
        if abs(u_i) > eps and abs(p_i.x) > eps:
            # print 'use in: u={}, p={}'.format(u_i, p_i.x)
            stop = False
            break

    if stop:
        print 'primal feasible & optimal'
        break

    else:
        s = 1.0 / k
        for i in range(2):
            u[i] = max(u[i] - s * penalties[i].x, 0.0)

print 'objective =', m.objVal

for v in m.getVars():
    print('%s: %f' % (v.varName, v.x))
