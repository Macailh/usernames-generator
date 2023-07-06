import random
import string


def generate_username(length):
    consonants = ''.join(random.choice(string.ascii_lowercase)
                         for _ in range(length // 2))
    vowels = ''.join(random.choice('aeiou')
                     for _ in range(length - (length // 2)))
    username = ''.join(random.choice(consonants + vowels)
                       for _ in range(length))
    return username


username_length = 8
generated_username = generate_username(username_length)
print("Generated username:", generated_username)
