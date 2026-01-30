import os
import pandas as pd
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "ml-20m"
PROCESSED_PATH = PROJECT_ROOT / "data" / "processed"

def load_data():
    """Loads raw data from CSV files."""
    movies_path = RAW_PATH / "movies.csv"
    ratings_path = RAW_PATH / "ratings.csv"
    
    if not movies_path.exists() or not ratings_path.exists():
        raise FileNotFoundError(f"Data files not found in {RAW_PATH}. Run download_data.py first.")
    
    logging.info("Loading movies.csv...")
    movies = pd.read_csv(movies_path)
    
    logging.info("Loading ratings.csv...")
    ratings = pd.read_csv(ratings_path)
    
    return movies, ratings

def preprocess_movies(movies):
    """Cleans movie data."""
    logging.info("Preprocessing movies...")
   
    movies['year'] = movies['title'].str.extract(r'\((\d{4})\)', expand=False)
    movies['year'] = pd.to_numeric(movies['year'], errors='coerce')
    

    movies['year'] = movies['year'].fillna(0).astype(int)
    
  
    movies['title'] = movies['title'].str.replace(r'\s*\(\d{4}\)', '', regex=True).str.strip()
    

    movies['genres'] = movies['genres'].str.split('|')
    
    return movies

def preprocess_ratings(ratings):
    """Cleans ratings data."""
    logging.info("Preprocessing ratings...")
   
    ratings['timestamp'] = pd.to_datetime(ratings['timestamp'], unit='s')
    return ratings

def save_data(movies, ratings):
    """Saves processed data to Parquet."""
    if not PROCESSED_PATH.exists():
        PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
        
    logging.info(f"Saving processed data to {PROCESSED_PATH}...")
    movies.to_parquet(PROCESSED_PATH / "movies.parquet", index=False)
    ratings.to_parquet(PROCESSED_PATH / "ratings.parquet", index=False)
    logging.info("Data saved successfully.")

def main():
    try:
        movies, ratings = load_data()
        movies = preprocess_movies(movies)
        ratings = preprocess_ratings(ratings)
        save_data(movies, ratings)
    except Exception as e:
        logging.error(f"Preprocessing failed: {e}")

if __name__ == "__main__":
    main()
