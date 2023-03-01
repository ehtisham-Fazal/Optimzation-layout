from pulp import *
problem = LpProblem('products', LpMaximize)
A = LpVariable('Product_A', lowBound=0 , cat=LpInteger)
B = LpVariable('product_B', lowBound=0 , cat=LpInteger)
# Our Objective Function
problem += 20000*A + 45000*B , 'Objective Function'
#Constraints
problem += 4*A + 5*B <= 30 , 'Location A'
problem += 3*A + 6*B <=30, 'Location B'
problem += 2*A + 7*B <=30, 'Location C'
print("Current Status: ", LpStatus[problem.status]) 
problem.solve()
print("Number of  product A sell : ", A.varValue)
print("Number of product B sell: ", B.varValue)
print("Total Profit: ", value(problem.objective))
