import pandas as pd

data = {"Marks": [45, 55, 65, 72, 88, 95]}

df = pd.DataFrame(data)

bins = [0, 50, 70, 90, 100]
labels = ["Fail", "Average", "Good", "Excellent"]

df["Grade"] = pd.cut(df["Marks"], bins=bins, labels=labels, include_lowest=True)

print(df)