#MSE=n1​∑(y−y^​)2
import numpy as np

# Actual values
y_true = np.array([1, 0, 1, 1])

# Model predictions
y_pred = np.array([0.9, 0.2, 0.8, 0.7])

# Mean Squared Error
mse = np.mean((y_true - y_pred) ** 2)

print(f"Mean Squared Error (MSE): {mse:.4f}")