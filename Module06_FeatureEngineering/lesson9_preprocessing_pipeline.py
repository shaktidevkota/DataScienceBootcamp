import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_data():
    data = {
        "Employee_ID": [101, 102, 103, 104, 105],
        "Name": ["  Alice Smith ", "Bob Jones...", "charlie brown", "David!", "Eva"],
        "Join_Date": [
            "2021-01-15",
            "2022/03/20",
            "14-05-2020",
            "2023-11-02",
            np.nan,
        ],
        "Salary": [50000, 60000, np.nan, 80000, 65000],
        "Loan_Amount": [5000, np.nan, 12000, 0, 7000],
        "Department": ["HR", "Engineering", "HR", "Sales", np.nan],
    }
    return pd.DataFrame(data)


def main():
    # Load DataFrame
    df = load_data()

    # Handle missing values
    df["Join_Date"] = df["Join_Date"].fillna("2023-01-01")
    df["Department"] = df["Department"].fillna("Unknown")

    # Clean text
    df["Name"] = (
        df["Name"]
        .astype(str)
        .str.strip()
        .str.replace(r"[^\w\s]", "", regex=True)
        .str.title()
    )

    # Convert date column
    df["Join_Date"] = pd.to_datetime(df["Join_Date"], format="mixed")

    # Create Loan_Ratio
    temp_salary = df["Salary"].fillna(df["Salary"].median())
    temp_loan = df["Loan_Amount"].fillna(0)
    df["Loan_Ratio"] = temp_loan / (temp_salary + 1)

    # Extract Year
    df["Join_Year"] = df["Join_Date"].dt.year

    # One-hot encode Department & Scale numeric columns
    numeric_features = ["Salary", "Loan_Amount", "Loan_Ratio", "Join_Year"]
    categorical_features = ["Department"]

    num_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    cat_pipeline = Pipeline(
        steps=[
            (
                "onehot",
                OneHotEncoder(handle_unknown="ignore", sparse_output=False),
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, numeric_features),
            ("cat", cat_pipeline, categorical_features),
        ],
        remainder="passthrough",
    )

    processed_array = preprocessor.fit_transform(df)

    encoded_cat_names = (
        preprocessor.named_transformers_["cat"]
        .named_steps["onehot"]
        .get_feature_names_out(categorical_features)
    )
    all_feature_names = numeric_features + list(encoded_cat_names) + ["Name"]

    df_processed = pd.DataFrame(
        processed_array, columns=all_feature_names + ["Employee_ID", "Join_Date"]
    )

    # Drop unnecessary columns
    columns_to_drop = ["Employee_ID", "Join_Date"]
    df_final = df_processed.drop(columns=columns_to_drop)

    print(df_final.to_string())


if __name__ == "__main__":
    main()