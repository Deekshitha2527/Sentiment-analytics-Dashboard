from flask import Flask, render_template, request, redirect, session
from sentiment import get_sentiment
from db import *

import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

app.secret_key = "secret123"

create_tables()

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        register_user(username, password)

        return redirect("/login")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = login_user(username, password)

        if user:
            session["user"] = username
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

    result = None
    score = None

    if request.method == "POST":

        text = request.form["text"]

        result, score = get_sentiment(text)

        insert_data(text, result, score)

    total, pos, neg, neu = get_stats()

    return render_template(
        "index.html",
        result=result,
        score=score,
        total=total,
        pos=pos,
        neg=neg,
        neu=neu
    )

@app.route("/history")
def history():

    data = fetch_all()

    return render_template(
        "history.html",
        data=data
    )

@app.route("/chart")
def chart():

    total, pos, neg, neu = get_stats()

    labels = ["Positive", "Negative", "Neutral"]
    values = [pos, neg, neu]

    plt.figure(figsize=(6,6))

    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.title("Sentiment Distribution")

    plt.savefig("static/chart.png")

    return render_template("chart.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["file"]

        df = pd.read_csv(file)

        for text in df["text"]:

            sentiment, score = get_sentiment(str(text))

            insert_data(text, sentiment, score)

        return redirect("/history")

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)