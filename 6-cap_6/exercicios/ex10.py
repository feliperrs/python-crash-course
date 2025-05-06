# ---------------------------------------------------------------------------- #
#!                           6.10 Números favoritos                            #
# ---------------------------------------------------------------------------- #

# Modifique seu programa do Exercício 6.2 (página 140) para que cada pessoa possa ter mais de um número favorito.

# Depois, exiba o nome de cada pessoa com seus números favoritos.

favorite_number = {
    'joao': [23, 7],
    'bento': [16, 3],
    'marina': [99, 21, 45],
    'paulo': [12],
    'adriana': [8, 14]
}

for person, numbers in favorite_number.items():
    print(f"\nName: {person.title()}")
    print("Favorite numbers:")
    for number in numbers:
        print(f"  {number}")