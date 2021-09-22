"""Main file for holding all functions of the functional version of bank system."""

import random
from typing import Iterator
from bank_system_functional.models.globals import *


def random_number_generator(a: int, b: int) -> Iterator[int]:
    """
    Generate a random number between a and b.

    Creates a list with all numbers from a to b.
    Runs while there are numbers in the list. For each cycle yields a random number and removes it.
    """
    numbers = [val for val in range(a, b)]

    while numbers:
        yield numbers.pop(random.randint(0, len(numbers) - 1))

number_gen = random_number_generator(100, 999)


def create_private_user(first_name: str, surname: str, id_nr: int) -> None:
    """Store private user information in global."""
    BANK[id_nr] = {
        'id': id_nr,
        'first_name': first_name,
        'surname': surname,
        'accounts': {}
    }


def create_company_user(name: str, id_nr: int) -> None:
    """Store company user information in global."""
    BANK[id_nr] = {
        'id': id_nr,
        'name': name,
        'accounts': {}
    }


def create_user(user_type: str, **kwargs) -> None:
    """Store user in global bank dict."""
    if user_type not in USER_TYPES:  # Check if user_type is valid.
        return

    # Call appropriate function depending on usertype.
    create_private_user(**kwargs) if user_type == 'private' else create_company_user(**kwargs)


def register_account(account_type: str, id_nr: int) -> None:
    """Register account for user."""
    if account_type not in ACCOUNT_TYPES:  # Check if account_type is valid
        return

    BANK[id_nr]['accounts'][account_type] = {
        'nr': next(number_gen),
        'amount': 0,
        'currency': CURRENCY,
        'interest_rate': INTEREST_RATE[account_type]
    }


def search_matches(user, *args) -> bool:
    """Check if search argument matches saved information in global."""
    search_values = {
        BANK[user].get('first_name', 0),
        BANK[user].get('surname', 0),
        BANK[user].get('name', 0),
    }

    return set(args).intersection(search_values) == set(args)


def search_private_user(first_name: str, surname: str) -> list:
    """Search for private user."""
    return [BANK[user] for user in BANK if search_matches(user, first_name, surname)]


def search_company_user(name: str) -> list:
    """Search for company user."""
    return [BANK[user] for user in BANK if search_matches(user, name)]


def deposit(account: str, amount: int, id_nr: int) -> None:
    """Make a deposit to chosen account based on user from unique id_nr."""
    BANK[id_nr]['accounts'][account]['amount'] += amount


def sufficient_funds(account: dict, amount: int) -> bool:
    """Check current amount vs requested amount to withdraw."""
    return account['amount'] >= amount


def charge(account: dict, amount: int):
    """Make the withdrawal."""
    account['amount'] -= amount


def withdraw(account: str, amount: int, id_nr: int) -> None:
    """Call for a withdrawal if sufficient funds else return print statement."""
    account = BANK[id_nr]['accounts'][account]

    if sufficient_funds(account, amount):
        charge(account, amount)
    else:
        print('Not enough funds')
