from flask import Flask, request, jsonify, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')

# Load your pre-trained model
model_path = 'models/model.h5'
model = tf.keras.models.load_model(model_path)

# Load the tokenizer
with open('models/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

def preprocess_review(review):
    sequences = tokenizer.texts_to_sequences([review])
    padded_sequences = pad_sequences(sequences, maxlen=100)  # Match maxlen used in training
    return padded_sequences

def predict_sentiment(review):
    review = preprocess_review(review)
    prediction = model.predict(review)
    sentiment_score = prediction[0][0]
    
    # Convert the score to a sentiment label
    if sentiment_score > 0.7:
        return "positive"
    elif sentiment_score < 0.3:
        return "negative"
    else:
        return "neutral"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.form.get('review', '')
    if review:
        sentiment = predict_sentiment(review)
        return jsonify({'sentiment': sentiment})
    else:
        return jsonify({'error': 'No review provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
