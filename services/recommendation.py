#recommendation.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_tfidf(df2):
    # Initialize a TF-IDF Vectorizer and remove stop words
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Replace NaN with an empty string
    df2['overview'] = df2['overview'].fillna('')
    
    # Fit and transform the overview column
    return tfidf.fit_transform(df2['overview'])

def compute_cosine_similarity(tfidf_matrix):
    # Compute the cosine similarity matrix
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def create_reverse_mapping(df2):
    # Create a reverse mapping of movie titles and indices
    return pd.Series(df2.index, index=df2['title']).drop_duplicates()

def get_recommendations(title, cosine_sim, indices, df2):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get similarity scores for the movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top 10 most similar movies (excluding the movie itself)
    sim_scores = sim_scores[1:11]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df2['title'].iloc[movie_indices]