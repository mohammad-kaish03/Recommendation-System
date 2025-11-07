import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process

# Load and preprocess data
df = pd.read_csv("netflix_titles.csv")

df[["director", "cast", "country", "date_added"]] = df[["director", "cast", "country", "date_added"]].fillna("Unknown")
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])
df["duration"] = df["duration"].fillna("Unknown")

# Prepare recommendation data
movies = df[["show_id", "title", "listed_in", "description"]].copy()
movies["tags"] = movies["description"] + " " + movies["listed_in"]
new_data = movies.drop(columns=["listed_in", "description"])

# Vectorize and compute similarity
vectorizer = CountVectorizer(max_features=8807, stop_words="english")
vectors = vectorizer.fit_transform(new_data["tags"].values.astype("U")).toarray()
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie_title):
    try:
        index = df[df['title'] == movie_title].index[0]
        similarity_scores = list(enumerate(similarity[index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]
        movie_indices = [i[0] for i in similarity_scores]
        return df.iloc[movie_indices][["title", "type", "release_year", "rating", "duration", "listed_in", "cast", "description"]]
    except IndexError:
        return pd.DataFrame()

# Streamlit UI
st.set_page_config(page_title="🎬 Netflix Movie Recommender", layout="wide")
st.title("🎬 Netflix Movie Recommender")
st.markdown("Get movie recommendations based on genre and description. Choose how you'd like to search:")

# Input method selection
input_method = st.radio("Choose input method:", ["Dropdown", "Search Bar"])
movie_list = df['title'].dropna().unique().tolist()
selected_movie = None

# Dropdown input
if input_method == "Dropdown":
    selected_movie = st.selectbox("🎬 Pick a movie from the list", sorted(movie_list))

# Search bar input with fuzzy matching
elif input_method == "Search Bar":
    user_input = st.text_input("🔍 Type a movie title")
    if user_input:
        best_match = process.extractOne(user_input, movie_list)
        if best_match and best_match[1] > 60:  # Confidence threshold
            st.success(f"Showing recommendations for: **{best_match[0]}**")
            selected_movie = best_match[0]
        else:
            st.error("No close match found. Try a different title.")

# Trigger recommendation
if selected_movie and st.button("Recommend"):
    results = recommend(selected_movie)
    if not results.empty:
        st.subheader("📽️ Recommended Movies")
        for _, row in results.iterrows():
            st.markdown(f"### {row['title']} ({row['release_year']})")
            st.markdown(f"**Type**: {row['type']}  |  **Rating**: {row['rating']}  |  **Duration**: {row['duration']}")
            st.markdown(f"**Genre**: {row['listed_in']}")
            st.markdown(f"**Cast**: {row['cast']}")
            st.markdown(f"**Description**: {row['description']}")
            st.markdown("---")
    else:
        st.error("No similar movies found.")