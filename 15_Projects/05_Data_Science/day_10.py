"""
📚 **Problem Statement: Book Recommendation Engine**

1. **Objective:**
   To develop a **content-based book recommendation system** that suggests similar books based on a user’s input title.

2. **Dataset:**
   The dataset (`books.csv`) contains book details such as **title**, **author**, and **description**.

3. **Approach:**

   * Use **TF-IDF Vectorization** to convert book descriptions into numerical feature vectors.
   * Apply **Cosine Similarity** to identify books with similar content or themes.

4. **Implementation:**

   * The system is deployed as an interactive **Streamlit web app**.
   * Users enter a book title, and the model recommends the **top 5 most similar books**.

5. **Expected Outcome:**
   The app displays a table of recommended books (titles and authors), helping users discover new books similar to their interests.

"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

df = pd.read_csv("books.csv")
df['title'] = df['title'].str.strip()
df['description'] = df['description'].fillna("")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()


def get_recommendations(title, df,  cosine_sim, indices):
    title = title.strip().lower()

    if title not in indices.index:
        return f"{title} not found in dataset"
    
    idx = indices.loc[title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]


    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]


st.title("Book Recommendation Engine")
st.write("Enter a book title and get similar recommendation")

select_book = st.text_input("Book: Title")

if select_book:
    results = get_recommendations(select_book, df, cosine_sim, indices)

    if isinstance(results, pd.DataFrame):
        st.table(results)
    else:
        st.warning(results)