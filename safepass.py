import secrets
import string
import pyperclip

def random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    random_characters = [secrets.choice(characters) for _ in range(length)]

    return ''.join(random_characters)



length_asked_to_user = int(input("Choose the length for your password: "))

safe_password = random_string(length_asked_to_user)
print(f'Your password is now copied to clipboard')
pyperclip.copy(safe_password)
