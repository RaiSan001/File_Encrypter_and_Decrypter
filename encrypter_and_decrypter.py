from fileinput import filename
from cryptography.fernet import Fernet
import os

#generating a fernet key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

#loading key
def load_key():
    return open("secret.key", "rb").read()

#encrypting file
def encrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        file_dat = file.read()

    encrypted_dat = fernet.encrypt(file_dat)
    with open(filename + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_dat)
    print(f"File '{filename}' encrypted as '{filename}.encrypted'")


#decrypting file
def decrypt_file(filename, key):
    fernet = Fernet(key)
    with open(filename, "rb") as encrypted_file:
        encrypted_dat = encrypted_file.read()

    decrypted_dat = fernet.decrypt(encrypted_dat)
    decrypted_filename = filename.replace(".encrypted", ".decrypted")
    with open(decrypted_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_dat)
    print(f"File '{filename}' decrypted to '{decrypted_filename}'.")

#main function
def main():
    #generating key or loading key
    if not os.path.exists("secret.key"):
        key = generate_key()
    else:
        key = load_key()

    action = input("Press 'E' for Encrypt and 'D' for Decrypt. ").strip()
    filename = input("Enter filename: ").strip()

    if action.lower() == "e":
        encrypt_file(filename, key)
    elif action.lower() == "d":
        decrypt_file(filename, key)
    else:
        print("Invalid. Use 'E' or 'D'")


if __name__ == "__main__":
    main()