import hashlib
import json
import os

DATA_FILE = "vault.json"

def load_vault():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_vault(vault):
    with open(DATA_FILE, "w") as file:
        json.dump(vault, file)

def encrypt(password, master):
    return hashlib.sha256((password + master).encode()).hexdigest()

def main():
    master_password = input("Enter your master password: ")
    vault = load_vault()

    while True:
        choice = input("\nOptions: (s)ave, (v)iew, (q)uit: ").lower()
        if choice == 's':
            account = input("Account name: ")
            password = input("Account password: ")
            vault[account] = encrypt(password, master_password)
            save_vault(vault)
            print("Password saved!")
        elif choice == 'v':
            for account, encrypted_pass in vault.items():
                print(f"{account}: {encrypted_pass}")
        elif choice == 'q':
            break

if __name__ == "__main__":
    main()
