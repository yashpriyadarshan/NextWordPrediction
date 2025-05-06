# Next Word Prediction Using Trigram Model

This project implements a **Next Word Prediction** system using a **Trigram (3-gram)** model based on **Natural Language Processing (NLP)**. The web application predicts the next word based on the user's last two typed words. The backend of the application is built using **Flask** and **Python**, while the frontend is created using **HTML**, **CSS**, and **JavaScript**.

The system dynamically provides next word suggestions as the user types, similar to the autocomplete feature found in popular applications like Gmail.

---

## **Features**

- **Next Word Prediction**: Predicts the next word based on the last two typed words.
- **Real-Time Suggestions**: Displays word suggestions as the user types.
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

