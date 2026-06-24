import matplotlib.pyplot as plt

marks = [45, 50, 52, 55, 58, 60, 62, 65, 68, 70, 72, 75, 98]

plt.boxplot(marks)

plt.xticks([1], ["Students"])   # Set x-axis label

plt.title("Distribution of Student Marks")
plt.ylabel("Marks")

plt.grid(True, linestyle="--", alpha=0.7)

plt.show()