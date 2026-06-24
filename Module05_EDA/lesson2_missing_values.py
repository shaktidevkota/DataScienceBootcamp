import pandas as pd
import numpy as np

# Provided dataset
data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita"],
    "Age": [20, np.nan, 22, 23, 24],
    "Salary": [50000, 60000, np.nan, 80000, 75000],
    "Department": ["HR", "IT", "HR", None, "Finance"]
}

df = pd.DataFrame(data)

# 1. Display the dataset
print("--- 1. Display the dataset ---")
print(df)
print("\n")

# 2. Show the missing-value matrix using isnull()
print("--- 2. Missing-value matrix using isnull() ---")
print(df.isnull())
print("\n")

# 3. Count missing values with isnull().sum()
print("--- 3. Count missing values with isnull().sum() ---")
print(df.isnull().sum())
print("\n")

# 4. Calculate the percentage of missing values
print("--- 4. Percentage of missing values (%) ---")
print((df.isnull().sum() / len(df)) * 100)
print("\n")

# 5. Create a version with missing rows removed
print("--- 5. Version with missing rows removed ---")
print(df.dropna())
print("\n")

# 6. Create a version with missing columns removed
print("--- 6. Version with missing columns removed ---")
print(df.dropna(axis=1))
print("\n")

# 7 & 8. Fill missing values and print final cleaned dataset
df_cleaned = df.copy()

# Fill Age using the mean (Excluding NaN, mean of 20, 22, 23, 24 is 22.25)
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].mean())

# Fill Salary using the median (Sorted values: 50k, 60k, 75k, 80k -> Median is 67500)
df_cleaned['Salary'] = df_cleaned['Salary'].fillna(df_cleaned['Salary'].median())

# Fill Department using the mode (Most frequent item is 'HR')
df_cleaned['Department'] = df_cleaned['Department'].fillna(df_cleaned['Department'].mode()[0])

print("--- 8. Final cleaned dataset ---")
print(df_cleaned)