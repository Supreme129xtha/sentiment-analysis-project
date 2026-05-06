# ISY503_A3 – Sentiment Analysis Web Application

## 📌 Project Overview

This project implements a Natural Language Processing (NLP) based sentiment analysis system. The application allows users to enter a text review and receive a prediction indicating whether the sentiment is **positive** or **negative**, along with a confidence score.

The machine learning model was developed and trained in **Google Colab** using a dataset of product reviews. The trained model is integrated into a **Flask web application**, providing a simple and interactive user interface.

---

## 🚀 Features

* Sentiment classification (Positive / Negative)
* Confidence score display
* Web-based interface using Flask
* Real-time user input processing
* Clean and responsive UI

---

## 🛠️ Technologies Used

* Python
* Flask (Web Framework)
* TensorFlow / Keras (Model Training in Google Colab)
* HTML & CSS (Frontend Interface)
* Google Colab (Model development and training)

---

## 📂 Project Structure

```
ISY503_A3/
│
├── app.py
├── sentiment_model.h5        (trained model)
├── tokenizer.pkl            (text tokenizer)
├── templates/
│     └── index.html
└── README.md
```

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```
git clone https://github.com/your-username/ISY503_A3.git
cd ISY503_A3
```

### 2. Install dependencies

```
pip install flask tensorflow numpy
```

### 3. Run the application

```
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🧠 How It Works

1. User enters a review in the input field
2. The text is preprocessed and converted into numerical format
3. The trained model predicts the sentiment
4. The result (Positive/Negative) and confidence score are displayed

---

## ⚖️ Ethical Considerations

* The dataset may contain bias, which can affect prediction accuracy
* The model may misinterpret sarcasm or ambiguous language
* Incorrect predictions could influence user decisions
* Efforts were made to ensure balanced classification and fair output

---

## 📊 Limitations

* Model accuracy depends on training data quality
* Limited understanding of context and sarcasm
* Designed for demonstration purposes rather than production use




