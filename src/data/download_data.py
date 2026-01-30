import os
import requests
import zipfile
import io
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

DATA_URL = "https://files.grouplens.org/datasets/movielens/ml-20m.zip"
# Get project root (3 levels up from src/data/download_data.py)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

def download_data():
    """Downloads and extracts the MovieLens 20M dataset."""
    if not RAW_DATA_PATH.exists():
        RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
    
    # Check if data already exists to avoid re-downloading
    if (RAW_DATA_PATH / "ml-20m" / "ratings.csv").exists():
        logging.info("Dataset already exists in %s", RAW_DATA_PATH)
        return

    logging.info("Downloading MovieLens 20M dataset from %s...", DATA_URL)
    try:
        response = requests.get(DATA_URL, stream=True)
        response.raise_for_status()
        
        logging.info("Extracting dataset to %s...", RAW_DATA_PATH)
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(RAW_DATA_PATH)
            
        logging.info("Dataset downloaded and extracted successfully to %s", RAW_DATA_PATH)
    except Exception as e:
        logging.error("Failed to download or extract dataset: %s", e)
        raise

if __name__ == "__main__":
    download_data()
