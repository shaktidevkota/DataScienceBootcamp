import pandas as pd
import matplotlib.pyplot as plt

# 1. Dataset Setup & Display
data = {
    "Employee": ["Ram", "Shyam", "Hari", "Sita", "Gita", "Pravin"],
    "Salary": [50000, 55000, 60000, 62000, 58000, 250000]
}

df = pd.DataFrame(data)
print("--- 1. Original Dataset ---")
print(df)
print("\n")

# 2. Display describe()
print("--- 2. Dataset Description ---")
print(df.describe())
print("\n")

# 3. Draw and save a box plot
# Note: saved to the current working directory as per guidelines
plt.boxplot(df['Salary'])
plt.title('Employee Salary Box Plot')
plt.ylabel('Salary ($)')
plt.savefig('salary_boxplot.png')
plt.close()

# 4. Calculate Q1, Q3, IQR, Lower Bound, Upper Bound
q1 = df['Salary'].quantile(0.25)
q3 = df['Salary'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("--- 4. Statistical Calculations ---")
print(f"Q1: {q1}")
print(f"Q3: {q3}")
print(f"IQR: {iqr}")
print(f"Lower Bound: {lower_bound}")
print(f"Upper Bound: {upper_bound}")
print("\n")

# 5. Display only the outliers
outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
print("--- 5. Outliers Identified ---")
print(outliers)
print("\n")

# 6. Remove the outliers
df_cleaned = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

# 7. Compare Means
mean_before = df['Salary'].mean()
mean_after = df_cleaned['Salary'].mean()

print("--- 7. Mean Comparison ---")
print(f"Mean before outlier removal: {mean_before:.2f}")
print(f"Mean after outlier removal: {mean_after:.2f}")