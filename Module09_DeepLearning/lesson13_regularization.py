from sklearn.linear_model import Ridge, Lasso
from sklearn.datasets import make_regression

# Create sample dataset
X, y = make_regression(
    n_samples=100,
    n_features=10,
    noise=20,
    random_state=42
)

# L2 Regularization
ridge = Ridge(alpha=1.0)
ridge.fit(X, y)

# L1 Regularization
lasso = Lasso(alpha=1.0)
lasso.fit(X, y)

print("Ridge Coefficients")
print(ridge.coef_)

print("\nLasso Coefficients")
print(lasso.coef_)