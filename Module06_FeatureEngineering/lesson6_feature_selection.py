import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104],  # Unique identifier for each employee
    "Name": ["Ram", "Shyam", "Hari", "Sita"],
    "Age": [20, 21, 22, 23],
    "Experience": [1, 2, 3, 4],
    "Salary": [30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

df_selected = df.drop(columns=["Name"])

print("\nSelected Features")
print(df_selected)