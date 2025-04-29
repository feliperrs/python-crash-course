# ---------------------------------------------------------------------------- #
#!                                 4.1 Pizzas                                  #
# ---------------------------------------------------------------------------- #

#? Pense em pelo menos, tres tipos de pizza que voec gosta.
#? Armazene esses nomes de pizza em uma lista e use um loop for para exibir o nome de cada uma.
#? Modifique seu loop for a fim de que exiba uma frase usando o nome da pizza, em vez de exibir apenas o nome da pizza
#? Para cada pizza, voce deve gerar uma linha de saida com uma simples afirmacao.
#? Adicione uma linha no final do seu programa, fora do loop for, que ressalte o quanto voce gosta de pizza
#? A saida deve ter tres ou mais linhas sbre os tipos de pizza que voce gosta e, em seguida uma frase adicional

pizza_tastes = ['bacon', 'calabresa', 'napolitana']

for pizza in pizza_tastes:
    print(f'{pizza.title()}')

for pizza in pizza_tastes:
    print(f'Gosto de pizza de {pizza.title()}')

for pizza in pizza_tastes:
    print(f'Gosto de pizza de {pizza.title()}')
print('\nEu amo pizza!!!!')