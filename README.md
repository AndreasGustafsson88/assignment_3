## Bank Management System

A basic system for small banking tasks such as:
* **Register users**
* **User search**
* **Open accounts**
* **Deposit and withdrawal**

The project contains an OOP solution as well as a functional. Emphasis is on the OOP version.

### Main problem encountered

***Slightly self inflected since I:***
* *Wanted the bank to have more than 1 customer with the same first and last name and a dict structure for fast search*
* *Used different user types with different properties and only wanted one search function*
* *Really didn't want to iterate over all user data for the search*

>The bank needs to quickly be able to find a BankAccount just by simply passing in the first & last name of a person.
>Implement this functionality, in which class should this be located?

First thought was to use a social_security_number as a key for user information search.
The task says to be able to search for first and last name. By using those as keys
I would restrict the bank to only one user with the same name.

I decided to try and make a fairly generic search that could handle different user types with different properties.
And also different search arguments. E.g. search for a combination of all properties vs only using name. 

Initially I went with a tuple key built up of (first_name, surname, social_security_number) or (name, social_security_number) for company users.

I would then iterate through every user in the bank and ask that user if all the search arguments are present among its properties.
Iterating both through all users and its properties didn't seem very optimal.

Initially I choose a dict structure for the sake of quickly finding specific users and also their bank accounts.
But I ended up iterating over the keys and not using the structure to its intended functionality.

### Solution

I built a mapper class to map an identifier number to every combination of user properties.
So all registered users gets a unique id which is used as key instead of the tuples previously used. 
This id is then mapped to every argument of the user.

When searching all search params are looked up first in the mapper class. Then returns a key which is used to
access user data directly from the bank.

Sacrificing som space for the application but greatly increases search speed.

### Result

**Old search**

* Average search time over 10 iterations with 1_000_000 users and 4 different searches: 6191224010.0 ns

**New search**
* 9 / 10 searches took 0 ns
* Average search time over 10 iterations with 1_000_000 users and 4 different searches: 100150.0 ns

Result is about 600_000 times faster for this example.

### Thoughts on improvements

* Use different mapping values, not sure int is the best.
* Would be fun to try and use a list structure and have the mapping class map to an index position.
* Use numpy for handling list operations.

### Usage Example

````python
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
````
