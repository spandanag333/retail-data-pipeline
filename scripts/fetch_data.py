import requests
import json
import os
from datetime import datetime

from scripts.config_loader import load_config
from scripts.logger import setup_logger

# Load config
config = load_config()
logger = setup_logger()

API_URL = config["api"]["url"]
RAW_DATA_PATH = config["paths"]["raw_data"]


def fetch_data():
    try:
        logger.info("Sending request to API...")

        response = requests.get(API_URL)
        response.raise_for_status()

        data = response.json()

        logger.info("Data fetched successfully")
        return data["products"]

    except Exception as e:
        logger.error(f"Error fetching data: {e}")
        return None


def save_data(data):
    try:
        os.makedirs(RAW_DATA_PATH, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(RAW_DATA_PATH, f"products_{timestamp}.json")

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        logger.info(f"Data saved successfully at {file_path}")

    except Exception as e:
        logger.error(f"Error saving data: {e}")


def main():
    logger.info("Starting data ingestion pipeline...")

    data = fetch_data()

    if data:
        logger.info(f"Number of records fetched: {len(data)}")
        logger.info(f"Sample record: {data[0]}")

        save_data(data)

        logger.info("Pipeline completed successfully")

    else:
        logger.error("Pipeline failed ❌ Check logs")


if __name__ == "__main__":
    main()