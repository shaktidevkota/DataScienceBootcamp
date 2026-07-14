#New Weight = Old Weight − Learning Rate × Gradient
#  Initial weight
weight = 0.5

# Learning rate
learning_rate = 0.1

# Gradient 
gradient = 0.3

print("Weight Before:", weight)

# Update rule
weight = weight - learning_rate * gradient

print("Weight After :", weight)