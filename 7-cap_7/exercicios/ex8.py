# ---------------------------------------------------------------------------- #
#!                              7.8 Sem pastrami                               #
# ---------------------------------------------------------------------------- #

# Usando a lista sandwich_orders do Exercício 7.7, assegure-se de que o sanduíche pastrami apareça na lista pelo menos três vezes.

# Faça um if no código perto do início de seu programa, exibindo uma mensagem que informe que a lanchonete está sem pastrami e, em seguida, use um loop while para remover todas as ocorrências de 'pastrami' em sandwich_orders.

# Faça questão de que nenhum sanduíche de pastrami acabe em finished_sandwiches.

sandwich_orders = ['big mac', 'pastrami', 'cheddar','pastrami', 'whopper', 'quarteirão','pastrami']
finished_sandwiches = []

# verifica se há pastrami na lista
if 'pastrami' in sandwich_orders:
    print("\nNo momento a lanchonete está sem Pastrami")
    
    # caso exista, remove todas as ocorrencias
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')


while sandwich_orders:
    # remove da lista de pedidos e adiciona na lista de prontos
    finished_sandwiches.append(sandwich_orders.pop())

# mostra os lanches prontos
print("\nSanduíches prontos:")
for i, sandwich in enumerate(finished_sandwiches, 1):
    print(f"\t{i} - {sandwich.title()}")

