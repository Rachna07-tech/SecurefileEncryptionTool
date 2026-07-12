from cryptography.fernet import Fernet, InvalidToken
import os
from key_manager import load_key

def decrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    filename = os.path.basename(file_path)

    if filename.endswith(".encrypted"):
        filename = filename[:-10]

    os.makedirs("decrypted_files", exist_ok=True)

    output_path = os.path.join(
        "decrypted_files",
        filename
    )

    with open(output_path, "wb") as output:
        output.write(decrypted_data)

    return output_path