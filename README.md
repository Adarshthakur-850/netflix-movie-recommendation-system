🎬 Netflix Movie Recommendation System

A Machine Learning–based movie recommendation system that suggests personalized Netflix movies using content-based and similarity-driven techniques. The system analyzes movie metadata such as genres, cast, crew, keywords, and overview to recommend similar movies to users.

This project demonstrates end-to-end data processing, feature engineering, similarity modeling, and recommendation generation using Python, Pandas, and Scikit-Learn.

🚀 Features

Content-Based Movie Recommendation

Cosine Similarity for finding similar movies

Text Vectorization using CountVectorizer / TF-IDF

Data Cleaning and Feature Engineering

Interactive recommendation through Jupyter Notebook / script

Scalable pipeline for large movie datasets

🗂️ Project Structure
netflix-movie-recommendation-system/

│

├── data/                  # Raw and processed datasets

├── notebooks/             # Jupyter notebooks for EDA and modeling

├── src/

│   └── data/              # Data processing scripts

├── requirements.txt

└── README.md

📊 Dataset

The dataset contains Netflix movie metadata including:

Movie Title

Genres

Cast

Crew

Keywords

Overview

Popularity metrics

The recommendation is built purely on movie content (no user history required).

🧠 How the Recommendation Works

Combine important textual features (genres, cast, crew, keywords, overview)

Clean and preprocess the text data

Convert text into numerical vectors using CountVectorizer / TF-IDF

Compute Cosine Similarity between movie vectors

For a given movie, retrieve top N most similar movies

🛠️ Tech Stack

Python

Pandas

NumPy

Scikit-Learn

Jupyter Notebook

Matplotlib / Seaborn (for EDA)

⚙️ Installation
git clone https://github.com/Adarshthakur-850/netflix-movie-recommendation-system.git
cd netflix-movie-recommendation-system
pip install -r requirements.txt

▶️ Usage

Open the notebook and run all cells:

jupyter notebook notebooks/


Or run the recommendation script (if available):

python src/main.py


Example:

recommend("Inception")


Output:

Top 5 Recommended Movies:
1. Interstellar
2. The Prestige
3. The Dark Knight
4. Memento
5. Tenet

📈 Exploratory Data Analysis

Genre distribution

Most frequent actors

Keyword frequency

Popular movies by count

🧩 Future Improvements

Hybrid recommendation (content + collaborative filtering)

Web interface using Streamlit / Flask

User login and personalized recommendations

Deployment on cloud

Integration with real-time Netflix dataset

📌 Learning Outcomes

This project covers:

NLP for feature extraction

Vector space modeling

Similarity metrics

ML pipeline design

Practical recommender system implementation

🤝 Contributing

Contributions, issues, and suggestions are welcome.

📜 License

This project is for educational and learning purposes.

👤 Author

Adarsh Thakur
Machine Learning | Data Science | DevOps Enthusiast
GitHub: https://github.com/Adarshthakur-850
