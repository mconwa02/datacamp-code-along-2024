import pandas as pd
import pytest
from pandas import DataFrame

from production_code import (
    max_customer_account_balance,
    customers_mean_age,
    creating_features_banking_data,
    marital_status_groups,
)


@pytest.fixture
def test_df():
    return DataFrame(
        data={
            "balance": [100, 200, 300, 400, 500],
            "age": [30, 40, 50, 60, 70],
        }
    )


def test_max_customer_account_balance():
    """Test the max_customer_account_balance function."""
    test_df = DataFrame(data={"balance": [100, 200, 300, 400, 500]})
    test_df = max_customer_account_balance(test_df)
    actual = test_df["balance_max"].iloc[0]
    expected = 500
    assert "balance_max" in test_df.columns
    assert actual == expected


def test_customers_mean_age(test_df):
    """Test the customers_mean_age function."""
    test_df = DataFrame(data={"age": [30, 40, 50, 60, 70]})
    test_df = customers_mean_age(test_df)
    actual = test_df["age_mean"].iloc[0]
    expected = 50
    assert "age_mean" in test_df.columns
    assert actual == expected


def test_creating_features_banking_data(test_df):
    actual_df = creating_features_banking_data(test_df)
    expected_df = DataFrame(
        data={
            "balance": [100, 200, 300, 400, 500],
            "age": [30, 40, 50, 60, 70],
            "balance_max": [500, 500, 500, 500, 500],
            "age_mean": [50.0, 50.0, 50.0, 50.0, 50.0],
        }
    )
    pd.testing.assert_frame_equal(actual_df, expected_df)


def test_marital_status_groups(test_df):
    test_df["marital"] = ["M", "M", "S", "S", "W"]
    actual_df = marital_status_groups(test_df)
    expected_df = DataFrame(
        data={
            "balance_max": [200.0, 400.0, 500.0],
            "age_mean": [35.0, 55.0, 70.0],
        },
        index=["M", "S", "W"],
    )
    expected_df.index.name = "marital"
    pd.testing.assert_frame_equal(actual_df, expected_df)
