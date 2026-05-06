from flask import Flask, render_template, request
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

model = load_model("sentiment_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 100

def predict_sentiment(text):
    text = text.lower()

    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)

    prediction = model.predict(padded)[0][0]

    if prediction >= 0.5:
        return f"Positive review 😊 (Confidence: {prediction:.2f})"
    else:
        return f"Negative review 😡 (Confidence: {1 - prediction:.2f})"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        text = request.form["review"]
        result = predict_sentiment(text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)