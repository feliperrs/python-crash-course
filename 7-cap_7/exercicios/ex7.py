# ---------------------------------------------------------------------------- #
#!                               7.7 Lanchonete                                #
# ---------------------------------------------------------------------------- #

# Crie uma lista chamada sandwich_orders e a preencha com o nome de diversos sanduíches.

# Depois, crie uma lista vazia chamada finished_sandwiches.

# Percorra a lista de pedidos de sanduíches com um loop e exiba uma mensagem para cada pedido, como: Seu lanche de atum está pronto.

# Conforme cada sanduíche é preparado, mova-o para a lista de sanduíches prontos.

# Após todos os sanduíches terem sido preparados, exiba uma mensagem enumerando cada um deles.

sandwich_orders = ['big mac', 'cheddar', 'whopper', 'quarteirão']

finished_sandwiches = []

while sandwich_orders:
    # remove um lanche da lista de pedidos e salva em uma variavel
    current_sandwich = sandwich_orders.pop()

    print(f"O lanche {current_sandwich.title()} está sendo preparado!")
    # adiciona a variavel criada na lista de lanches prontos
    finished_sandwiches.append(current_sandwich)

# listando todos os lanches prontos
print(f"\nLanches prontos:")
num=0
for lanche in finished_sandwiches:
    num += 1
    print(f"\t{num} - {lanche}")