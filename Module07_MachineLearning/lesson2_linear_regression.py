import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
    "Salary": [30000, 35000, 42000, 50000, 58000, 65000, 72000, 80000]
}

df = pd.DataFrame(data)

# Features and Target
X = df[["Experience"]]
y = df["Salary"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("Predicted Salaries:")
print(predictions)

print("\nActual Salaries:")
print(y_test.values)