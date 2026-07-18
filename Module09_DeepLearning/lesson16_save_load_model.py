from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

print("Model Trained!")

# Save model
joblib.dump(model, "iris_model.pkl")
print("Model Saved!")

# Load model
loaded_model = joblib.load("iris_model.pkl")

prediction = loaded_model.predict([[5.1, 3.5, 1.4, 0.2]])

print("Prediction:", prediction)