# ---------------------------------------------------------------------------- #
#!                             8.6 Nome de cidades                             #
# ---------------------------------------------------------------------------- #

# Escreva uma função chamada city_country() que recebe o nome de uma cidade e seu país. 

# A função deve retornar uma string formatada como esta:
# "Santiago, Chile"

# Chame sua função com pelo menos três pares cidade-país e exiba os valores retornados.

def city_country(city, country):
    print(f"{city.title()}, {country.title()}")

city_country('são paulo', 'brasil')
city_country('londres', 'inglaterra')
city_country('nova iorque', 'EUA')