from flask import Flask, render_template, request

app = Flask(__name__)

positive_words = ["good", "great", "amazing", "love", "excellent", "best"]
negative_words = ["bad", "worst", "hate", "terrible", "awful"]

def predict_sentiment(text):
    text = text.lower()
    
    score = 0
    
    for word in positive_words:
        if word in text:
            score += 1
            
    for word in negative_words:
        if word in text:
            score -= 1

    if score >= 0:
        return "Positive review 😊"
    else:
        return "Negative review 😡"

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        text = request.form["review"]
        result = predict_sentiment(text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)