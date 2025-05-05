# ---------------------------------------------------------------------------- #
#!                          Uma lista de dicionarios                           #
# ---------------------------------------------------------------------------- #

favorite_language = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell']
}

for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")