import os
from pathlib import Path

import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from schema import ProductSchema
from sqlalchemy import create_engine


def load_settings():
    """Load DB settings from .env file"""
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

    settings = load_settings()

    connection_string = f"postgresql://{settings['db_user']}:{settings['db_pass']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"

    engine = create_engine(connection_string)

    with engine.connect() as conn, conn.begin():
        df_crm = pd.read_sql(query, conn)

    return df_crm


if __name__ == "__main__":

    query = "SELECT * FROM products_bronze"
    try:
        df_crm = run_query(query=query)
        print("Validation successful! Data is clean.")
        print(df_crm)
    except pa.errors.SchemaError as e:
        print("Data validation failed!")
        # The error object contains a 'failure_cases' DataFrame
        # with the specific rows that failed validation.
        print("Failure cases:")
        print(e.failure_cases)
