# ---------------------------------------------------------------------------- #
#                           6.8 Animais de estimação                           #
# ---------------------------------------------------------------------------- #

# Crie vários dicionários, em que cada dicionário represente um animal de estimação diferente.

# Em cada dicionário inclua o tipo de animal e o nome do dono.

# Armazene esses dicionários em uma lista chamada pets.

# Depois, percorra sua lista com um loop e, enquanto faz isso, exiba tudo o que sabe sobre cada animal de estimação.

pets = []

pet = {
    'animal': 'cachorro',
    'nome': 'rex',
    'dono': 'ana'
}
pets.append(pet)

pet = {
    'animal': 'gato',
    'nome': 'mia',
    'dono': 'bruno'
}
pets.append(pet)

pet = {
    'animal': 'papagaio',
    'nome': 'louro',
    'dono': 'carlos'
}
pets.append(pet)

pet = {
    'animal': 'hamster',
    'nome': 'bolinha',
    'dono': 'débora'
}
pets.append(pet)

pet = {
    'animal': 'tartaruga',
    'nome': 'nina',
    'dono': 'eduardo'
}
pets.append(pet)

for pet in pets:
    print(f"Animal: {pet['animal'].title()}")
    print(f"Nome: {pet['nome'].title()}")
    print(f"Dono: {pet['dono'].title()}\n")