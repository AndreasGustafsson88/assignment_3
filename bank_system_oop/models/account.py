"""Main module for holding abstract Account class."""

from abc import ABC, abstractmethod
from bank_system_oop.models.custom_error import InsufficientFundsException
from bank_system_oop.utils.helper_functions import random_number_generator


class Account(ABC):
    """
    Abstract class to represent an account.

    ...
    Attributes
    ----------
    _account_numbers: Iterator: cls - Generates a random number
    _amount: int - balance of the account
    _currency: str - account currency
    _nr: int - unique identifier for each account
    balance: int - Checks the current amount

    Methods
    -------
    _deposit: - makes a deposit
    _withdraw: - makes a withdrawal if enough funds
    generate: cls - Creates instance of the class
    sufficient_funds - Checks if a withdrawal is possible
    """

    _account_numbers = random_number_generator(100_000, 999_999)

    def __init__(self):
        """Init properties."""
        self._amount: int = 0
        self._currency: str = 'SEK'
        self._nr = next(self._account_numbers)

    @classmethod
    def generate(cls):
        """Class method for creating instance of class."""
        return cls()

    def deposit(self, amount: int) -> None:
        """Add amount to the existing account balance."""
        self._amount += amount

    def withdraw(self, amount: int) -> None:
        """Make a withdrawal if sufficient funds on the account else prints an exception with explanation."""
        try:
            if self.sufficient_funds(amount):
                self._amount -= amount
            else:
                raise InsufficientFundsException(self._amount, amount, self._currency)

        except InsufficientFundsException as e:
            print(e)

    def sufficient_funds(self, amount: int) -> bool:
        """Check if a withdrawal is possible."""
        return self._amount >= amount

    def __repr__(self):
        """Create a string representation of class properties."""
        return '\n'.join([f"{key}: {self.__dict__[key]}" for key in self.__dict__])
