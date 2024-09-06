# Netflix Recommendation System

This Flask application provides personalized movie recommendations using content-based filtering. It utilizes TMDB 5000 movie metadata to offer suggestions based on the similarity of movie descriptions.

## Project Structure

- `app.py`: The main application script that initializes the Flask interface and handles API requests.
- `config.py`: Contains initialization logic for loading data and configuring the recommendation system.
- `services/`
  - `data_loader.py`: Handles loading and preprocessing of the movie data.
  - `recommendation.py`: Implements Content-Based Filtering by computing TF-IDF vectors and cosine similarity.
- `utils/`
  - `helpers.py`: Provides helper functions for error handling and other utilities.

## Setup and Installation

Ensure you have Python 3.6+ installed and proceed with the following steps to set up the project environment:

1. Install required Python packages:

    ```bash
    pip install Flask pandas scikit-learn numpy
    ```

2. Download the required datasets and place them in the appropriate directory accessible by the `data_loader.py` script:

    - TMDB 5000 movie dataset (`tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`)

## Usage

To run the Flask application, navigate to the project directory in your terminal and execute:

```bash
python app.py
```

This command will start the Flask server, making the API available for movie recommendations. Interact with the API by sending a GET request to /recommend with a movie title as a query parameter, like so:

```bash
http://127.0.0.1:5000/recommend?title=The%20Dark%20Knight%20Rises
```

## Features

1. Data Loading and Parsing: Automated scripts to load and parse the TMDB 5000 movie dataset.

2. Content-Based Recommendation: Utilizes TF-IDF vectorization and cosine similarity to find movies similar to a given title.

3. Flask API: A simple and efficient web API to interact with the recommendation system.


## License

This README accurately reflects the Flask setup, dependencies, and usage, replacing Streamlit references with Flask and adjusting the paths and method descriptions accordingly. Feel free to copy and paste this content directly into your `README.md` file.