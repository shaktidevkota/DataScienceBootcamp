import pandas as pd

data = {
    'Name': ['shakti', 'raj', 'devkota', 'pravin', 'rabin'],
    'Age': [25, 30, 35, 40, 22],
    'Department': ['HR', 'Engineering', 'Data', 'Engineering', 'HR'],
    'Salary': [60000.0, 85000.0, 95000.0, 120000.0, 58000.0]
}
df = pd.DataFrame(data)

# print(df)
print("--- 1. df ---")
print(df)
print("\n")

# print(df.shape)
print("--- 2. df.shape ---")
print(df.shape)
print("\n")

# print(df.columns)
print("--- 3. df.columns ---")
print(df.columns)
print("\n")

# print(df.dtypes)
print("--- 4. df.dtypes ---")
print(df.dtypes)
print("\n")

# print(df.info())
print("--- 5. df.info() ---")
df.info()
print("\n")

# print(df.describe())
print("--- 6. df.describe() ---")
print(df.describe())
print("\n")

# print(df.describe(include="all"))
print("--- 7. df.describe(include='all') ---")
print(df.describe(include="all"))
print("\n")