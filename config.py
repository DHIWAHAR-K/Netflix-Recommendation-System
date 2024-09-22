#config.py
from data_loader import load_data, parse_data
from recommendation import compute_tfidf, compute_cosine_similarity, create_reverse_mapping

def initialize_data():
    # Load and prepare data
    df2 = load_data()
    df2 = parse_data(df2)
    
    # Compute TF-IDF matrix and cosine similarity
    tfidf_matrix = compute_tfidf(df2)
    cosine_sim = compute_cosine_similarity(tfidf_matrix)
    
    # Create a reverse mapping of movie indices
    indices = create_reverse_mapping(df2)
    
    return df2, cosine_sim, indices