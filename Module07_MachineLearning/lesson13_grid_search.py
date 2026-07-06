import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier

# Dataset
data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8],
    "Passed": [0,0,0,0,1,1,1,1]
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

# Model
model = RandomForestClassifier(random_state=42)

# Hyperparameters
params = {
    "n_estimators": [10, 50, 100],
    "max_depth": [2, 3, 4]
}

# Grid Search
grid = GridSearchCV(
    estimator=model,
    param_grid=params,
    cv=3
)

grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)