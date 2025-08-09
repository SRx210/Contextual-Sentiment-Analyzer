# 🎬 IMDb Sentiment Analyzer

This project is a sentiment analysis tool that predicts whether a movie review is **positive** or **negative** using machine learning.

Built using:
- ✅ TF-IDF (Text Vectorization)
- ✅ Logistic Regression (Classifier)
- ✅ Streamlit (Frontend Web App)

---

## 📊 Dataset

- **IMDb Movie Review Dataset**
- Source: [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews)
- 50,000 movie reviews labeled as `positive` or `negative`

---

## 🚀 How It Works

1. Clean and preprocess text (remove punctuation, lowercase, etc.)
2. Convert text into vectors using **TF-IDF**
3. Train a **Logistic Regression** model
4. Save the model with **Pickle (.pkl)**
5. Use **Streamlit** to create a user interface where anyone can:
   - Enter a movie review
   - Get the predicted sentiment instantly!

---

## 🧪 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/SRx210/Contextual-Sentiment-Analyzer.git
cd imdb-sentiment-analyzer
````

### 2. Install dependencies
* Python 3.8+
* scikit-learn
* pandas
* numpy
* streamlit
* pickle
### 3. Run the app

```bash
streamlit run app.py
```
---

## ✅ Future Plans

* [ ] Add BERT-based version for improved accuracy
* [ ] Deploy online using Streamlit Cloud
* [ ] Visualize word clouds and predictions

---

## 📬 Contact

[Sohan Raut](https://github.com/SRx210)

---

⭐ If you like this project, give it a star on GitHub!

````