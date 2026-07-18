import numpy as np

np.random.seed(42)

# Simulated neuron outputs
neurons = np.array([0.5, 1.2, 0.8, 2.1, 1.5, 0.9])

print("Before Dropout:")
print(neurons)

# 50% Dropout
dropout_rate = 0.5

mask = np.random.binomial(1, 1 - dropout_rate, size=neurons.shape)

after_dropout = neurons * mask

print("\nDropout Mask:")
print(mask)

print("\nAfter Dropout:")
print(after_dropout)