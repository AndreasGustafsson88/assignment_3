"""Main file for holding all information about globals."""

BANK = {}
USER_TYPES = ['private', 'company']
ACCOUNT_TYPES = ['savings', 'salary']
CURRENCY = 'SEK'
INTEREST_RATE = {
    'savings': 0.05,
    'salary': 0.02
}
USERS = {
    'Andreas': {
        'first_name': 'Andreas',
        'surname': 'Gustafsson',
        'id_nr': 123123
    },
    'carrot_inc': {
        'name': 'carrot',
        'id_nr': 456789
    }
}
