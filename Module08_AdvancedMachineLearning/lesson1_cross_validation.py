import pandas as pd

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

# Dataset
data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Passed": [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Hours_Studied"]]
y = df["Passed"]

# Model
model = RandomForestClassifier(random_state=42)

# Cross Validation
scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print("Scores:", scores)
print("Average Accuracy:", scores.mean())