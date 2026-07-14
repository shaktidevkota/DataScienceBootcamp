import numpy as np
import matplotlib.pyplot as plt

# Input values
x = np.linspace(-10, 10, 200)

# ReLU
relu = np.maximum(0, x)

# Sigmoid
sigmoid = 1 / (1 + np.exp(-x))

# Tanh
tanh = np.tanh(x)

# Leaky ReLU
leaky_relu = np.where(x > 0, x, 0.01 * x)

# Plot each activation separately
plt.figure(figsize=(6, 4))
plt.plot(x, relu)
plt.title("ReLU")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(x, sigmoid)
plt.title("Sigmoid")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(x, tanh)
plt.title("Tanh")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(x, leaky_relu)
plt.title("Leaky ReLU")
plt.grid(True)
plt.show()