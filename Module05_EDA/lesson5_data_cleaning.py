import pandas as pd
import numpy as np

data = {
    "Name": [" Ram", "shyam ", "HARI", "sita", None],
    "Age": ["20", "21", "Twenty Two", "23", "24"],
    "Salary": ["50000", "$60,000", "70000", "80000", None],
    "Department": ["HR", "it", "Finance", "HR", "finance"]
}

df = pd.DataFrame(data)

print("--- 1. Original Dataset ---")
print(df)

print("\n--- 2. Data Types Before Cleaning ---")
print(df.dtypes)

df['Name'] = df['Name'].str.strip()

df['Department'] = df['Department'].str.upper()

df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df['Salary'] = df['Salary'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
df['Salary'] = pd.to_numeric(df['Salary'])

df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\n--- 3. Data Types After Cleaning ---")
print(df.dtypes)

print("\n--- 4. Final Cleaned Dataset ---")
print(df)