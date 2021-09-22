"""Main module for holding PrivateUser class."""

from bank_system_oop.models.account import Account
from bank_system_oop.models.user import User


class PrivateUser(User):
    """
    Class for private users of the bank, subclasses of User.

    ...
    Attributes
    ----------
    first_name: str - First name of person.
    surname: str - Surname of person.

    Methods
    -------
    _store_account - Store new account after its been created.
    _create_account - Call cls method of Account to generate new account.
    register_account - Create and store new account based on account type requested.
    withdraw - Pass a request to account for withdrawal.
    deposit - Pass a request to account for deposit.
    get_properties - Used by @filter_result returns class specific properties.
    """

    def __init__(self, first_name, surname, social_security_number):
        """Init properties."""
        self.surname: str = surname
        self.first_name: str = first_name
        super().__init__(id_nr=social_security_number)

    def _store_account(self, account_type: str, account: Account) -> None:
        """Store a new account."""
        self.accounts[account_type] = account

    def _create_account(self, account_type: str) -> Account:
        """Call cls method of Account to return an instance of itself."""
        return self.ACCOUNT_TYPES[account_type].generate()

    def register_account(self, account: str) -> None:
        """Create and stores new account."""
        new_account = self._create_account(account)
        self._store_account(account, new_account)

    def withdraw(self, account: str, amount: float) -> None:
        """Pass a request to account object for a withdrawal."""
        self.accounts[account].withdraw(amount)

    def deposit(self, account: str, amount: float) -> None:
        """Pass a request to account object for a deposit."""
        self.accounts[account].deposit(amount)

    def get_properties(self) -> tuple:
        """Return class specific properties."""
        return self.first_name, self.surname, self.id
