"""
Home assignment 3.

Course: Effective Programming - Assignment 3.
Student: Andreas Gustafsson.
"""

from bank_system_functional.models.functions import *
from bank_system_oop.models.bank import Bank


def simple_banking_management_oop():
    """Run main script for running usage examples of oop bank management system."""
    bank = Bank('My_bank')  # Initiate bank

    # Create users, choose between private and company, return user directly if needed
    ricky = bank.register_user('private', 'Ricky', 'Wysocki', 222222)
    bank.register_user('company', 'E_will_inc', 666666)
    bank.register_user('private', 'Paul', 'Mcbeth', 111111)
    bank.register_user('private', 'Page', 'Pierce', 121212)
    bank.register_user('private', 'Super', 'Man', 123456)
    bank.register_user('private', 'Ricky', 'Wysocki', 221122)

    # Search for user no match -> returns no match
    user = bank.search_user('Rikki', 'Whysolucky', 222222)
    print(user)

    # Search for user more than one match -> returns prompt to specify search and details about results
    user = bank.search_user('Ricky', 'Wysocki')
    print(user)

    # Search for user one match -> Returns user object
    user = bank.search_user('E_will_inc')
    print(user)

    # Same search works with different args for both private and company -> return user
    company_user = bank.search_user(666666)
    print(company_user)

    # Register an account, specify which type -> None
    ricky.register_account('savings')
    ricky.register_account('salary')

    # Deposit to specified account or access directly from account
    ricky.deposit('savings', 100)
    ricky.accounts['savings'].deposit(100)
    ricky.deposit('salary', 20)

    # Make a withdrawal if sufficient funds
    ricky.withdraw('savings', 50)

    # Prints an exception with explanation
    ricky.withdraw('salary', 30)
    ricky.accounts['salary'].withdraw(30)


def simple_banking_management_functional():
    """Run main script for running usage examples of functional bank management system."""
    create_user('private', **USERS['Andreas'])
    create_user('company', **USERS['carrot_inc'])

    result = search_private_user('Andreas', 'Gustafsson')
    result_2 = search_company_user('carrot')

    register_account('savings', USERS['Andreas']['id_nr'])
    register_account('salary', USERS['Andreas']['id_nr'])

    deposit('savings', 100, USERS['Andreas']['id_nr'])
    deposit('salary', 20, USERS['Andreas']['id_nr'])

    withdraw('savings', 50, USERS['Andreas']['id_nr'])
    withdraw('salary', 30, USERS['Andreas']['id_nr'])

    print(BANK[USERS['Andreas']['id_nr']])


if __name__ == "__main__":
    simple_banking_management_oop()
    simple_banking_management_functional()
