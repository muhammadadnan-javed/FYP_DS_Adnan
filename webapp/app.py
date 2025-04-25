# webapp/app.py

# webapp/app.py

import streamlit as st
import joblib
import os
from recommend_utils import load_movies, load_ratings, get_top_n

# 📌 Page setup
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("MovieLens Recommender System")
st.caption("Built using Surprise + Streamlit")

# 🚀 Load data and pretrained model
with st.spinner("Loading model and data..."):
    movies = load_movies()
    ratings = load_ratings()

    # ✅ Load saved trained model (SVD++)
    model_path = os.path.join("webapp", "svdpp_best_model.pkl")
    if os.path.exists(model_path):
        model = joblib.load(model_path)
    else:
        st.error("❌ Trained model not found. Please train and save it first.")
        st.stop()

st.success("✅ Model loaded successfully!")

# 📋 User input sidebar
st.sidebar.header("Select Options")
user_ids = ratings['userId'].unique()
selected_user = st.sidebar.selectbox("Select a User ID", sorted(user_ids))

num_recs = st.sidebar.slider("Number of Recommendations", min_value=3, max_value=15, value=5)

# 🔘 Recommend button
if st.sidebar.button("Recommend"):
    with st.spinner("Generating personalized recommendations..."):
        recommendations = get_top_n(model, selected_user, movies, n=num_recs)

    st.subheader(f"Top {num_recs} Recommended Movies for User {selected_user}")
    st.table(recommendations.style.format({"predicted_rating": "{:.2f}"}))
