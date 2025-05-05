# ---------------------------------------------------------------------------- #
#!                         Uma lista em um dicionario                          #
# ---------------------------------------------------------------------------- #

# armazena informações sobre uma pizza que esta sendo pedida
pizza = {
    'crust' : 'thick',
    'toppigns' : ['mushrooms', 'extra cheese']
}

# resume o pedido
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppigns']:
    print(f'\t{topping}')
