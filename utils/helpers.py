#helpers.py
def handle_missing_title():
    return {"error": "Please provide a movie title."}, 400

def handle_movie_not_found():
    return {"error": "Movie not found."}, 404