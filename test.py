import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%&*?"
    return "".join(random.choice(characters) for _ in range(length))

password = generate_password(16)
print(f"Dein neues Passwort: {password}")