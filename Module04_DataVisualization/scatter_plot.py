import matplotlib.pyplot as plt

# Data
experience = [1, 2, 3, 4, 5, 6, 7]
salary = [30000, 35000, 42000, 50000, 58000, 65000, 72000]

# Create scatter plot
plt.scatter(experience, salary, color="green", s=80)

# Add Title and Labels
plt.title("Salary vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

# Enable Grid
plt.grid(True)

# Adjust layout to prevent truncation
plt.tight_layout()

# Save the plot
plt.savefig("salary_vs_experience.png")

plt.show()