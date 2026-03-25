import requests
import json
import os
from datetime import datetime

from scripts.config_loader import load_config
from scripts.logger import setup_logger

config = load_config()
logger = setup_logger()

USERS_API = config["api"]["users_url"]
RAW_FOLDER = config["paths"]["raw_data"]


def fetch_users():
    try:
        logger.info("Fetching users data...")

        response = requests.get(USERS_API)
        response.raise_for_status()

        data = response.json()
        return data["users"]

    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        return None


def save_users(data):
    try:
        os.makedirs(RAW_FOLDER, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(RAW_FOLDER, f"users_{timestamp}.json")

        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        logger.info(f"Users data saved at {file_path}")

    except Exception as e:
        logger.error(f"Error saving users data: {e}")


def main():
    logger.info("Starting users ingestion...")

    data = fetch_users()

    if data:
        logger.info(f"Users fetched: {len(data)}")
        save_users(data)
    else:
        logger.error("Users ingestion failed")


if __name__ == "__main__":
    main()
