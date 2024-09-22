#data_loader.py
import pandas as pd
from ast import literal_eval

def load_data():
    # Load the data
    df1 = pd.read_csv('./tmdb_5000_credits.csv')
    df2 = pd.read_csv('./tmdb_5000_movies.csv')
    
    # Rename columns
    df1.columns = ['id', 'tittle', 'cast', 'crew']
    
    # Merge the datasets
    df2 = df2.merge(df1, on='id')
    return df2

def parse_data(df2):
    # Parse stringified columns (cast, crew, keywords, genres)
    features = ['cast', 'crew', 'keywords', 'genres']
    for feature in features:
        df2[feature] = df2[feature].apply(literal_eval)
    return df2