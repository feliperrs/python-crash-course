# ---------------------------------------------------------------------------- #
#!                             Passando uma lista                              #
# ---------------------------------------------------------------------------- #
def greet_users(names):
    """Exibe um simples Hello para cada usuario na lista"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)