from cryptography.fernet import Fernet
import os

KEY_FILE = "keys/secret.key"

def generate_key():
    os.makedirs("keys", exist_ok=True)

    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

    return True

def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()