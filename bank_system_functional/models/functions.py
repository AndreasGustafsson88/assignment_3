import random
from typing import Iterator
from bank_system_functional.models.globals import *


def random_number_generator(a: int, b: int) -> Iterator[int]:
    """
    Generates a random number between a and b.

    Creates a list with all numbers from a to b.
    Runs while there are numbers in the list. For each cycle yields a random number and removes it.
    """

    numbers = [val for val in range(a, b)]

    while numbers:
        yield numbers.pop(random.randint(0, len(numbers) - 1))

number_gen = random_number_generator(100, 999)


def create_private_user(first_name: str, surname: str, id_nr: int) -> None:
    BANK[id_nr] = {
        'id': id_nr,
        'first_name': first_name,
        'surname': surname,
        'accounts': {}
    }


def create_company_user(name: str, id_nr: int) -> None:
    BANK[id_nr] = {
        'id': id_nr,
        'name': name,
        'accounts': {}
    }


def create_user(user_type: str, **kwargs) -> None:
    """Creates user in global bank dict"""

    if user_type not in USER_TYPES:
        return

    create_private_user(**kwargs) if user_type == 'private' else create_company_user(**kwargs)


def register_account(account_type: str, id_nr: int) -> None:
    """Registers account for user"""

    if account_type not in ACCOUNT_TYPES:
        return

    BANK[id_nr]['accounts'][account_type] = {
        'nr': next(number_gen),
        'amount': 0,
        'currency': CURRENCY,
        'interest_rate': INTEREST_RATE[account_type]
    }


def search_matches(user, *args) -> bool:
    search_values = {
        BANK[user].get('first_name', 0),
        BANK[user].get('surname', 0),
        BANK[user].get('name', 0),
    }

    return set(args).intersection(search_values) == set(args)


def search_private_user(first_name: str, surname: str) -> list:
    return [BANK[user] for user in BANK if search_matches(user, first_name, surname)]


def search_company_user(name: str) -> list:
    return [BANK[user] for user in BANK if search_matches(user, name)]


def deposit(account: str, amount: int, id_nr: int) -> None:
    BANK[id_nr]['accounts'][account]['amount'] += amount


def sufficient_funds(account: dict, amount: int) -> bool:
    return account['amount'] >= amount


def charge(account: dict, amount: int):
    account['amount'] -= amount


def withdraw(account: str, amount: int, id_nr: int) -> None:
    account = BANK[id_nr]['accounts'][account]

    if sufficient_funds(account, amount):
        charge(account, amount)
    else:
        print('Not enough funds')