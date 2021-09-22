"""Main module for holding abstract Account class."""

from abc import ABC, abstractmethod
from bank_system_oop.utils.helper_functions import random_number_generator


class Account(ABC):
    """
    Abstract class to represent an account.

    ...
    Attributes
    ----------
    cls:
        _account_numbers: Iterator - Generate a random number.
    _amount: int - Balance of the account.
    _currency: str - Account currency.
    _nr: int - Unique identifier for each account.

    Methods
    -------
    cls:
        generate - Create an instance of itself.
    deposit - Make a deposit.
    withdraw - Make a withdrawal if enough funds.
    __repr__ - String representation of class properties.
    """

    _account_numbers = random_number_generator(100_000, 999_999)

    def __init__(self):
        """Init properties."""
        self._amount: int = 0
        self._currency: str = 'SEK'
        self._nr = next(self._account_numbers)

    @classmethod
    @abstractmethod
    def generate(cls):
        """Abstract method."""
        pass

    @abstractmethod
    def deposit(self, amount):
        """Abstract method."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Abstract method."""
        pass

    def __repr__(self):
        """Create a string representation of class properties."""
        return '\n'.join([f"{key}: {self.__dict__[key]}" for key in self.__dict__])
