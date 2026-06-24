import pandas as pd
import numpy as np

# 1. SIMULATE LOADING DATA (Saving your data to a CSV first)
data = {
    "name": ["Serina", "Alisha", "Shital", "Shakti"],
    "age": [20, 21, 22, 23],
    "marks": [80, 55, 90, 70]
}
pd.DataFrame(data).to_csv("student_records.csv", index=False)

# 2. THE PROJECT: LOAD AND ANALYZE
# Load the data
df = pd.read_csv("student_records.csv")

# Transform: Add the status column
df["status"] = np.where(df["marks"] >= 60, "Pass", "Fail")

# Analyze: Calculate key metrics
total_students = len(df)
average_mark = df["marks"].mean()
pass_rate = (df["status"] == "Pass").sum() / total_students * 100

# 3. GENERATE REPORT
print("=== STUDENT PERFORMANCE REPORT ===")
print("\nFinal Dataset:")
print(df.to_string(index=False))

print("\n=== SUMMARY STATISTICS ===")
print(f"Total Students: {total_students}")
print(f"Average Mark:   {average_mark:.1f}")
print(f"Passing Rate:   {pass_rate:.1f}%")

# 4. EXPORT RESULTS
df.to_csv("final_student_report.csv", index=False)
print("\n[Success] Report saved to 'final_student_report.csv'")