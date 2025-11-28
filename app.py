from flask import Flask, render_template, request
from src.data_loader import load_data
from src.preprocessing import preprocess
from src.recommender import MovieRecommender
from src.poster_fetcher import fetch_movie_details

app = Flask(__name__)

# ------------------- LOAD & PREPARE DATA -------------------
df = load_data("data/imdb_top_1000.csv")
df = preprocess(df)
model = MovieRecommender(df)
# ------------------------------------------------------------


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    # Handle user inputs from form
    if request.method == "POST":
        query_type = request.form.get("query_type")

        # ---------------- TITLE SEARCH ----------------
        if query_type == "title":
            title = request.form.get("movie_name")

            movies = model.recommend(title)     # list of movie names
            result = []

            for m in movies:
                details = fetch_movie_details(m)
                result.append(details if details else {"title": m})

        # ---------------- KEYWORD SEARCH ----------------
        elif query_type == "keyword":
            keyword = request.form.get("keyword")

            movies = model.recommend_by_keywords(keyword)
            result = []

            for m in movies:
                details = fetch_movie_details(m)
                result.append(details if details else {"title": m})

        # ---------------- GENRE SEARCH ----------------
        elif query_type == "genre":
            genre = request.form.get("genre")

            movies = model.recommend_by_genre(genre)
            result = []

            for m in movies:
                details = fetch_movie_details(m)
                result.append(details if details else {"title": m})

    # Return HTML page
    return render_template(
        "index.html",
        result=result,
        movies=df["Series_Title"].tolist()
    )


if __name__ == "__main__":
    app.run(debug=True)
