from pandas import DataFrame, Series

from sample_code import df


def max_customer_account_balance(df: DataFrame) -> DataFrame:
    """Adds a column with the maximum account balance to the DataFrame."""
    df["balance_max"] = df["balance"].max()
    return df


def customers_mean_age(df: DataFrame) -> DataFrame:
    """Adds a column with the mean age of all customers to the DataFrame."""
    df["age_mean"] = df["age"].mean()
    return df


def gb_max_customer_account_balance(df: DataFrame) -> DataFrame:
    """Adds a column with the maximum account balance to the DataFrame."""
    df["balance_max"] = df["balance"].max()
    return df["balance_max"].iloc[0]


def gb_customers_mean_age(df: DataFrame) -> DataFrame:
    """Adds a column with the mean age of all customers to the DataFrame."""
    df["age_mean"] = df["age"].mean()
    return df["age_mean"].iloc[0]


def marital_status_groups(df: DataFrame) -> DataFrame:
    return df.groupby("marital").apply(
        lambda x: Series(
            {
                "balance_max": gb_max_customer_account_balance(x),
                "age_mean": gb_customers_mean_age(x),
            }
        ),
        include_groups=False,
    )


def creating_features_banking_data(df):
    return df.pipe(max_customer_account_balance).pipe(customers_mean_age)


if __name__ == "__main__":
    banking_customers_df = creating_features_banking_data(df)
    print(banking_customers_df.head())
    print(marital_status_groups(df))
