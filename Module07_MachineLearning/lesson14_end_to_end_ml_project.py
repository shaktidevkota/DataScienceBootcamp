import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = {
    "Age":[25,45,22,35,28,40,30,50],
    "Income":[35000,70000,18000,50000,25000,65000,40000,80000],
    "Credit_Score":[700,750,500,680,550,720,650,800],
    "Loan_Amount":[5000,10000,8000,7000,9000,12000,6000,15000],
    "Approved":[1,1,0,1,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[["Age","Income","Credit_Score","Loan_Amount"]]

y = df["Approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

new_customer = [[32, 55000, 720, 8000]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")
