import sqlite3
from encryption import decrypt_vote


def create_connection():
    return sqlite3.connect("voting.db")


def view_results():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT encrypted_vote FROM votes")
    votes = cursor.fetchall()

    conn.close()

    if not votes:
        print("No votes cast yet.")
        return

    # Count votes
    results = {}

    for vote in votes:
        encrypted_vote = vote[0]
        decrypted_vote = decrypt_vote(encrypted_vote)

        if decrypted_vote in results:
            results[decrypted_vote] += 1
        else:
            results[decrypted_vote] = 1

    print("\n🗳 Voting Results (Decrypted)")
    print("-----------------------------")

    for candidate, count in results.items():
        print(f"{candidate} : {count} votes")

    # Find winner
    winner = max(results, key=results.get)
    print("\n🏆 Winner:", winner)


if __name__ == "__main__":
    print("🔐 Admin Panel")
    password = input("Enter admin password: ")

    # Simple admin password check (you can improve later)
    if password == "admin123":
        view_results()
    else:
        print("❌ Incorrect admin password!")