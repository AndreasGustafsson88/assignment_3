import random
from typing import Iterator


def filter_result(func):
    """
    Decorator for search results
    ...

    Filters result based on how long the result is.

    Returns object if len == 1
    Returns no match if len == 0
    Returns details on matching result if len > 1
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return 'No match!' if not result \
            else result[0] if len(result) == 1 \
            else f'Got more than one mach for search, please specify search:\n {[[user.get_properties()] for user in result]}!'

    return wrapper


def random_number_generator(a: int, b: int) -> Iterator[int]:
    """
    Generates a random number between a and b.

    Creates an Iterator with a list of randomly generated numbers between a - b.
    Yields next number for the list while there are numbers in the Iterator.
    """

    numbers = filter(lambda n: n, random.sample(range(a, b), b - a))

    while numbers:
        yield next(numbers)
