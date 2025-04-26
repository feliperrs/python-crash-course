# ---------------------------------------------------------------------------- #
#!                                   Listas                                    #
# ---------------------------------------------------------------------------- #

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# consultando as bicicletas nos indices 1 e 3

print(bicycles[1])
print(bicycles[3])

# acessando o ultimo item da lista

print(bicycles[-1])

# acessando o penultimo item da lista

print(bicycles[-2])

# acessando a primeira bicicleta da lista e compondo uma mensagem utilizando este valor

message = f'My first bicycle was a {bicycles[0].title()}'
print(message)