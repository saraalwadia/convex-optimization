import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# Expected Return vector
e_return = np.array([0.12, 0.10, 0.07])

# Variance and covariance matrix
Sigma = np.array([
    [0.10, 0.02, 0.04],
    [0.02, 0.08, 0.03],
    [0.04, 0.03, 0.09]
])   

# Decision variable: investment weights
x = cp.Variable(3)
ret_min = 0.09  # Minimum required return

# Objective: minimize risk (portfolio variance)
objective = cp.Minimize(cp.quad_form(x, Sigma)) #Minimize x^T Σx

# Constraints
constraints = [
    e_return @ x >= ret_min,
    cp.sum(x) == 1,
    x >= 0
]

# Define and solve the problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Print results
print("Optimal investment:", x.value)
print("Minimum portfolio risk (variance):", problem.value)


# Plot the allocation
asset_names = ['Asset 1', 'Asset 2', 'Asset 3']
weights = x.value

plt.bar(asset_names, weights, color='skyblue')
plt.title("Optimal Portfolio Allocation")
plt.ylabel("Investment Weight")
plt.ylim(0, 1)
plt.grid(axis='y')

plt.show()