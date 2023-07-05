import random
import string


def generate_username(longitud):
    characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(characters)
                       for _ in range(longitud))
    return username


username_length = 8
username = generate_username(username_length)
print("Generated username:", username)
