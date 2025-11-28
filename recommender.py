from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, df):
        self.df = df
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(df["combined_features"])
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def recommend(self, title, top_n=10):
        if title not in self.df["Series_Title"].values:
            return ["Movie not found."]

        index = self.df[self.df["Series_Title"] == title].index[0]
        distances = self.similarity_matrix[index]

        similar_movies = sorted(
            list(enumerate(distances)),
            key=lambda x: x[1],
            reverse=True
        )[1:top_n+1]

        return [self.df.iloc[i[0]].Series_Title for i in similar_movies]

    def recommend_by_keywords(self, keywords, top_n=10):
        query_vec = self.vectorizer.transform([keywords])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        top_indices = scores.argsort()[::-1][:top_n]
        return self.df.iloc[top_indices]["Series_Title"].tolist()

    def recommend_by_genre(self, genre, top_n=10):
        sub = self.df[self.df["Genre"].str.contains(genre, case=False)]
        sub = sub.sort_values("IMDB_Rating", ascending=False)
        return sub["Series_Title"].head(top_n).tolist()
