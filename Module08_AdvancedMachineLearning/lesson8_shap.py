import pandas as pd
import shap

from sklearn.ensemble import RandomForestClassifier

# Dataset
data = {
    "Age": [20,25,30,35,40,45],
    "Income": [20000,30000,40000,50000,60000,70000],
    "Credit_Score": [600,650,700,720,750,800],
    "Approved": [0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Age","Income","Credit_Score"]]
y = df["Approved"]

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# SHAP Explainer
explainer = shap.TreeExplainer(model)

# Calculate SHAP values
shap_values = explainer.shap_values(X)

# Summary Plot
shap.summary_plot(shap_values, X)