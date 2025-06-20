# ---------------------------------------------------------------------------- #
#!                           Usando a funçao range()                           #
# ---------------------------------------------------------------------------- #

for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

for value in range(6):
    print(value)

# ---------------------------------------------------------------------------- #
#!               Usando o range() para criar uma lista de numeros              #
# ---------------------------------------------------------------------------- #

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range (2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

# ---------------------------------------------------------------------------- #
#!                Estatisticas simples com uma lista de numeros                #
# ---------------------------------------------------------------------------- #

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# ---------------------------------------------------------------------------- #
#!                             List comprehensions                             #
# ---------------------------------------------------------------------------- #

squares = [value ** 2 for value in range(1,11)]
print(squares)