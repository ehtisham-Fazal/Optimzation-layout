from pulp import *
import numpy as np

model = LpProblem("L1M", LpMaximize)

K = range(3)  
I = range(4)  
A = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 0], [1, 0, 1]])  
E = np.array([[0, 3, 2], [3, 0, 1], [2, 1, 0]])  

x = LpVariable.dicts("x", [(i, k) for i in I for k in K], cat=LpBinary)
X = LpVariable("X")

y = LpVariable.dicts("y", [(k1, k2, i1, i2) for k1 in K for k2 in K for i1 in I for i2 in I], cat=LpBinary)

model += X

for i in I:
    model += lpSum([x[(i, k)] for k in K]) == 1

for k in K:
    model += lpSum([x[(i, k)] for i in I]) == 1

for i in I:
    for k in K:
        model += x[(i, k)] <= A[i, k]

for k1 in K:
    for k2 in K:
        for i1 in I:
            for i2 in I:
                model += y[(k1, k2, i1, i2)] == LpAffineExpression([(x[(i1, k1)], 1), (x[(i2, k2)], 1)])
                model += E[k1, k2] * y[(k1, k2, i1, i2)] <= X

model.solve()

print(f"Objective function value: {value(X)}")
for i in I:
    for k in K:
        print(f"x_({i+1},{k+1}) = {value(x[(i, k)])}")
