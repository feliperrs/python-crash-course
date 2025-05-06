# ---------------------------------------------------------------------------- #
# !                                8.5 Cidades                                 #
# ---------------------------------------------------------------------------- #

# Escreva uma função chamada describe_city() que aceite o nome de uma cidade e de seu país.

# A função deve exibir uma simples frase, como Reykjavík fica na Islândia. Forneça ao parâmetro do país um valor default.

# Chame sua função para três cidades diferentes e, pelo menos, para uma que não esteja no país default.

def describe_city(city, country='Brasil'):
    print(f"{city.title()} fica no(a) {country.title()}")


describe_city('são paulo')
describe_city('porto alegre')
describe_city('buenos aires', 'argentina')
