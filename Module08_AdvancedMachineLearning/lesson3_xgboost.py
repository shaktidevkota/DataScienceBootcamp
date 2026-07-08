import pandas as pd

from xgboost import XGBClassifier

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
model = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

# Train
model.fit(X, y)

# Predict
prediction = model.predict([[28, 35000]])

print("Prediction:", prediction)