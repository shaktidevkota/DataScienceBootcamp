import pandas as pd

data = {
    "EmployeeID": [101, 102, 102, 103, 104, 104, 105],
    "Name": ["Ram", "Shyam", "Shyam", "Hari", "Sita", "Sita", "Gita"],
    "Department": ["HR", "IT", "IT", "Finance", "HR", "HR", "Marketing"],
    "Salary": [50000, 60000, 60000, 70000, 65000, 65000, 72000],
}

df = pd.DataFrame(data)

print("--- 1. Original Dataset ---")
print(df)
print("\n")

print("--- 2. Duplicate Rows (Boolean Mask) ---")
print(df.duplicated())
print("\n")

print("--- 3. Count of Duplicate Rows ---")
print(df.duplicated().sum())
print("\n")

print("--- 4. Subset showing only the duplicate rows ---")
print(df[df.duplicated()])
print("\n")

print("--- 5. Dataset after removing duplicates (Keep First) ---")
print(df.drop_duplicates())
print("\n")

print("--- 6. Dataset after removing duplicates (Keep Last) ---")
print(df.drop_duplicates(keep="last"))
print("\n")

print("--- 7. Dataset after dropping ALL versions of duplicates ---")
print(df.drop_duplicates(keep=False))
print("\n")

print("--- 8. Duplicates based only on EmployeeID ---")
print(df[df.duplicated(subset=["EmployeeID"])])