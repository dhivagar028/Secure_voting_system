from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("secret.key", "rb").read()


def encrypt_vote(vote):
    key = load_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(vote.encode())
    return encrypted.decode()   # ✅ convert bytes → string


def decrypt_vote(encrypted_vote):
    key = load_key()
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_vote.encode())  # ✅ string → bytes
    return decrypted.decode()


if __name__ == "__main__":
    generate_key()
    print("🔑 Secret key generated successfully!")