import streamlit as st
import joblib

st.set_page_config(page_title="Nepali News Classifier", page_icon="📰", layout="centered")
st.header("📰 Nepali News Text Classifier")
st.markdown("Enter a piece of Nepali news text below, and the model will predict its category.")

model = joblib.load("nep_news.joblib")

user_input = st.text_area(
    label="Paste your Nepali news text here:",
    placeholder="यहाँ आफ्नो समाचार लेख्नुहोस्...",
    max_chars=1000,
    height=300
)

if st.button("Classify News"):
    if user_input.strip() == "":
        st.warning("कृपया समाचारको पाठ प्रविष्ट गर्नुहोस्।")
    else:
        prediction = model.predict([user_input])[0]
        st.success(f"🔹 Predicted Category: **{prediction}**")
