import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import pickle

# Load and preprocess data
def load_data(data_dir):
    texts = []
    labels = []
    for category in ['pos', 'neg']:
        label = 1 if category == 'pos' else 0
        dir_name = os.path.join(data_dir, 'train', category)
        for fname in os.listdir(dir_name):
            with open(os.path.join(dir_name, fname), 'r', encoding='utf-8') as f:
                texts.append(f.read())
                labels.append(label)
    return texts, labels

data_dir = 'dataset/aclImdb'
texts, labels = load_data(data_dir)

# Tokenize the data
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
data = pad_sequences(sequences, maxlen=100)

# Save the tokenizer
os.makedirs('models', exist_ok=True)
with open('models/tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Create the model
model = Sequential()
model.add(Embedding(5000, 128, input_length=100))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Train the model
labels = np.array(labels)
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

model.fit(X_train, y_train, batch_size=32, epochs=10, validation_data=(X_test, y_test))

# Save the model
model.save('models/model.h5')

print(f"Validation Accuracy: {history.history['val_accuracy'][-1]}")