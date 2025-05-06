# ---------------------------------------------------------------------------- #
#!                                6.11 Cidades                                 #
# ---------------------------------------------------------------------------- #

# Crie um dicionário chamado cities.

# Utilize o nome de três cidades como chaves de seu dicionário.

# Crie um dicionário de informações sobre cada cidade e inclua o país em que a cidade está, sua população aproximada e um fato sobre essa cidade.

# O nome das chaves para o dicionário de cada cidade devem ser alguma coisa como country, population e fact.

# Exiba o nome de cada cidade e todas as informações que você armazenou a respeito.

cities = {
    'paris': {
        'country': 'frança',
        'population': 2148000,
        'fact': 'É conhecida como a cidade luz e abriga a Torre Eiffel.'
    },
    'tokyo': {
        'country': 'japão',
        'population': 13960000,
        'fact': 'É a área metropolitana mais populosa do mundo.'
    },
    'rio de janeiro': {
        'country': 'brasil',
        'population': 6748000,
        'fact': 'É famosa pelo Cristo Redentor e pelo carnaval.'
    }
}

for city, information in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population: {information['population']}")
    print(f"Fact: {information['fact']}")
