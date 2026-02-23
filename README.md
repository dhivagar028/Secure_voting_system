# Secure Voting System

A mini secure voting system built using Python and SQLite.

## Features
- User registration & login
- Password hashing using SHA256
- Encrypted vote storage using Fernet
- One-person-one-vote logic
- Admin result panel

## How to Run

1. Install dependencies:
   pip install cryptography

2. Create database:
   python database.py

3. Generate encryption key:
   python encryption.py

4. Register user:
   python auth.py

5. Cast vote:
   python voting.py

6. View results:
   python admin.py

Admin password: admin123