import pandas as pd
import json
import os

# Path to raw data folder
RAW_FOLDER = "C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/data/raw"
PROCESSED_FOLDER = "C:/Users/spand/Desktop/Data Engineer/retail-data-pipeline/data/processed"

# Create processed folder
os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def get_latest_file():
    files = os.listdir(RAW_FOLDER)
    files = [f for f in files if f.endswith(".json")]
    
    latest_file = max(files)  # latest based on timestamp
    return os.path.join(RAW_FOLDER, latest_file)


def transform_data(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Convert JSON to DataFrame
    df = pd.DataFrame(data)
    return df


def clean_data(df):
    # Select useful columns
    df = df[["id", "title", "price", "category", "rating", "stock"]]
    
    # Rename columns
    df.rename(columns={
        "title": "product_name"
    }, inplace=True)
    
    # Handle missing values (if any)
    df.fillna(0, inplace=True)
    
    return df


def save_data(df):
    output_path = os.path.join(PROCESSED_FOLDER, "products_cleaned.csv")
    df.to_csv(output_path, index=False)
    
    print(f"Clean data saved to {output_path}")


def main():
    print("Starting transformation...")

    file_path = get_latest_file()
    print(f"Processing file: {file_path}")
    
    df = transform_data(file_path)
    print("Raw Data Sample:\n", df.head())
    
    df_clean = clean_data(df)
    print("Cleaned Data Sample:\n", df_clean.head())
    
    save_data(df_clean)
    
    print("Transformation completed successfully ✅")


if __name__ == "__main__":
    main()
