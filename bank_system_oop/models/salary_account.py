"""Main module for holding SalaryAccount class."""

from bank_system_oop.models.account import Account
from bank_system_oop.models.custom_error import InsufficientFundsException


class SalaryAccount(Account):
    """
    Class for salary accounts for the users of the bank, subclass of Account.

    ...
    Attributes
    ----------
    interest_rate: float - Interest rate for current account type. Default 0.02.

    Methods
    -------
    cls:
        generate - Create instance of the class.
    deposit - Make a deposit.
    withdraw - Make a withdrawal if sufficient funds.
    sufficient_funds - Check if a withdrawal is possible.
    """

    def __init__(self):
        """Init properties."""
        self.interest_rate: float = 0.02
        super().__init__()

    @classmethod
    def generate(cls):
        """Class method for creating instance of class."""
        return cls()

    def deposit(self, amount: int) -> None:
        """Add amount to the existing account balance."""
        self._amount += amount

    def withdraw(self, amount: int) -> None:
        """Make a withdrawal if sufficient funds on the account else print an exception with explanation."""
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
