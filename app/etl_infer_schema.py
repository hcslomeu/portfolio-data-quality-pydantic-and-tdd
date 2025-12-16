"""
Infers a Pandera schema from the 'products_bronze' table and saves it.

This script connects to the database, retrieves all data from the
'products_bronze' table, and uses Pandera's `infer_schema` function to
generate a data schema based on the table's structure and contents. The
resulting schema is then written to a Python file named 'schema_crm.py' in the
project's root directory. This is useful for bootstrapping data validation
rules.
"""

import os
from pathlib import Path

import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from sqlalchemy import create_engine


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


def run_query(query: str) -> pd.DataFrame:
    """Executes a SQL query and returns the results as a pandas DataFrame.

    This function establishes a connection to the database using the loaded
    settings, runs the provided SQL query, and fetches the results into a

    pandas DataFrame. No validation is performed at this stage.

    Args:
        query (str): The SQL query to execute.

    Returns:
        pd.DataFrame: A DataFrame containing the query results.
    """

    settings = load_settings()

    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
        df_crm = pd.read_sql(query, conn)

    return df_crm


if __name__ == "__main__":

    query = "SELECT * FROM products_bronze"
    df_crm = run_query(query=query)

    schema_crm = pa.infer_schema(df_crm)

    with open(
        "schema_crm.py",
        "w",
        encoding="utf-8",
    ) as file:
        file.write(schema_crm.to_script())

    print(schema_crm)
