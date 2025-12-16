import pandas as pd
import pytest

from app.etl import transform


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Fixture to create a sample DataFrame for testing."""
    data = {
        "id_prod": [1, 2, 3],
        "name_prod": ["Product A", "Product B", "Product C"],
        "quantity": [10, 0, 5],
        "price": [2.5, 10.0, 0.0],
        "category": ["Category A", "CATEGORY B", "Category C"],
    }
    return pd.DataFrame(data)


def test_inventory_total_value_calculation(sample_dataframe):
    """
    Test the calculation of the 'inventory_total_value' column.
    """
    # Use .copy() to ensure the original fixture is not modified
    transformed_df = transform(sample_dataframe.copy())
    expected_values = pd.Series([25.0, 0.0, 0.0], name="inventory_total_value")
    pd.testing.assert_series_equal(
        transformed_df["inventory_total_value"], expected_values
    )


def test_category_normalization(sample_dataframe):
    """
    Test the normalization of the 'category' column to lowercase.
    """
    # Use .copy() to ensure the original fixture is not modified
    transformed_df = transform(sample_dataframe.copy())
    expected_values = pd.Series(
        ["category a", "category b", "category c"], name="category_normalized"
    )
    pd.testing.assert_series_equal(
        transformed_df["category_normalized"], expected_values
    )


def test_availability_calculation(sample_dataframe):
    """
    Test the calculation of the 'availability' column.
    """
    # Use .copy() to ensure the original fixture is not modified
    transformed_df = transform(sample_dataframe.copy())
    expected_values = pd.Series([True, False, True], name="availability")
    pd.testing.assert_series_equal(transformed_df["availability"], expected_values)
