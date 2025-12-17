import os
from pathlib import Path

import duckdb
import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from sqlalchemy import create_engine

from .schema import ProductSchema, ProductSchemaKPI


def load_settings():
    """Loads database connection settings from a .env file.

    This function reads the .env file in the current working directory to
    load essential database credentials and connection information.

    Returns:
        dict: A dictionary containing the database settings (host, user,
            password, database name, and port).
    """
    dotenv_path = Path.cwd() / ".env"
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_pass": os.getenv("POSTGRES_PASSWORD"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_port": os.getenv("POSTGRES_PORT"),
    }
    return settings


@pa.check_output(ProductSchema)
def run_query(query: str) -> pd.DataFrame:
    """Executes a SQL query and validates the output against a Pandera schema.

    This function establishes a connection to the database using the loaded
    settings, runs the provided SQL query, and fetches the results into a
    pandas DataFrame. The output DataFrame is then validated against the
    `ProductSchema` to ensure data quality and integrity before further
    processing.

    Args:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: A DataFrame containing the query results, validated
            against the `ProductSchema`.

    Raises:
        pa.errors.SchemaError: If the DataFrame loaded from the database
            fails validation against the `ProductSchema`.
    """

    settings = load_settings()

    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
        df_crm = pd.read_sql(query, conn)

    return df_crm


@pa.check_input(ProductSchema)
@pa.check_output(ProductSchemaKPI)
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Applies business logic and transformations to the product DataFrame.

    This function enriches the input DataFrame by:
    1.  Calculating the total inventory value for each product.
    2.  Normalizing the product category names to lowercase.
    3.  Determining product availability based on quantity.

    Args:
        df (pd.DataFrame): The input DataFrame containing validated product
            data.

    Returns:
        pd.DataFrame: The transformed DataFrame, ready for loading or further
            analysis.
    """
    df["inventory_total_value"] = df["quantity"] * df["price"]
    df["category_normalized"] = df["category"].str.lower()
    df["availability"] = df["quantity"] > 0

    return df


@pa.check_input(ProductSchemaKPI, lazy=True)
def load_to_duckdb(df: pd.DataFrame, table_name: str, db_file: str = "my_duckdb.db"):
    """
    Carrega o DataFrame no DuckDB, criando ou substituindo a tabela especificada.

    Args:
        df: DataFrame do Pandas para ser carregado no DuckDB.
        table_name: Nome da tabela no DuckDB onde os dados serão inseridos.
        db_file: Caminho para o arquivo DuckDB. Se não existir, será criado.
    """
    con = duckdb.connect(database=db_file, read_only=False)
    con.register("df_temp", df)
    con.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df_temp")
    con.close()


if __name__ == "__main__":

    query = "SELECT * FROM products_bronze"
    try:
        df_crm = run_query(query=query)
        df_crm_kpi = transform(df_crm)
        print("Validation successful! Data is clean.")
        print(df_crm_kpi)
    except pa.errors.SchemaError as e:
        print("Data validation failed!")
        # The error object contains a 'failure_cases' DataFrame
        # with the specific rows that failed validation.
        print("Failure cases:")
        print(e.failure_cases)

    with open("inferred_schema.json", "w") as file:
        file.write(df_crm_kpi.to_json())

    load_to_duckdb(df=df_crm_kpi, table_name="table_kpi")
