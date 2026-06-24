import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")

# Count Plot
plt.figure(figsize=(6, 4))
sns.countplot(data=tips, x="day")
plt.title("1. Count Plot")
plt.show()

# Heatmap
plt.figure(figsize=(6, 4))
numeric_tips = tips.select_dtypes(include=["float64", "int64"])
correlation_matrix = numeric_tips.corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("2. Heatmap")
plt.show()

# Pair Plot
sns.pairplot(data=iris, hue="species")
plt.suptitle("3. Pair Plot", y=1.02)
plt.show()

# Violin Plot
plt.figure(figsize=(6, 4))
sns.violinplot(data=tips, x="day", y="total_bill", hue="smoker", split=True)
plt.title("4. Violin Plot")
plt.show()

# KDE Plot
plt.figure(figsize=(6, 4))
sns.kdeplot(data=tips, x="total_bill", fill=True)
plt.title("5. KDE Plot")
plt.show()