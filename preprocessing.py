import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df.dropna(inplace=True)

    df.drop('customerID', axis=1, inplace=True)

    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    df = pd.get_dummies(df, drop_first=True)

    return df


if __name__ == "__main__":
    df = load_and_clean_data("data/raw/customers.csv")
    df.to_csv("data/processed/clean_data.csv", index=False)
    print("✅ Data cleaned & saved")
