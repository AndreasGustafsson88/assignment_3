"""Main module for holding Mapper class."""

from functools import reduce
from bank_system_oop.utils.helper_functions import random_number_generator


class Mapper(dict):
    """
    A class to handle custom mapping features for fast search of the bank.

    ...
    Attributes
    ----------
    cls:
        _mapping_gen: Iterator: - Initiate the Iterator for generating mapping values.
    mapping_value: int - Mapping value used for mapping user params to unique ids.

    Methods
    -------
    set_mapping_value - Calls for the Iterator to fetch a new value and assign it to self.mapping_value
    create_mapping - Creates and stores the mapping value for every argument passed to method
    search_mapping_nrs - Calls for a lookup in __dict__ of all arguments passed to the method.
    """

    _mapping_gen = random_number_generator(1_000_000, 3_000_000)

    def __init__(self):
        """Init properties."""
        self.mapping_value: int = 0

    def set_mapping_value(self) -> None:
        """Update the mapping value, called every time a new mapping is created."""
        self.mapping_value = next(self._mapping_gen)

    def create_mapping(self, args: tuple):
        """
        Create mapping.

        ...
        Stores each argument as a key with an assigned number unique to all its arguments.

        E.g _index = {
            'Paul': [123456],
            'Mcbeth': [123456]
            int(social_id_nr): [123456]
        }

        For users with the same name there will be several values to the same key. E.g 'Paul': [123456, 456123]
        """
        self.set_mapping_value()

        # Iterate over the arguments and append mapping to argument. If no arg exists as key a new one is created.
        for arg in args:
            if not self.__dict__.get(arg, None):
                self.__dict__[arg] = [self.mapping_value]
            else:
                self.__dict__[arg].append(self.mapping_value)

    def search_mapping_nrs(self, *args):
        """
        Search mapping_nrs.

        Fetches all mapping_nrs for matching result for each argument in the search.

        Matching numbers are added to matching_index.
        If an argument doesn't have a match it will append an empty string.
        (We need an iterable that returns None when iterating in the reduce function).

        E.g.
        _index = {
            'Paul': [123456, 456123],
            'Mcbeth': [123456]
            }

        args = ('Paul', 'Mcbeth')
        matching_index = [[123456, 456123], [123456]]

        Return a set of matching values for each mapping_nr using intersection from set and reduce -> {123456}
        """
        matching_indexes = [self.__dict__.get(arg, '') for arg in args]

        return reduce(lambda a, b: set(a).intersection(set(b)), matching_indexes)
