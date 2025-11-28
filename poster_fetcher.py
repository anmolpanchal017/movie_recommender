import os

def fetch_movie_details(title):

    # Convert title to file-safe name
    filename = title.replace(":", "").replace(" ", "_") + ".jpg"
    poster_path = os.path.join("static", "posters", filename)

    # If local poster exists
    if os.path.exists(poster_path):
        poster_url = f"/static/posters/{filename}"
    else:
        poster_url = "/static/placeholder.png"

    return {
        "title": title,
        "year": "",
        "genre": "",
        "rating": "",
        "plot": "",
        "poster": poster_url
    }
