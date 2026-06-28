import pandas as pd

data = {
    "Height_cm": [170, 165, 180, 175],
    "Weight_kg": [65, 55, 80, 72]
}

df = pd.DataFrame(data)

# Convert height to meters
df["Height_m"] = df["Height_cm"] / 100

# Create BMI
df["BMI"] = df["Weight_kg"] / (df["Height_m"] ** 2)

print(df)