🎬 Netflix Movie Recommendation System
🧠 Project Overview

This project is a content-based movie recommender system built using Netflix’s public dataset.
It suggests movies similar to a user-selected title based on genre and description similarity, using Natural Language Processing (NLP) techniques.

An interactive Streamlit web app lets users search or select movies and view detailed recommendations with metadata like genre, cast, and rating.

🚀 Features

🔍 Smart Search – Find movies via dropdown or fuzzy search (tolerates typos).

🎞️ Personalized Recommendations – Suggests top 5 similar titles using content-based filtering.

📊 Metadata Display – View each movie’s genre, cast, rating, and summary.

⚡ Lightweight & Fast – Runs entirely on precomputed cosine similarity (no database needed).

🧩 How It Works

Combines textual features (description + listed_in) into a single “tags” field.

Converts these tags into numerical vectors using CountVectorizer.

Calculates cosine similarity between all movies.

Returns the top 5 most similar titles for a given movie.

📁 Dataset

Source: Netflix Titles Dataset (Kaggle)

File: netflix_titles.csv

Key Columns Used:

title – Movie/Show name

description – Plot summary

listed_in – Genres/categories

cast – Main actors

rating, release_year, duration

🛠️ Tech Stack

Python 3.x

Libraries: pandas, scikit-learn, rapidfuzz, streamlit

NLP Model: CountVectorizer (Bag-of-Words)

Frontend: Streamlit UI

⚙️ Installation & Setup

Clone this repository

git clone https://github.com/<your-username>/Netflix-Recommendation-System.git
cd Netflix-Recommendation-System


Install dependencies

pip install -r requirements.txt


Run the Streamlit App

streamlit run streamlit.py


or simply double-click app.bat (Windows users).

Try Sample Titles
See sample titles.txt for examples like:

Stranger Things

Money Heist

Black Mirror

📂 Repository Structure
📁 Netflix-Recommendation-System
│
├── netflix_titles.csv               # Dataset
├── netflix_titles recommend.ipynb   # Notebook for data preprocessing & similarity
├── streamlit.py                     # Main app file
├── app.bat                          # Quick launcher (Windows)
├── requirements.txt                 # Dependencies
├── sample titles.txt                # Example titles for testing
└── README.md                        # Documentation

🧾 Example Output

Input: Money Heist
Output Recommendations:
<img width="1740" height="807" alt="Screenshot 2026-01-20 210059" src="https://github.com/user-attachments/assets/57d463a0-4e60-46c2-904c-e7d5d583e1b8" />


Narcos

Breaking Bad

The Crown

Ozark

Peaky Blinders

Each includes:

🎭 Genre

🎬 Cast

⭐ Rating

📝 Short description

💡 Future Improvements

Add collaborative filtering (user–item interactions).

Include poster and trailer links using TMDB API.

Deploy online (e.g., Streamlit Cloud or Hugging Face Spaces).

Optimize similarity with TF-IDF or Sentence Transformers.

👨‍💻 Author

Mohammad Kaish Ansari
📍 Data Analyst | Aspiring Data Scientist
📧 mohammadkaish834@gmail.com

🏷️ License

This project is released under the MIT License — free to use, modify, and distribute with attribution.
