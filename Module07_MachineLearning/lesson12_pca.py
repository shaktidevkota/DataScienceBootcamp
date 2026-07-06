import pandas as pd

from sklearn.decomposition import PCA

# Dataset
data = {
    "Math": [80, 85, 90, 70, 60],
    "Science": [82, 86, 91, 72, 61],
    "English": [78, 84, 89, 69, 59]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# PCA Model
pca = PCA(n_components=2)

# Transform data
reduced_data = pca.fit_transform(df)

print("\nReduced Data:")
print(reduced_data)