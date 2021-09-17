from bank_system_oop.models.account import Account


class SavingsAccount(Account):
    """
    Class for savings accounts for the users of the bank, subclass of Account.
    ...

    Attributes - Inherited
    ----------------------
    _account_numbers: generator: cls -- Generates a random number
    _amount: int -- balance of the account
    _currency: str -- account currency
    _nr: int -- unique identifier for each account
    balance: int - Checks the current amount

    Attributes
    ----------
    interest_rate: float - interest rate for current account type, default 0.05

    Methods - Inherited
    -------
    generate: cls - Creates instance of the class
    _deposit - makes a deposit
    _withdraw - makes a withdrawal
    sufficient_funds - checks if a withdrawal is possible
    """

    def __init__(self):
        self.interest_rate: float = 0.05
        super().__init__()
