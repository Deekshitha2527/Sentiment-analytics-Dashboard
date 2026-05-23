# 📊 Social Media Sentiment Analysis App

A Python-based application that analyzes the sentiment of user input text and classifies it as **Positive**, **Negative**, or **Neutral**.
The application also provides **data storage, visualization, and export features**, making it useful for basic data analysis tasks.

---

## 🚀 Features

* ✅ Sentiment Analysis using NLP (TextBlob)
* ✅ Improved handling of negation (e.g., "not good")
* ✅ GUI-based interface using Tkinter
* ✅ Stores results in SQLite database
* ✅ View analysis history
* ✅ Search text by keyword
* ✅ View sentiment statistics
* ✅ Data visualization (Pie Chart & Bar Chart)
* ✅ Export results to CSV file

---

## 🛠️ Tech Stack

* **Python**
* **TextBlob** (Natural Language Processing)
* **SQLite** (Database)
* **Tkinter** (GUI)
* **Matplotlib** (Data Visualization)

---

## 📂 Project Structure

```
sentiment_analysis/
│── app.py        # Main GUI application
│── db.py         # Database operations
│── sentiment.py  # Sentiment analysis logic
│── data.db       # SQLite database (auto-created)
│── sentiment_data.csv  # Exported data (optional)
```

---

## ⚙️ Installation & Setup

1. Clone the repository or download the project
2. Install required libraries:

```
pip install textblob matplotlib
python -m textblob.download_corpora
```

3. Run the application:

```
python app.py
```

---

## 🧪 How It Works

1. Enter text in the input field
2. Click **Analyze**
3. The app:

   * Calculates sentiment polarity using TextBlob
   * Applies basic negation handling
   * Classifies sentiment as Positive, Negative, or Neutral
4. Stores the result in a SQLite database
5. Allows viewing history, statistics, and charts

---

## 📊 Data Visualization

The application provides:

* 📈 **Bar Chart** → Shows count of each sentiment
* 🥧 **Pie Chart** → Shows percentage distribution

These help in understanding overall sentiment trends.

---

## ⚠️ Limitations

* Basic NLP model (TextBlob) may not handle:

  * Sarcasm
  * Complex language
  * Context-heavy sentences
* Accuracy can be improved using advanced models like BERT

---

## 🔮 Future Improvements

* Use advanced NLP models (HuggingFace / BERT)
* Add real-time social media data (Twitter API)
* Improve UI/UX design
* Deploy as a web application

---`

## 👩‍💻 Author

[Deekshitha N]
