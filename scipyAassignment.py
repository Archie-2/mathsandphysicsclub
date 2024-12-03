import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(vars):
    x, y = vars
    return 2 * (x - y - 3)**2 + 4 * (x + 2*y + 1)**4

# Define the constraints
constraints = [
    {'type': 'ineq', 'fun': lambda vars: vars[0] - vars[1] + 3},  # x - y + 3 >= 0
    {'type': 'ineq', 'fun': lambda vars: 5 - ((vars[0] + 2)**2 + (vars[1] + 1)**2)}  # (x+2)^2 + (y+1)^2 <= 5
]

# Initial guess
initial_guess = [0, 0]

# Solve the optimization problem
result = minimize(objective, initial_guess, constraints=constraints)

# Output the results
print("Optimal value of x and y:", result.x)
print("Minimum value of the objective function:", result.fun)
