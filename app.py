#app.py
from config import initialize_data
from flask import Flask, jsonify, request
from services.recommendation import get_recommendations

app = Flask(__name__)

# Initialize and load data on startup
df2, cosine_sim, indices = initialize_data()

@app.route('/recommend', methods=['GET'])
def recommend():
    # Get the movie title from the request
    title = request.args.get('title')
    if not title:
        return jsonify({"error": "Please provide a movie title."}), 400
    # Get recommendations
    try:
        recommendations = get_recommendations(title, cosine_sim, indices, df2)
        return jsonify({"recommendations": recommendations.tolist()})
    except KeyError:
        return jsonify({"error": "Movie not found."}), 404

if __name__ == '__main__':
    app.run(debug=True)