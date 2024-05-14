from flask import Flask, request, jsonify
import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Ensure the punkt tokenizer is available
nltk.download('punkt')

# Load the model and vectorizer
data = pd.read_csv("./mental_health.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])
y = data['label']
logistic_classifier = LogisticRegression()
logistic_classifier.fit(X, y)

def clean_text_function(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

@app.route('/predict', methods=['POST'])
def predict():
    """ API endpoint to predict stress or no stress from the input text. """
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    cleaned_text = clean_text_function(text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = logistic_classifier.predict(vectorized_text)
    label = "stress" if prediction[0] == 1 else "no stress"  

    return jsonify({'label': label})  

if __name__ == '__main__':
    app.run(debug=True)
