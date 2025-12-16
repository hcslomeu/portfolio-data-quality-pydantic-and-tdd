import pandera.pandas as pa
from pandera import Field

email_regex = r"[^@]+@[^@]+\.[^@]+"


class ProductSchemaEmail(pa.DataFrameModel):
    """Schema for validating the structure and quality of product data.

    This class leverages the Pandera `DataFrameModel` to define a strict data
    contract for product-related DataFrames. It serves as a centralized,
    declarative, and self-documenting guide to the expected data types,
    constraints, and format of product data.

    By validating DataFrames against this schema, we ensure data integrity
    before processing, preventing common data quality issues.

    Attributes:
        id_prod (int): The unique identifier for the product.
            The value must be between 1 and 10 (inclusive).
        name_prod (str): The name of the product.
        quantity (int): The available stock quantity of the product.
            Must be between 20 and 200.
        price (float): The price of the product. Must be between 5.0 and 120.0.
        category (str): The product category.
        index (int): The DataFrame index, which must be between 0 and 9.
        email (str): The email of the customer.

    Config:
        coerce (bool): If True, automatically attempts to cast DataFrame
            columns to the data types specified in the schema.
        strict (bool): If True, the DataFrame must contain exactly the columns
            specified in the schema; no more, no less.
        unique (list[str]): Ensures that all rows are unique across the
            combination of the specified columns.
    """

    id_prod: int = Field(ge=1, le=10, description="Unique product identifier")
    name_prod: str = Field(description="Name of the product")
    quantity: int = Field(
        ge=20, le=200, description="Available quantity of the product"
    )
    price: float = Field(ge=5.0, le=120.0, description="Price of the product")
    category: str = Field(description="Category of the product")
    email: str = Field(regex=email_regex, description="Customer emails")

    # Defines the DataFrame index constraints
    index: pa.typing.Index[int] = Field(ge=0, le=9, description="Row index")

    class Config:
        """
        Configuration class for the Pandera schema.
        """

        # Coerce data to the specified types
        coerce: bool = True
        # Do not fail on columns present in the DataFrame but not in the schema
        strict: bool = True
        # Name of the schema for identification
        name: str = "ProductSchema_DataFrameModel"
        # Report all duplicate rows
        unique: list[str] = ["id_prod", "name_prod", "quantity", "price", "category"]
        # Allow duplicate column names
        unique_column_names: bool = False
        # Do not add columns missing from the DataFrame
        add_missing_columns: bool = False
