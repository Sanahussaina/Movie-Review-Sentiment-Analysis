# Movie Review Sentiment Analysis

This project performs sentiment analysis on movie reviews using a deep learning model.

## Project Structure
movie-review-sentiment-analysis/
│
├── dataset/
│   └── aclImdb/  # Extract the IMDb dataset here
│
├── frontend/
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   └── templates/
│       └── index.html
│
├── models/
│   └── sentiment_model.h5
│
├── app.py
├── preprocess.py
├── train_model.py
├── init_db.py
├── requirements.txt
└── README.md


   1. **Download the IMDb Dataset**:
      - IMDb Movie Reviews Dataset: [Download here](https://ai.stanford.edu/~amaas/data/sentiment/).

  
### Running the Project

1. **Open a Terminal** (Command Prompt, PowerShell, or any terminal you prefer).

2. **Navigate to the Project Directory**:
   
   cd path/to/movie-review-sentiment-analysis
   

3. **Set Up Virtual Environment**:
   
   python -m venv env
   env\Scripts\activate  # On Windows
   source env/bin/activate  # On macOS/Linux
   

4. **Install Dependencies**:
   
   pip install -r requirements.txt
   

5. **Prepare the Dataset**:
   
   python preprocess.py
   

6. **Train the Model**:
   
   python train_model.py
   

7. **Initialize the Database**:
   
   python init_db.py
   

8. **Run the Flask Application**:
   
   python app.py
   

9. **Access the Web Application**:
   Open your browser and navigate to `http://127.0.0.1:5000` to see the frontend where you can input movie reviews and get sentiment analysis.

