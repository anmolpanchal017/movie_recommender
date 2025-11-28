import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df = df.drop_duplicates(subset="Series_Title")
    return df
