import numpy as np

# Inputs
X = np.array([25, 40000])

# Weights
W = np.array([0.03, 0.00002])

# Bias
b = -1

# Weighted Sum
z = np.dot(X, W) + b

# ReLU Activation
output = max(0, z)

print("Weighted Sum:", z)
print("Output after ReLU:", output)