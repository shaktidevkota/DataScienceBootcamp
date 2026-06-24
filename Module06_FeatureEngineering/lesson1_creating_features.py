import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita"],
    "Age": [20, 25, 30, 35],
    "Salary": [30000, 50000, 70000, 90000],
    "Experience": [1, 3, 5, 8]
}

df = pd.DataFrame(data)

print(df)

df["Salary_per_Experience"] = df["Salary"] / df["Experience"]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[0, 24, 34, 100],
    labels=["Young", "Adult", "Senior"]
)

df["High_Salary"] = df["Salary"] >= 60000

def experience_level(exp):
    if exp < 2:
        return "Beginner"
    elif exp < 5:
        return "Intermediate"
    else:
        return "Experienced"

df["Experience_Level"] = df["Experience"].apply(experience_level)
print(df)