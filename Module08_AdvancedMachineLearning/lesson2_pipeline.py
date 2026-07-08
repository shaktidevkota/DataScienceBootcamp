import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Dataset
data = {
    "Age": [20, 25, 30, 35, 40, 45],
    "Income": [20000, 30000, 40000, 50000, 60000, 70000],
    "Approved": [0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Approved"]

# Create Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(random_state=42))
])

# Train
pipeline.fit(X, y)

# Predict
prediction = pipeline.predict([[28, 35000]])

print("Prediction:", prediction)