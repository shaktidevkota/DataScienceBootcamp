import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Experience": [1, 2, 3, 4, 5, 6, 7],
    "Salary": [30000, 35000, 42000, 50000, 58000, 65000, 72000]
}

df = pd.DataFrame(data)

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    s=100
)

plt.title("Experience vs Salary")

plt.show()