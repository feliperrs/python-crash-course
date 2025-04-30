# ---------------------------------------------------------------------------- #
#!                       4.11 Minhas pizzas, suas pizzas                       #
# ---------------------------------------------------------------------------- #

#? Comece com o programa do Exercício 4.1 (página 92). Faça uma cópia da lista de pizzas e a nomeie como friend_pizzas. Em seguida, siga os etapas:
#? Adicione uma pizza nova à lista original.
#? Adicione uma pizza diferente à lista friend_pizzas.
#? Prove que tem duas listas separadas. 
#? Exiba a mensagem: Minhas pizzas favoritas são:. E, em seguida, use um loop for para exibir a primeira lista. 
#? Exiba a mensagem: Minhas pizzas favoritas são:. E, em seguida, use um loop for para exibir a segunda lista. 
#? Garanta que cada pizza nova seja armazenada na lista adequada.

pizza_tastes = ['bacon', 'calabresa', 'napolitana']

friend_pizzas = pizza_tastes[:]

pizza_tastes.append('marguerita')
friend_pizzas.append('4 queijos')

print('Minhas pizzas favoritas são:')
for pizza in pizza_tastes:
    print(pizza.title())

print('\nAs pizzas favoritas do meu amigo são:')
for pizza in friend_pizzas:
    print(pizza.title())