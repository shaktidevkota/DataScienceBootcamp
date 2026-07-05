import pandas as pd

from sklearn.cluster import KMeans

# Dataset
data = {
    "Age": [20, 21, 22, 45, 46, 47],
    "Spending": [200, 250, 220, 5000, 5200, 5100]
}

df = pd.DataFrame(data)

X = df[["Age", "Spending"]]

# KMeans Model
model = KMeans(
    n_clusters=2,
    random_state=42
)

# Train and assign clusters
df["Cluster"] = model.fit_predict(X)

print(df)