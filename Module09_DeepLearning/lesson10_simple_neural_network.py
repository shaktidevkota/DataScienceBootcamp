import numpy as np

# Dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [0], [0], [1]])

# Random weights
np.random.seed(42)
weights = np.random.randn(2, 1)
bias = np.random.randn(1)

learning_rate = 0.1


# Sigmoid Activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Sigmoid Derivative
def sigmoid_derivative(x):
    return x * (1 - x)


# Training
for epoch in range(1000):

    # Forward Propagation
    z = np.dot(X, weights) + bias
    output = sigmoid(z)

    # Loss
    loss = np.mean((y - output) ** 2)

    # Backpropagation
    error = y - output

    d_output = error * sigmoid_derivative(output)

    d_weights = np.dot(X.T, d_output)

    d_bias = np.sum(d_output)

    # Update
    weights += learning_rate * d_weights
    bias += learning_rate * d_bias

    if epoch % 100 == 0:
        print(f"Epoch {epoch}")
        print(f"Loss : {loss:.5f}")
        print("-" * 30)

print("\nFinal Predictions")
print(sigmoid(np.dot(X, weights) + bias))