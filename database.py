import sqlite3

def init_db():
    conn = sqlite3.connect("chat_logs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            bot_response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_conversation(user_message, bot_response):
    conn = sqlite3.connect("chat_logs.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conversations (user_message, bot_response) VALUES (?, ?)",
        (user_message, bot_response)
    )
    conn.commit()
    conn.close()

def get_all_conversations():
    conn = sqlite3.connect("chat_logs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conversations ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows