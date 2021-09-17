from bank_system_functional.models.functions import *
from bank_system_oop.models.bank import Bank

"""
Course: Effective Programming - Assignment 3
Student: Andreas Gustafsson

"""


def simple_banking_management_oop():
    # Initiate bank
    bank = Bank('My_bank')

    # Create users, choose between private and company, return user directly if needed
    andreas = bank.register_user('private', 'Ricky', 'Wysocki', 222222)
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
    andreas.register_account('savings')
    andreas.register_account('salary')

    # Deposit to specified account or access directly from account
    andreas.deposit('savings', 100)
    andreas.accounts['savings'].deposit(100)
    andreas.deposit('salary', 20)

    # Make a withdrawal if sufficient funds
    andreas.withdraw('savings', 50)

    # Throws an exception with explanation
    andreas.withdraw('salary', 30)


def simple_banking_management_functional():

    # Initiate generator

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
    simple_banking_management_functional()
    simple_banking_management_oop()
