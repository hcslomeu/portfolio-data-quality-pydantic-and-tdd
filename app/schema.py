import pandera.pandas as pa
from pandera import Field


class ProductSchema(pa.DataFrameModel):
    """
    Schema for product data validation using Pandera's DataFrameModel.

    This class defines the expected structure and constraints for a DataFrame
    containing product information. It validates data types, value ranges,
    and nullability for each column.
    """

    id_prod: int = Field(ge=1, le=10, description="Unique product identifier")
    name_prod: str = Field(description="Name of the product")
    quantity: int = Field(
        ge=20, le=200, description="Available quantity of the product"
    )
    price: float = Field(ge=5.0, le=120.0, description="Price of the product")
    category: str = Field(description="Category of the product")

    # Defines the DataFrame index constraints
    index: pa.typing.Index[int] = Field(ge=0, le=9, description="Row index")

    class Config:
        """
        Configuration class for the Pandera schema.
        """

        # Coerce data to the specified types
        coerce: bool = True
        # Do not fail on columns present in the DataFrame but not in the schema
        strict: bool = False
        # Name of the schema for identification
        name: str = "ProductSchema_DataFrameModel"
        # Report all duplicate rows
        unique: list[str] = ["id_prod", "name_prod", "quantity", "price", "category"]
        # Allow duplicate column names
        unique_column_names: bool = False
        # Do not add columns missing from the DataFrame
        add_missing_columns: bool = False
