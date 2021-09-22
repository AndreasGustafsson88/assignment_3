"""Main module for holding CompanyUser."""

from bank_system_oop.models.account import Account
from bank_system_oop.models.user import User


class CompanyUser(User):
    """
    Class for company customers of the bank, subclasses of User.

    ...
    Attributes
    ----------
    name: str - Name of the company.

    Methods
    -------
    _store_account - Store new account after its been created.
    _create_account - Call cls method of Account to generate new account.
    register_account - Create and store new account based on account type requested.
    withdraw - Pass a request to account for withdrawal.
    deposit - Pass a request to account for deposit.
    get_properties - Used by @filter_result returns class specific properties.
    """

    def __init__(self, name, company_id):
        """Init properties."""
        self.name = name
        super().__init__(id_nr=company_id)

    def _store_account(self, account_type: str, account: Account) -> None:
        """Store a new account."""
        self.accounts[account_type] = account

    def _create_account(self, account_type: str) -> Account:
        """Call cls method of Account to return an instance of itself."""
        return self.ACCOUNT_TYPES[account_type].generate()

    def register_account(self, account: str) -> None:
        """Create and store new account."""
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
        return self.name, self.id
