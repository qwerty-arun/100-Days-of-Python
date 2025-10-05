"""
YouTube Comment Classifier

1. **Objective:**
   Build a machine learning web app that classifies YouTube comments as **Toxic** or **Supportive** using Natural Language Processing (NLP).

2. **Dataset:**
   The dataset (`youtube_comments.csv`) contains user comments labeled as either *toxic* or *supportive*.

3. **Approach:**
   Use a **TF-IDF Vectorizer** to convert text into numerical form and **Logistic Regression** for sentiment classification, combined in a Scikit-learn **Pipeline**.

4. **Implementation:**
   A **Streamlit** web interface allows users to enter a comment, which the trained model classifies instantly.

5. **Outcome:**
   The app displays whether the entered comment is **Toxic** (negative) or **Supportive** (positive).

"""
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])
    model.fit(df['comment'], df['label'])
    return model

model = load_model()

st.title("Youtube Comment Classifier")
st.write("Classify your comments as Toxic or Supportive")
user_input = st.text_area("Enter a youtube comment")

if user_input:
    prediction = model.predict([user_input])[0]
    if prediction == 'toxic':
        st.error("This comment is likely **Toxic**")
    else:
        st.success("This comment is **Supportive**")