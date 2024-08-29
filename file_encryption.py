from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'secret.key'.")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted_data)
    print(f"File '{file_path}' encrypted and saved as '{file_path}.enc'.")

def decrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(file_path.replace(".enc", ""), "wb") as file:
        file.write(decrypted_data)
    print(f"File '{file_path}' decrypted and saved as '{file_path.replace('.enc', '')}'.")
