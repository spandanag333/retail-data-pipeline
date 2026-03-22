import requests
import json
import os
from datetime import datetime

# API endpoint (DummyJSON - better than fake API)
API_URL = "https://dummyjson.com/products"

# Create folders if they don't exist
os.makedirs("C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/data/raw", exist_ok=True)
os.makedirs("C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/logs", exist_ok=True)


def fetch_data():
    try:
        print("Sending request to API...")
        
        # Send GET request to API
        response = requests.get(API_URL)
        
        # Raise error if request fails
        response.raise_for_status()
        
        # Convert response to JSON
        data = response.json()
        
        # Extract only product list (important)
        return data["products"]
    
    except Exception as e:
        log_error(str(e))
        return None


def save_data(data):
    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # File path
    file_path = f"C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/data/raw/products_{timestamp}.json"
    
    # Save JSON file
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Data saved successfully at {file_path}")


def log_error(error_msg):
    log_file = "C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/logs/error.log"
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] ERROR: {error_msg}\n")


def main():
    print("Starting data pipeline...")
    
    data = fetch_data()
    
    if data:
        print(f"Number of records fetched: {len(data)}")
        print("Sample record:", data[0])  # helps you understand structure
        
        save_data(data)
        print("Pipeline completed successfully ✅")
    
    else:
        print("Pipeline failed ❌ Check logs")


if __name__ == "__main__":
    main()