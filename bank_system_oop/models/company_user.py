from bank_system_oop.models.user import User


class CompanyUser(User):
    """
    Class for company customers of the bank, subclasses of User.
    ...

    Attributes - Inherited
    ----------
    ACCOUNT_TYPES: dict: cls - Holds information about the type of accounts that are available to users
    accounts: dict - All users accounts
    __id: int - Unique identifier for the user

    Attributes
    ----------
    name: str - name of the company

    Methods - Inherited
    -------
    withdraw - passes a request to account for withdrawal
    deposit - passes a request to account for deposit
    register_account - Creates and stores new account based on account type requested
    _store_account - stores new account after its been created
    _create_account - Calls cls method of Account to generate new account

    Methods
    .......
    get_properties - Used by @filter_result returns class specific properties
    """

    def __init__(self, name, id_nr):
        self.name = name
        super().__init__(id_nr)

    def get_properties(self) -> tuple:
        """Returns class specific properties"""

        return self.name, self.id
