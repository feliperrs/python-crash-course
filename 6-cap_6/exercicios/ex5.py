# ---------------------------------------------------------------------------- #
#!                                  6.5 Rios                                   #
# ---------------------------------------------------------------------------- #

# Crie um dicionário contendo os três principais rios e o país por onde cada rio passa. Use um par chave-valor por exemplo como 'nile': 'egypt'.

# Use um loop para exibir uma frase sobre cada rio, como: O Nilo atravessa o Egito.

# Use um loop para exibir o nome de cada rio incluído no dicionário.

# Use um loop para exibir o nome de cada país incluído no dicionário.

rivers = {
'Amazonas': 'Brasil',
'Nilo': 'Egito',
'Yangtzé': 'China'
}

for rio, pais in rivers.items():
    print(f'O {rio} atravessa o {pais}\n')

for rio in rivers:
    print(f'- {rio}')

for pais in rivers.values():
    print(f'- {pais}')