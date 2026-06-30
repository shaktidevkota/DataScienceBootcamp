import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "Salary": [30000, 35000, 42000, 50000, 58000, 65000, 72000, 80000]
}

df = pd.DataFrame(data)

# Features (X)
X = df[["Experience"]]

# Target (y)
y = df["Salary"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)