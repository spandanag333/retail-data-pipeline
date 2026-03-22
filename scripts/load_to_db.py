import pandas as pd
import sqlite3
import os

# Paths
PROCESSED_FILE = "C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/data/processed/products_cleaned.csv"
DB_PATH = "C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/data/products.db"


def load_data():
    # Read cleaned CSV
    df = pd.read_csv(PROCESSED_FILE)
    return df


def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def load_to_db(df, conn):
    # Load into SQL table
    df.to_sql("products", conn, if_exists="replace", index=False)
    print("Data loaded into database successfully")


def run_sample_query(conn):
    query = "SELECT category, AVG(price) as avg_price FROM products GROUP BY category;"
    
    result = pd.read_sql(query, conn)
    
    print("\nSample Query Result:")
    print(result)


def main():
    print("Starting data load process...")

    df = load_data()

    print(f"Rows loaded to DB: {len(df)}")
    
    conn = create_connection()

    load_to_db(df, conn)
    run_sample_query(conn)

    conn.close()

    print("Data load completed successfully ✅")


if __name__ == "__main__":
    main()