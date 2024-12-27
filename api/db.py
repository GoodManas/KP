import sqlite3

users = sqlite3.connect('db/users.db')

if __name__ == "__main__":
  users.execute('''
    CREATE TABLE IF NOT EXISTS users (
      id INTEGER PRIMARY KEY,
      login TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL
    );
    ''')