from shortener.models import ShortenedURL
import random
import string


def generate_short_code() -> str:
    """
    Generates a unique short code for a ShortenedURL object.
    """
    characters = string.ascii_letters + string.digits
    code_length = 6
    while True:
        short_code = ''.join(random.choice(characters)
                             for _ in range(code_length))
        if not ShortenedURL.objects.filter(short_code=short_code).exists():
            return short_code
