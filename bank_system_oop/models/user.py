from abc import ABC, abstractmethod
from bank_system_oop.models.account import Account
from bank_system_oop.models.salary_account import SalaryAccount
from bank_system_oop.models.savings_account import SavingsAccount


class User(ABC):
    """
    Abstract class that represents a user.
    ...

    Attributes
    ----------
    ACCOUNT_TYPES: dict: cls - Holds information about the type of accounts that are available to users
    accounts: dict - All users accounts
    __id: int - Unique identifier for the user

    Methods
    -------
    withdraw - passes a request to account for withdrawal
    deposit - passes a request to account for deposit
    register_account - Creates and stores new account based on account type requested
    _store_account - stores new account after its been created
    _create_account - Calls cls method of Account to generate new account
    get_properties: abstract - Get class specific properties
    """

    ACCOUNT_TYPES = {
        'savings': SavingsAccount,
        'salary': SalaryAccount
    }

    def __init__(self, id_nr):
        self.accounts: dict[str: Account] = {}
        self.__id: int = id_nr

    @property
    def id(self):
        return self.__id

    def _store_account(self, account_type: str, account: Account) -> None:
        """Stores a new account"""

        self.accounts[account_type] = account

    def _create_account(self, account_type: str) -> Account:
        """Calls cls method of Account to return an instance of itself"""

        return self.ACCOUNT_TYPES[account_type].generate()

    def register_account(self, account: str) -> None:
        """Creates and stores new account"""

        new_account = self._create_account(account)
        self._store_account(account, new_account)

    def withdraw(self, account: str, amount: float) -> None:
        """Passes a request to account object for a withdrawal"""

        self.accounts[account].withdraw(amount)

    def deposit(self, account: str, amount: float) -> None:
        """Passes a request to account object for a deposit"""

        self.accounts[account].deposit(amount)

    @abstractmethod
    def get_properties(self):
        pass

    def __repr__(self):
        return '\n'.join([f"{key}: {self.__dict__[key]}" for key in self.__dict__])
