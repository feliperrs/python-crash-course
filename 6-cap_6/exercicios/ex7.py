# ---------------------------------------------------------------------------- #
#!                                 6.7 Pessoas                                 #
# ---------------------------------------------------------------------------- #

# Comece com o programa escrito para Exercício 6.1 (página 140).

# Crie dois dicionários novos representando pessoas diferentes e armazene todos os três dicionários em uma lista chamada people.

# Percorra sua lista de pessoas com um loop. 

# À medida que percorre a lista, exiba tudo o que sabe sobre cada pessoa.

person_0 = {
    'first_name' : 'joão',
    'last_name' : 'pereira',
    'age' : 23,
    'city' : 'curitiba'
    }

person_1 = {
    'first_name' : 'gabriel',
    'last_name' : 'santos',
    'age' : 34,
    'city' : 'rio de janeiro'
    }

person_2 = {
    'first_name' : 'matheus',
    'last_name' : 'carvalho',
    'age' : 19,
    'city' : 'sao paulo'
    }

person_list = [person_0, person_1, person_2]

for person in person_list:
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}\n")