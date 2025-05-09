# ---------------------------------------------------------------------------- #
#!                 Passando um número arbitrário de argumentos                 #
# ---------------------------------------------------------------------------- #

def make_pizza(*toppings):
    """sintetiza a pizza que estamos prestes a fazer"""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra chesse')

# ---------------------------------------------------------------------------- #
#!               Misturando argumentos posicionais e arbitrarios               #
# ---------------------------------------------------------------------------- #

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16,'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra chesse')