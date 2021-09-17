class InsufficientFundsException(Exception):
    """
    Class for handling errors when not enough funds in account
    ...
    """

    def __init__(self, message):
        super().__init__(message)
