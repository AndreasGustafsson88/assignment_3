"""Main module for holding helper functions."""

import random
from typing import Iterator


def filter_result(func):
    """
    Decorator for search results.

    Filters result based on how long the result is.

    Returns object if len == 1
    Returns no match if len == 0
    Returns details on matching result if len > 1
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return 'No match!' if not result \
            else result[0] if len(result) == 1 \
            else f'Found more than one match, please specify search:\n {[user.get_properties() for user in result]}!'

    return wrapper


def random_number_generator(a: int, b: int) -> Iterator[int]:
    """
    Generate a random number between a and b.

    Creates a list with all numbers from a to b.
    Runs while there are numbers in the list. For each cycle yields a random number and removes it.
    """
    numbers = [val for val in range(a, b)]

    while numbers:
        yield numbers.pop(random.randint(0, len(numbers) - 1))
