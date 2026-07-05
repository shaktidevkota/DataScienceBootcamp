import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "Passed": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# KNN Model
model = KNeighborsClassifier(n_neighbors=3)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test.values)

print("Accuracy:", accuracy_score(y_test, predictions))