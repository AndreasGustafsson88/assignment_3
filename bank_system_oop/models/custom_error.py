"""Main module for holding custom error classes."""


class InsufficientFundsException(Exception):
    """Class for handling errors when not enough funds in account."""

    def __init__(self, current_amount, requested_amount, currency):
        """Init properties."""
        self.current_amount: int = current_amount
        self.requested_amount: int = requested_amount
        super().__init__(
            f'Not enough funds. Current: {current_amount}{currency} Requested {requested_amount}{currency}. '
            f'After transaction {current_amount - requested_amount}{currency}'
        )
