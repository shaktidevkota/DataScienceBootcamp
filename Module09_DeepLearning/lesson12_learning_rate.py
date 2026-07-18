import numpy as np

weight = 0.5

X = np.array([1, 2, 3, 4])
y = np.array([2, 4, 6, 8])

learning_rate = 0.01

for epoch in range(20):

    prediction = weight * X
   
    #learning_rate = 0.001
    learning_rate = 2

    loss = np.mean((y - prediction) ** 2)

    gradient = -2 * np.mean(X * (y - prediction))

    weight -= learning_rate * gradient

    print(
        f"Epoch {epoch+1:02d} | "
        f"Weight={weight:.4f} | "
        f"Loss={loss:.4f}"
    )