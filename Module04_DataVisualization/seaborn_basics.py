import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1200, 1500, 1800, 1700, 2100]
}

df = pd.DataFrame(data)

sns.lineplot(data=df, x="Month", y="Sales", marker="o")

plt.title("Monthly Sales")

plt.show()