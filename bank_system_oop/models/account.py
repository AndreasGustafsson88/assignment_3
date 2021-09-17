from abc import ABC
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
        self._amount: int = 0
        self._currency: str = 'SEK'
        self._nr = next(self._account_numbers)

    @property
    def balance(self):
        return self._amount

    @property
    def nr(self):
        return self._nr

    @classmethod
    def generate(cls):
        """Class method for creating instance of class"""

        return cls()

    def deposit(self, amount: int) -> None:
        """Adds amount to the existing account balance"""

        self._amount += amount

    def withdraw(self, amount: int) -> None:
        """Makes a withdrawal if sufficient funds on the account"""

        if self.sufficient_funds(amount):
            self._amount -= amount
        else:
            message = f'Not enough funds. Current: {self._amount} {self._currency}, ' \
                      f'requested {amount} {self._currency} After transaction {self._amount - amount} {self._currency}'
            raise InsufficientFundsException(message=message)

    def sufficient_funds(self, amount: int) -> bool:
        """Checks if a withdrawal is possible"""

        return self._amount >= amount

    def __repr__(self):
        return '\n'.join([f"{key}: {self.__dict__[key]}" for key in self.__dict__])
