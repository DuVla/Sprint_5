import random
import string

def generate_login(name='test', surname='testov', cohort='5555'):
    random_digits = "".join(random.choices(string.digits, k=3))
    return f"{name}_{surname}_{cohort}_{random_digits}@yandex.ru"

def generate_password(length=10):
    characters = string.ascii_letters + string.digits
    return "".join(random.choices(string.ascii_letters, k=length))