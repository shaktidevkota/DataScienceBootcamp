import pandas as pd

data = {
    "Income": [50000, 60000, 75000, 90000],
    "Loan": [25000, 20000, 50000, 30000]
}

df = pd.DataFrame(data)

# Create Loan Ratio
df["Loan_Ratio"] = df["Loan"] / df["Income"]

print(df)