import numpy as np

# Initial weight
weight = 2.0

# Learning rate
learning_rate = 0.1

# Simple dataset: y = 2x
X = np.array([1, 2, 3, 4])
y_true = np.array([2, 4, 6, 8])

print("Initial Weight:", weight)

for epoch in range(10):

    # Prediction
    y_pred = weight * X

    # Calculate Mean Squared Error
    loss = np.mean((y_true - y_pred) ** 2)

    # Gradient
    gradient = -2 * np.mean(X * (y_true - y_pred))

    # Weight Update (SGD)
    weight = weight - learning_rate * gradient

    print(f"Epoch {epoch+1}")
    print(f"Loss : {loss:.4f}")
    print(f"Weight: {weight:.4f}")
    print("-" * 30)