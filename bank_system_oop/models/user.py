"""Main module for holding User class."""

from abc import ABC, abstractmethod
from bank_system_oop.models.account import Account
from bank_system_oop.models.salary_account import SalaryAccount
from bank_system_oop.models.savings_account import SavingsAccount


class User(ABC):
    """
    Abstract class to represents a user.

    ...
    Attributes
    ----------
    cls:
        ACCOUNT_TYPES: dict - Holds information about the type of accounts that are available to users.
    @property:
        id: int - Getter of __id
    accounts: dict - All the users accounts.
    __id: int - Unique identifier for the user (Private).

    Methods
    -------
    register_account - Register the user.
    withdraw - Pass a request to account for withdrawal.
    deposit - Pass a request to account for deposit.
    get_properties: abstract - Get class specific properties.
    __repr__ - String representation of class attributes.
    """

    ACCOUNT_TYPES = {
        'savings': SavingsAccount,
        'salary': SalaryAccount
    }

    def __init__(self, id_nr):
        """Init properties."""
        self.accounts: dict[str: Account] = {}
        self.__id: int = id_nr

    @property
    def id(self):
        """Getter of attribute __id."""
        return self.__id

    @abstractmethod
    def register_account(self, account: str):
        """Abstract method."""
        pass

    @abstractmethod
    def withdraw(self, account: str, amount: float):
        """Abstract method."""
        pass

    @abstractmethod
    def deposit(self, account: str, amount: float):
        """Abstract method."""
        pass

    @abstractmethod
    def get_properties(self):
        """Abstract method."""
        pass

    def __repr__(self):
        """Create a string representation of class attributes."""
        return '\n'.join([f"{key}: {self.__dict__[key]}" for key in self.__dict__])
