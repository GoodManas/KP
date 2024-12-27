import sqlite3

db = sqlite3.connect('db/time_tracking.db')

if __name__ == "__main__":
  db.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY,
      login TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL
    );
    ''')