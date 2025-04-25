# webapp/recommend_utils.py
import os
import pandas as pd
from surprise import Dataset, Reader, SVD
import joblib

# Define base project path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Load movies metadata
def load_movies():
    path = os.path.join(BASE_DIR, "MoviesLense", "movies.csv")
    return pd.read_csv(path)

# Load ratings data
def load_ratings():
    path = os.path.join(BASE_DIR, "MoviesLense", "ratings.csv")
    return pd.read_csv(path)

# Load or train model (uses saved .pkl if available)
def train_model():
    model_path = os.path.join(BASE_DIR, "webapp", "svd_model.pkl")

    if os.path.exists(model_path):
        try:
            print("Loading saved model...")
            return joblib.load(model_path)
        except Exception as e:
            print("Failed to load model. Reason:", str(e))
            print("Re-training the model...")

    # Either model file didn't exist OR loading failed — so we retrain
    ratings = load_ratings()
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    trainset = data.build_full_trainset()

    model = SVD(n_factors=50, lr_all=0.005, reg_all=0.1)
    model.fit(trainset)

    joblib.dump(model, model_path)
    print("Model trained and saved to:", model_path)
    return model


# Generate top-N recommendations for a user
def get_top_n(model, user_id, movies_df, n=5):
    movie_ids = movies_df['movieId'].unique()
    rated_df = load_ratings()
    watched = rated_df[rated_df['userId'] == user_id]['movieId'].values
    unseen = [m for m in movie_ids if m not in watched]

    predictions = [(movie, model.predict(user_id, movie).est) for movie in unseen]
    predictions.sort(key=lambda x: x[1], reverse=True)
    top_n = predictions[:n]

    top_n_df = pd.DataFrame(top_n, columns=["movieId", "predicted_rating"])
    result = pd.merge(top_n_df, movies_df, on="movieId")[["title", "predicted_rating"]]
    return result
