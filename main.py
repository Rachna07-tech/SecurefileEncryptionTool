from encrypt import encrypt_file
from decrypt import decrypt_file
import os
from gui import*

print("=== Secure File Encryption Tool ===")
print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Choose an option (1 or 2): ")

file_path = input("Enter the full path of the file: ")

if not os.path.exists(file_path):
    print("File not found!")
else:
    if choice == "1":
        encrypt_file(file_path)
    elif choice == "2":
        decrypt_file(file_path)
    else:
        print("Invalid choice!")