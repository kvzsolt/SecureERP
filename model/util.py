import random
import string

ALPHABET_LOWER = string.ascii_lowercase
NUMBERS = string.digits


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    random_lower_letters = "".join(random.choices(ALPHABET_LOWER, k=number_of_small_letters))
    random_upper_letters = "".join(random.choices(ALPHABET_LOWER.upper(), k=number_of_capital_letters))
    random_digits = "".join(random.choices(NUMBERS, k=number_of_digits))
    random_special_chars = "".join(random.choices(allowed_special_chars, k=number_of_special_chars))
    joined_string = random_lower_letters + random_upper_letters + random_digits + random_special_chars
    id_generated = "".join(random.sample(joined_string, k=len(joined_string)))
    return id_generated
