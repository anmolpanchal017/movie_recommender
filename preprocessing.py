def preprocess(df):
    for col in ["Overview", "Genre", "Director", "Star1", "Star2", "Star3", "Star4"]:
        df[col] = df[col].fillna("")

    df["combined_features"] = (
        df["Genre"] + " " +
        df["Director"] + " " +
        df["Star1"] + " " +
        df["Star2"] + " " +
        df["Star3"] + " " +
        df["Star4"] + " " +
        df["Overview"]
    )

    return df
