import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1200, 1500, 1800, 1700, 2100]

# Line chart
plt.plot(months, sales, marker="o", linestyle="-", label="Sales")

# Title and labels
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

# Grid
plt.grid(True, linestyle="--", alpha=0.6)

# Legend
plt.legend()

# Display graph
plt.show()