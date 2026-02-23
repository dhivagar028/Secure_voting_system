import sqlite3


def create_database():
    conn = sqlite3.connect("voting.db")
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            has_voted INTEGER DEFAULT 0
        )
    """)

    # Votes table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            encrypted_vote TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("✅ Database (users + votes) created successfully!")


if __name__ == "__main__":
    create_database()