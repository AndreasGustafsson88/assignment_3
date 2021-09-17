from bank_system_oop.models.user import User


class PrivateUser(User):
    """
    Class for private users of the bank, subclasses of User.
    ...

    Attributes - Inherited
    ----------
    ACCOUNT_TYPES: dict: cls - Holds information about the type of accounts that are available to users
    accounts: dict - All users accounts
    __id: int - Unique identifier for the user

    Attributes
    ----------
    first_name: str - first name of person
    surname: str - surname of person

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

    def __init__(self, first_name, surname, id_nr):
        self.surname: str = surname
        self.first_name: str = first_name
        super().__init__(id_nr)

    def get_properties(self) -> tuple:
        """Returns class specific properties"""

        return self.first_name, self.surname, self.id
