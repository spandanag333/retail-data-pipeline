import pandas as pd
import sqlite3
import os

from scripts.config_loader import load_config

# Load config
config = load_config()

PROCESSED_FILE = config["paths"]["processed_data"]
DB_PATH = config["database"]["name"]

# Ensure DB directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)


def load_data():
    try:
        df = pd.read_csv(PROCESSED_FILE)
        return df

    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None


def create_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        return conn

    except Exception as e:
        print(f"Error connecting to DB: {e}")
        return None


def load_to_db(df, conn):
    try:
        df.to_sql("products", conn, if_exists="replace", index=False)
        print("Data loaded into database successfully")

    except Exception as e:
        print(f"Error loading data into DB: {e}")


def run_sample_query(conn):
    try:
        query = """
        SELECT category, AVG(price) as avg_price 
        FROM products 
        GROUP BY category;
        """

        result = pd.read_sql(query, conn)

        print("\nSample Query Result:")
        print(result)

    except Exception as e:
        print(f"Error running query: {e}")


def main():
    print("Starting data load process...")

    df = load_data()

    if df is None:
        print("Data load failed ❌")
        return

    print(f"Rows loaded to DB: {len(df)}")

    conn = create_connection()

    if conn is None:
        print("DB connection failed ❌")
        return

    load_to_db(df, conn)
    run_sample_query(conn)

    conn.close()

    print("Data load completed successfully ✅")


if __name__ == "__main__":
    main()