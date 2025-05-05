# ---------------------------------------------------------------------------- #
#!             Percorrendo todos os pares chave-valor com um loop              #
# ---------------------------------------------------------------------------- #

user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

# ---------------------------------------------------------------------------- #
#!          Percorrendo todas as chaves de um dicionario com um loop           #
# ---------------------------------------------------------------------------- #

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name.title())


friends = ['phil', 'sarah']

for name in favorite_languages:
    print(f'Hi {name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\n\t{name.title()}, I see ou love {language}\n')
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll')


# ---------------------------------------------------------------------------- #
#! Percorrendo as chaves de um dicionario com um loop em uma ordem especifica  #
# ---------------------------------------------------------------------------- #

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll')

# ---------------------------------------------------------------------------- #
#!          Percorrendo todos os valores de um dicionario com um loop          #
# ---------------------------------------------------------------------------- #

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

print('The following languages have been mentioned:')

for language in favorite_languages.values():
    print(language.title())

print('\nThe following languages have been mentioned:')

for language in set(favorite_languages.values()):
    print(language.title())