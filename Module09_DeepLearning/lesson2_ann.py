import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Dataset
data = {
    "Age": [20, 25, 30, 35, 40, 45],
    "Income": [20000, 30000, 40000, 50000, 60000, 70000],
    "Approved": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Approved"]

# Build ANN
model = Sequential([
    Dense(16, activation="relu", input_shape=(2,)),
    Dense(8, activation="relu"),
    Dense(1, activation="sigmoid")
])

# Compile
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

# Train
model.fit(
    X,
    y,
    epochs=50,
    verbose=1
)

# Prediction
prediction = model.predict([[28, 35000]])

print(prediction)