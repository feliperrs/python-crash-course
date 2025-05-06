# ---------------------------------------------------------------------------- #
#!                            6.9 Lugares favoritos                            #
# ---------------------------------------------------------------------------- #

# Crie um dicionário chamado favorite_places.

# Pense em três nomes para usar como chave no dicionário e armazene de um a três lugares favoritos por cada pessoa.

# Percorra o dicionário com um loop e exiba o nome de cada pessoa e seus lugares favoritos.

favorite_places = {
    'ana': ['paris', 'roma', 'lisboa'],
    'bruno': ['tóquio'],
    'carla': ['londres', 'bariloche']
}


for name, places in favorite_places.items():
    print(f"\nName: {name.title()}")
    print("Favorite places:")
    for place in places:
        print(f"-{place.title()}")