import sqlite3

def connect():
    return sqlite3.connect("data.db")

def create_tables():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sentiments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        sentiment TEXT,
        score REAL
    )
    """)

    conn.commit()
    conn.close()

def register_user(username, password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username, password)
    )

    conn.commit()
    conn.close()

def login_user(username, password):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user

def insert_data(text, sentiment, score):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO sentiments(text,sentiment,score) VALUES(?,?,?)",
        (text, sentiment, score)
    )

    conn.commit()
    conn.close()

def fetch_all():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM sentiments")

    data = cursor.fetchall()

    conn.close()

    return data

def get_stats():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM sentiments")
    total = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM sentiments WHERE sentiment='Positive'"
    )
    pos = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM sentiments WHERE sentiment='Negative'"
    )
    neg = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM sentiments WHERE sentiment='Neutral'"
    )
    neu = cursor.fetchone()[0]

    conn.close()

    return total, pos, neg, neu