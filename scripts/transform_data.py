import pandas as pd
import json
import os
import glob

from scripts.config_loader import load_config
from scripts.logger import setup_logger

# Load config + logger
config = load_config()
logger = setup_logger()

RAW_FOLDER = config["paths"]["raw_data"]
OUTPUT_FILE = config["paths"]["processed_data"]
OUTPUT_DIR = os.path.dirname(OUTPUT_FILE)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_latest_file():
    files = glob.glob(os.path.join(RAW_FOLDER, "products_*.json"))

    if not files:
        raise FileNotFoundError("No product JSON files found")

    latest_file = max(files, key=os.path.getctime)
    return latest_file

def get_latest_users_file():
    files = glob.glob(os.path.join(RAW_FOLDER, "users_*.json"))

    if not files:
        raise FileNotFoundError("No users JSON files found")

    latest_file = max(files, key=os.path.getctime)
    return latest_file


def load_users_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        df = pd.DataFrame(data)
        logger.info("Users data loaded successfully")
        return df

    except Exception as e:
        logger.error(f"Error loading users data: {e}")
        return None


def transform_data(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)

        df = pd.DataFrame(data)
        logger.info("Raw data loaded into DataFrame")
        return df

    except Exception as e:
        logger.error(f"Error reading file: {e}")
        return None


def clean_data(df):
    try:
        # Select columns
        df = df[["id", "title", "price", "category", "rating", "stock"]]

        # Rename
        df = df.rename(columns={"title": "product_name"})

        # Handle missing
        df = df.fillna(0)

        # STEP A: Simulate relationship
        df["user_id"] = df["id"] % 30

        # STEP B: Load users
        users_file = get_latest_users_file()
        users_df = load_users_data(users_file)

        if users_df is None:
            logger.error("Users data not available for merge")
            return df

        # STEP C: Merge
        merged_df = df.merge(
            users_df[["id", "firstName"]],
            left_on="user_id",
            right_on="id",
            how="left"
        )

        # STEP D: Cleanup columns
        merged_df.rename(columns={"firstName": "customer_name"}, inplace=True)

        merged_df.drop(columns=["id_y"], inplace=True)
        merged_df.rename(columns={"id_x": "id"}, inplace=True)

        logger.info("Data merged successfully")

        return merged_df

    except Exception as e:
        logger.error(f"Error in cleaning/merging data: {e}")
        return None


def save_data(df):
    try:
        df.to_csv(OUTPUT_FILE, index=False)
        logger.info(f"Clean data saved to {OUTPUT_FILE}")

    except Exception as e:
        logger.error(f"Error saving file: {e}")


def main():
    logger.info("Starting transformation pipeline...")

    try:
        file_path = get_latest_file()
        logger.info(f"Processing file: {file_path}")

        df = transform_data(file_path)

        if df is None:
            logger.error("Transformation failed")
            return

        logger.info(f"Rows before cleaning: {len(df)}")

        df_clean = clean_data(df)

        if df_clean is None:
            logger.error("Cleaning failed")
            return

        logger.info(f"Rows after cleaning: {len(df_clean)}")

        save_data(df_clean)

        logger.info("Transformation completed successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    main()
