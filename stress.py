from flask import Flask, request, jsonify
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ensure the punkt tokenizer is available
nltk.download('punkt')

# Preprocess the text data
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# Load the train and test datasets
train = pd.read_csv("dreaddit-train.csv")
test = pd.read_csv("dreaddit-test.csv")

train["text"] = train["text"].apply(preprocess_text)
test["text"] = test["text"].apply(preprocess_text)

# Split the train dataset
x_train = train["text"]
y_train = train["label"]

# Vectorize the text data
vectorizer = CountVectorizer(stop_words="english")
x_train_vect = vectorizer.fit_transform(x_train)

# Train the Naive Bayes classifier
naive_bayes = MultinomialNB()
naive_bayes.fit(x_train_vect, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint to predict stress or no stress from the input text."""
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    cleaned_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = naive_bayes.predict(vectorized_text)
    label = "stressed" if prediction[0] == 1 else "unstressed"

    return jsonify({'label': label})  

if __name__ == '__main__':
    app.run(debug=True)
