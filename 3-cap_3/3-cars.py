# ---------------------------------------------------------------------------- #
#!                            Organizando uma lista                            #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
#!               Ordenando uma lista permanentemente com sort()                #
# ---------------------------------------------------------------------------- #

# organiza em ordem alfabetica de forma definitiva

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# ---------------------------------------------------------------------------- #
#!                          Ordem alfabetica reversa                           #
# ---------------------------------------------------------------------------- #

# passando o argumento reverse=True para sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# ---------------------------------------------------------------------------- #
#!             Ordenando uma lista de temporariamente com sorted()             #
# ---------------------------------------------------------------------------- #

# na afeta a ordem original da lista
# tambem aceita o argumento reverse=True

cars = ['bmw', 'audi', 'toyota', 'subaru']

print('\nHere is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# ---------------------------------------------------------------------------- #
#!              Exibindo uma lista em ordem inversa com reverse()              #
# ---------------------------------------------------------------------------- #

# nao ordena de forma alfabetica
# inverte a ordem da lista
# altera de forma permanente
# para voltar a ordem original basta usar reverse() novamente.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)