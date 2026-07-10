import pandas as pd

from catboost import CatBoostClassifier

# Dataset
data = {
    "Age": [20, 25, 30, 35, 40, 45],
    "Income": [20000, 30000, 40000, 50000, 60000, 70000],
    "Approved": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Approved"]

# Model
model = CatBoostClassifier(
    iterations=100,
    learning_rate=0.1,
    random_seed=42,
    verbose=False
)

# Train
model.fit(X, y)

# Predict
prediction = model.predict([[28, 35000]])

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")