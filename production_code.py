from pandas import DataFrame

from sample_code import df


def max_customer_account_balance(df: DataFrame) -> DataFrame:
    """Adds a column with the maximum account balance to the DataFrame."""
    df["balance_max"] = df["balance"].max()
    return df


def customers_mean_age(df: DataFrame) -> DataFrame:
    """Adds a column with the mean age of all customers to the DataFrame."""
    df["age_mean"] = df["age"].mean()
    return df


# def filer_customer_items(df: DataFrame) -> DataFrame:
#     """ insert a good doc string"""
#     df["annual_duration_flat"] = [
#         item for sublist in df["annual_duration"].tolist() for item in sublist
#     ]
#     return df
#
#
# def join_customer_names(df: DataFrame) -> DataFrame:
#     """ insert a good doc string"""
#     df["campaign_limit_concat"] = (
#         "".join(str(item) for item in df["campaign_limit"].tolist()),
#     )
#     return df


def creating_features_banking_data(df):
    return (
        df.pipe(max_customer_account_balance).pipe(customers_mean_age)
        # todo fix broken pipe functions
        # .pipe(filer_customer_items)
        # .pipe(join_customer_names)
    )


if __name__ == "__main__":
    banking_customers_df = creating_features_banking_data(df)
    print(banking_customers_df.head())
