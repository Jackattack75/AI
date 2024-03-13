# programmer: Mr Sutton
# Date: 3/12/2024
# program: password Generator
# resource: https://www.youtube.com/watch?v=jRAAaDll34Q

import hashlib
import os
import getpass

def hash_password(password, salt):
    # Combine the password and salt and hash them using SHA-256
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

def main():
    # Prompt the user to enter a password without echoing characters
    password = getpass.getpass("Enter your password: ")

    # Generate a random salt
    salt = os.urandom(32).hex()

    # Hash the password using the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed Password:", hashed_password)

if __name__ == "__main__":
    main()