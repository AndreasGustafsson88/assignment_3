from bank_system_oop.models.company_user import CompanyUser
from bank_system_oop.models.private_user import PrivateUser
from bank_system_oop.models.mapper import Mapper
from bank_system_oop.models.user import User
from bank_system_oop.utils.helper_functions import filter_result


class Bank:
    """
    A class to represent a bank.
    ...

    Attributes
    ----------
    USER_TYPES: dict: cls - stores the types of users that the bank has
    name: str - name of the bank
    _users: dict - Stores all the user data
    _index: Mapper - Mapper class to handle all key / value mapping for searches

    Methods
    -------
    _create_user - Sends args to user class and returns user object
    _store_user - Stores user in self._users dictionary
    registers_user - Registers a user with the bank
    search_user - Searches for user registered with the bank
    """

    USER_TYPES = {
        'private': PrivateUser,
        'company': CompanyUser
    }

    def __init__(self, name):
        self._name: str = name
        self._users: dict = {}
        self._index: Mapper = Mapper()

    def _create_user(self, user_type: str, user_data: tuple) -> User:
        """Creates and returns the user"""

        return self.USER_TYPES[user_type](*user_data)

    def _store_user(self, new_user: User) -> None:
        """
        User is stored in the _user dict as a user object with their unique nr as key.

        E.g _users = {
            123456: User(Paul, Mcbeth, social_id_nr)
            }
        """

        self._users[self._index.mapping_value] = new_user

    def register_user(self, user: str, *args) -> User:
        """Creates user and mapping then stores new user based on user type"""

        new_user = self._create_user(user, args)  # call for create user

        self._index.create_mapping(args)  # create mapping

        self._store_user(new_user)  # call for storing user data

        return new_user

    @filter_result
    def search_user(self, *args) -> list:
        """
        Search that works on both private and company customer and with different search arguments without iterating
        over every user.

        Gets a user object for every match. Returns list that is filtered through @filter_result decorator depending on
        how many matches was found.
        """

        # pass all search argument to search for mapping_nrs
        indexes = self._index.search_mapping_nrs(*args)

        # return each user that had matching mapping_nrs for every argument
        return [self._users.get(i) for i in indexes] if indexes else None

    def __repr__(self):
        return '\n'.join([f"{key}: {self.__dict__[key]}" for key in self.__dict__])
