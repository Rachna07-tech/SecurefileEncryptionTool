from cryptography.fernet import Fernet
import os
from key_manager import load_key

def encrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    os.makedirs("encrypted_files", exist_ok=True)

    filename = os.path.basename(file_path)

    output_path = os.path.join(
        "encrypted_files",
        filename + ".encrypted"
    )

    with open(output_path, "wb") as output:
        output.write(encrypted_data)

    return output_path