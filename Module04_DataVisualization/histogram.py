import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 62, 65, 67, 70, 72, 75,
         78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=6, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y", linestyle="--", alpha=0.6)

plt.show()