import random
import string
import typer


def generate_username(length):
    """
    Generates a random username of the specified length.

    Args:
        length (int): The desired length of the username.

    Returns:
        str: The randomly generated username.

    """
    consonants = ''.join(random.choice(string.ascii_lowercase)
                         for _ in range(length // 2))
    vowels = ''.join(random.choice('aeiou')
                     for _ in range(length - (length // 2)))
    username = ''.join(random.choice(consonants + vowels)
                       for _ in range(length))
    return username


app = typer.Typer()


@app.command()
def generate(length: int):
    GENERATED_USERNAME = generate_username(length)
    typer.echo(f"Generated username: {GENERATED_USERNAME}")


if __name__ == "__main__":
    app()
