import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Create the initial DataFrame
data = {
    "Salary": [30000, 50000, 70000, 90000, 120000]
}
df = pd.DataFrame(data)

# Task 1: Apply MinMaxScaler
min_max_scaler = MinMaxScaler()
df["Salary_Normalized"] = min_max_scaler.fit_transform(df[["Salary"]])

# Task 2: Apply StandardScaler
standard_scaler = StandardScaler()
df["Salary_Standardized"] = standard_scaler.fit_transform(df[["Salary"]])

# Task 3: Compare
print(df)