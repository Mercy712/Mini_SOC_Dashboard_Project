
from cryptography.fernet import Fernet      # the cyrptography module gives simple, strong symmeric encryption (same key to encrypt and decrypt)
import os  



def load_key(key_path="logs/secret.key"):
    with open(key_path, "rb") as key_file:
        return key_file.read()

key = load_key()
fernet = Fernet(key)

# Example usage
log_entry = "2025-08-19 23:10:00 | SUCCESS"
encrypted = fernet.encrypt(log_entry.encode())






