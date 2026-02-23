from encryption import encrypt_vote
import sqlite3


def create_connection():
    return sqlite3.connect("voting.db")


# 🗳 Cast Vote
def cast_vote(username, candidate):
    conn = create_connection()
    cursor = conn.cursor()

    # Check if user already voted
    cursor.execute(
        "SELECT has_voted FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()

    if result is None:
        print("❌ User not found!")
        conn.close()
        return

    has_voted = result[0]

    if has_voted == 1:
        print("❌ You have already voted. Cannot vote again.")
        conn.close()
        return

    # 🔐 Encrypt vote before storing
    encrypted = encrypt_vote(candidate)

    cursor.execute(
        "INSERT INTO votes (encrypted_vote) VALUES (?)",
        (encrypted,)
    )

    # Mark user as voted
    cursor.execute(
        "UPDATE users SET has_voted = 1 WHERE username = ?",
        (username,)
    )

    conn.commit()
    conn.close()

    print("✅ Vote cast successfully (Encrypted)!")


if __name__ == "__main__":
    username = input("Enter username: ")
    print("Candidates: A, B, C")
    candidate = input("Choose candidate: ")

    cast_vote(username, candidate)