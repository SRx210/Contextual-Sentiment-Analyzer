import streamlit as st
import joblib

# Load the trained model
pipeline = joblib.load("tfidf_logreg_sentiment.pkl")

st.title("🎬 IMDb Movie Review Sentiment Analyzer")

# Input box
user_input = st.text_area("Enter your movie review:")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        prediction = pipeline.predict([user_input])[0]
        sentiment = "Positive!!" if prediction == 1 else "Negative!!"
        st.success(f"Sentiment: {sentiment}")
    else:
        st.warning("Please enter a review to analyze.")