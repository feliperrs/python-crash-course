# ---------------------------------------------------------------------------- #
#!                       Um dicionario em um dicionario                        #
# ---------------------------------------------------------------------------- #

users = {
    'aeinstein': {
        'first' : 'albert',
        'second' : 'einstein',
        'location' : 'princeton'
    },
    'mcurie' : {
        'first' : 'marie',
        'second' : 'curie',
        'location' : 'paris'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['second']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}") 