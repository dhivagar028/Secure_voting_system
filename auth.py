import sqlite3
import hashlib


def create_connection():
    return sqlite3.connect("voting.db")


# 🔐 Hash Password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# 👤 Register User
def register_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    password_hash = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        print("✅ User registered successfully!")

    except sqlite3.IntegrityError:
        print("❌ Username already exists!")

    conn.close()
# 🔑 Login User
def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password_hash, has_voted FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result is None:
        print("❌ User not found!")
        return None

    stored_hash, has_voted = result

    if stored_hash == hash_password(password):
        print("✅ Login successful!")
        return has_voted
    else:
        print("❌ Incorrect password!")
        return None


# 🔎 Test Registration
if __name__ == "__main__":
    choice = input("1. Register\n2. Login\nChoose option: ")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if choice == "1":
        register_user(username, password)
    elif choice == "2":
        login_user(username, password)
    else:
        print("Invalid option")