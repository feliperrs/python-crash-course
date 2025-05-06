# ---------------------------------------------------------------------------- #
#!                           7.9 Férias tão sonhadas                           #
# ---------------------------------------------------------------------------- #

# Crie uma pesquisa que pergunte aos usuários sobre as férias de seus sonhos.

# Crie um prompt mais ou menos assim: Se pudesse visitar qualquer lugar do mundo, para onde iria? 

# Inclua um bloco de código que exiba os resultados dessa pesquisa.

responses = {}

while True:
    name = input("\nQual o seu nome? ")
    place = input("Se pudesse visitar qualquer lugar do mundo, para onde iria?  ")

    responses[name] = place

    repeat = input("Existe outra pessoa para responder?(sim/nao) ")
    if repeat == 'nao':
        break

print("\n=== Resultado da Pesquisa ===")
for nome, lugar in responses.items():
    print(f"{nome.title()} gostaria de visitar {lugar}")