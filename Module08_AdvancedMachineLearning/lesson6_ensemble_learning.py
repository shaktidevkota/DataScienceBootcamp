
import pandas as pd

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Dataset
data = {
    "Age": [20,25,30,35,40,45],
    "Income": [20000,30000,40000,50000,60000,70000],
    "Approved": [0,0,1,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Age", "Income"]]
y = df["Approved"]

# Individual Models
lr = LogisticRegression()
dt = DecisionTreeClassifier(random_state=42)
knn = KNeighborsClassifier()

# Voting Ensemble
model = VotingClassifier(
    estimators=[
        ("lr", lr),
        ("dt", dt),
        ("knn", knn)
    ],
    voting="hard"
)

model.fit(X, y)

prediction = model.predict([[28,35000]])

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")