import string
import secrets
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase

def generate_random_password(length:int) -> str:
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(int(length)))