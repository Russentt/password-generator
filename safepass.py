import secrets
import string
import pyperclip

def random_string(length):
    if length >= 8:
        characters = string.ascii_letters + string.digits + string.punctuation
        random_characters = [secrets.choice(characters) for _ in range(length)]
        return ''.join(random_characters)
    else:
        raise ValueError("Length is too short")



print("This is a password generator. You must send a length equal or greather than 8")
length_asked_to_user = int(input("Choose the length for your password: "))

try:
    safe_password = random_string(length_asked_to_user)
    pyperclip.copy(safe_password)
    print("Your password is copied to clipboard")
except ValueError as e:
    print(f"Error: {e}")
