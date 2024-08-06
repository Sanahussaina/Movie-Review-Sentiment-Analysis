import os
import numpy as np
import nltk
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Set the NLTK data path
nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')
nltk.data.path.append(nltk_data_path)

# Download stopwords if not already downloaded
try:
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
except LookupError:
    nltk.download('stopwords', download_dir=nltk_data_path)
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')

def load_data(data_dir):
    texts, labels = [], []
    for label_type in ['neg', 'pos']:
        dir_name = os.path.join(data_dir, label_type)
        for fname in os.listdir(dir_name):
            if fname.endswith('.txt'):
                with open(os.path.join(dir_name, fname), 'r', encoding='utf-8') as f:
                    texts.append(f.read())
                labels.append(0 if label_type == 'neg' else 1)
    return texts, labels

def preprocess_data(texts, labels, max_len=100, max_words=5000):
    texts = [' '.join([word for word in text.split() if word.lower() not in stop_words]) for text in texts]

    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    word_index = tokenizer.word_index

    data = pad_sequences(sequences, maxlen=max_len)
    labels = np.asarray(labels)

    return data, labels, word_index

if __name__ == "__main__":
    data_dir = 'dataset/aclImdb/train'
    texts, labels = load_data(data_dir)
    data, labels, word_index = preprocess_data(texts, labels)
    np.save('data.npy', data)
    np.save('labels.npy', labels)
    np.save('word_index.npy', word_index)
