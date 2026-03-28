import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv("dataset.csv")

X = data["text"]
y = data["label"]

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_vectorized, y)

def detect_phishing_ml(email):
    email_vec = vectorizer.transform([email])
    prediction = model.predict(email_vec)[0]
    
    if prediction == 1:
        return "⚠️ Phishing Email Detected"
    else:
        return "✅ Safe Email"