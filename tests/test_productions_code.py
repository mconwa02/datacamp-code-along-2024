import pytest
from pandas import DataFrame

from production_code import max_customer_account_balance, customers_mean_age


@pytest.fixture
def test_df():
    return DataFrame(
        data={"balance": [100, 200, 300, 400, 500], "age": [30, 40, 50, 60, 70]}
    )


def test_max_customer_account_balance(test_df):
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
