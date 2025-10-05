"""
YouTube Comment Sentiment Classification

1. **Objective:**
   To develop a machine learning model that classifies YouTube comments based on sentiment (e.g., *positive*, *negative*, or *neutral*).

2. **Motivation:**

   * YouTube receives thousands of comments per video.
   * Manual analysis of sentiment is time-consuming and subjective.
   * Automating this process helps creators understand audience feedback more efficiently.

3. **Dataset:**

   * The dataset contains YouTube comments and their corresponding sentiment labels.
   * The data is split into 80% training and 20% testing sets.

4. **Approach:**

   * Use **TF-IDF Vectorization** to convert text data into numerical features.
   * Apply **Logistic Regression** as the classification algorithm.
   * Combine both steps using a **Scikit-learn Pipeline** for efficiency.

5. **Implementation Steps:**

   * Load and preprocess the dataset.
   * Split the dataset into training and testing subsets.
   * Build a machine learning pipeline with `TfidfVectorizer` and `LogisticRegression`.
   * Train the model on the training data.
   * Evaluate model accuracy on the test data.

6. **Evaluation Metric:**

   * The model’s performance is measured using **accuracy** on the test dataset.

7. **Expected Outcome:**

   * The program outputs the accuracy percentage, showing how well the model predicts sentiments of unseen YouTube comments.

"""
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv("youtube_comments.csv")

# 20% test data, 80% training data
X_train, X_test, y_train, y_test = train_test_split(df['comment'], df['label'], test_size=0.2, random_state=42) 

model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

model.fit(X_train, y_train)

acc = model.score(X_test, y_test)
print(f"Model trained. Accuracy: {round(acc * 100, 2)}%")