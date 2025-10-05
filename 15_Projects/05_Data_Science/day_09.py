"""
📚 **Problem Statement: Book Recommendation System**

1. **Objective:**
   To build a **content-based recommendation system** that suggests books similar to a given title based on their descriptions.

2. **Dataset:**
   The dataset (`books.csv`) contains details about books such as their **title**, **author**, and **description**.

3. **Approach:**

   * Use **TF-IDF Vectorization** to convert book descriptions into numerical feature vectors.
   * Compute **Cosine Similarity** to measure how similar each book is to others based on description content.

4. **Implementation:**

   * When a book title is provided, the system retrieves the **top 5 most similar books** using cosine similarity scores.
   * The output displays the **titles and authors** of the recommended books.

5. **Expected Outcome:**
   The program recommends books with **similar themes or content**, helping users discover new books aligned with their interests.

"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv("books.csv")

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df['title'])


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[['title', 'author']].iloc[book_indices]

rec = get_recommendations("Spacebound")
print(rec)