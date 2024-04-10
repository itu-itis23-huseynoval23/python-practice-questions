import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

password_length = int(input("Enter the length of the password you want to generate: "))
password = generate_password(password_length)
print("Generated Password:", password)
