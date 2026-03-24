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
    files = glob.glob(os.path.join(RAW_FOLDER, "*.json"))

    if not files:
        raise FileNotFoundError("No raw JSON files found")

    latest_file = max(files, key=os.path.getctime)
    return latest_file


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
        df = df[["id", "title", "price", "category", "rating", "stock"]]

        df = df.rename(columns={
            "title": "product_name"
        })

        df = df.fillna(0)

        logger.info("Data cleaned successfully")
        return df

    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
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
