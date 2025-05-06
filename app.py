from flask import Flask, request, jsonify, render_template
import nltk
import random
from nltk.util import ngrams
from collections import defaultdict

nltk.download('punkt_tab')

nltk.download('punkt')

app = Flask(__name__)

def load_corpus():
    with open('corpus.txt', 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text

corpus = load_corpus()

def build_ngram_model(corpus, n):
    tokens = nltk.word_tokenize(corpus)
    ngram_list = list(ngrams(tokens, n))
    model = defaultdict(lambda: defaultdict(int))

    for word in ngram_list:
        history = word[0: -1]
        pred = word[-1]
        model[history][pred] += 1

    # Normalize the frequencies
    for key, value in model.items():
        count = float(sum(value.values()))
        for k, v in value.items():
            model[key][k] = v / count

    return model

def ngram_predict(model, h):
  h = tuple(h)

  if h in model:
    word = list(model[h].keys())
    pred = list(model[h].values())
    return random.choices(word, weights=pred)[0]
  else:
    return "No prediction"


model = build_ngram_model(corpus, 3)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = ngram_predict(model, data['text'].split()[-2:])
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
