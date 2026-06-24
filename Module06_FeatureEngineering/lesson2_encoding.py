import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Name": ["Ram", "Hari", "Sita", "Gita", "Shyam"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Education": ["Bachelor", "Master", "Bachelor", "PhD", "Master"]
}

df = pd.DataFrame(data)

le = LabelEncoder()
df["Education"] = le.fit_transform(df["Education"])

df = pd.get_dummies(df, columns=["Department"], dtype=int)

print(df)