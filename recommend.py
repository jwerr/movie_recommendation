import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
def load_data(filepath):
    """
    Load the dataset from a CSV file.
    """
    data = pd.read_csv(filepath)
    return data

# Preprocess the data
def preprocess_data(data):
    """
    Combine genres and plot summaries into a single text field.
    """
    if 'plot_summary' in data.columns:
        data['combined_text'] = data['genre'].fillna('') + " " + data['plot_summary']
    else:
        data['combined_text'] = data['genre'].fillna('')
    return data

# Build the TF-IDF matrix
def build_tfidf_matrix(data):
    """
    Transform the combined text into a TF-IDF matrix.
    """
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), min_df=2)
    tfidf_matrix = vectorizer.fit_transform(data['combined_text'])
    return vectorizer, tfidf_matrix

# Recommend movies
def recommend_movies(user_input, data, vectorizer, tfidf_matrix, top_n=5):
    """
    Recommend movies based on user input.
    """
    user_input = user_input.strip().lower()
    if not user_input:
        print("Please enter a valid movie description.")
        return pd.DataFrame()

    # Transform user input into a TF-IDF vector
    user_vector = vectorizer.transform([user_input])

    # Compute cosine similarity
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()

    # Get top N recommendations
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    recommendations = data.iloc[top_indices].copy()
    recommendations['similarity_score'] = similarities[top_indices]

    return recommendations[['title', 'similarity_score']]

# Main function
def main():
    # Load and preprocess data
    data = load_data("data/movies.csv")
    data = preprocess_data(data)

    # Build TF-IDF matrix
    vectorizer, tfidf_matrix = build_tfidf_matrix(data)

    # Get user input
    user_query = input("What kind of movie are you in the mood for? Describe your preferences: ").strip()

    # Get recommendations
    recommendations = recommend_movies(user_query, data, vectorizer, tfidf_matrix)

    # Display results
    if not recommendations.empty:
        print("\nTop Recommendations:")
        print(recommendations)
    else:
        print("No recommendations found. Try a different description.")

if __name__ == "__main__":
    main()