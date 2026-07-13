import numpy as np

# Inputs
age = 25
income = 40000

# Weights
w_age = 0.03
w_income = 0.00002

# Bias
bias = -1

# Weighted Sum
z = (age * w_age) + (income * w_income) + bias

print("Weighted Sum (z):", z)

# Step Activation
if z >= 0:
    print("Loan Approved")
else:
    print("Loan Rejected")