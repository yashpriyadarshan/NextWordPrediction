# Next Word Prediction Using Trigram Model

This project implements a **Next Word Prediction** system using a **Trigram (3-gram)** model based on **Natural Language Processing (NLP)**. The web application predicts the next word based on the user's last two typed words. The backend of the application is built using **Flask** and **Python**, while the frontend is created using **HTML**, **CSS**, and **JavaScript**.

The system dynamically provides next word suggestions as the user types, similar to the autocomplete feature found in popular applications like Gmail.

---

## **Features**

- **Next Word Prediction**: Predicts the next word based on the last two typed words.
- **Real-Time Suggestions**: Displays word suggestions as the user types.
- **Corpus used**: Uses the *The Odyssey* book as a corpus to train a trigram n-gram model.
- **Backend**: Built using **Flask** to serve a Trigram model for predicting the next word.
- **Frontend**: Created with **HTML**, **CSS**, and **JavaScript** for user interaction.
- **Interactive UI**: The user can press **Enter** to automatically insert the predicted word into the text field.

---

## **How It Works**

1. **User Input**: The user types a sequence of words into the input field.
2. **Prediction**: As the user types, the application sends the last two words to the backend.
3. **Backend**: The **Flask** server receives the input, processes it with a **Trigram (3-gram)** model built from a corpus of text, and predicts the next word.
4. **Frontend**: The predicted word is shown as a suggestion in real time.
5. **Insertion**: The user can press **Enter** to automatically insert the predicted word into the input field.

---

## **Project Structure**

├── app.py # Flask application<br>
├── corpus.txt # Text file used to build the N-gram model<br>
├── templates/<br>
&nbsp└── index.html # HTML structure for the webpage, includes css and javascript<br>
└── requirements.txt # Python dependencies<br>


---

## **Installation**

To run this project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/next-word-prediction.git
    cd next-word-prediction
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the necessary NLTK data (for tokenization):
    ```bash
    python -m nltk.downloader punkt
    ```

5. Ensure that the `corpus.txt` file is present in the root directory.

---

## **Run the Application Locally**

1. Start the Flask server:
    ```bash
    python app.py
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```
    
---

## **Libraries and Technologies Used**

- **Flask**: Web framework for Python.
- **NLTK**: Natural Language Toolkit, used for tokenizing and building the n-gram model.
- **HTML/CSS**: For creating and styling the user interface.
- **JavaScript**: For handling user input and interacting with the backend via API calls.

---

## **Challenges Faced**

- **Handling large text corpora**: The corpus used to train the n-gram model can be quite large, requiring efficient handling and processing to ensure the application performs well.
- **Real-time predictions**: Implementing an efficient system for real-time text predictions while ensuring responsiveness and accuracy.

---

## **Requirements**

- Python 3.x
- Flask
- NLTK

You can install the necessary Python libraries using:

```bash
pip install -r requirements.txt
