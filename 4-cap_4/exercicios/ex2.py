# ---------------------------------------------------------------------------- #
#                                  4.2 Animais                                 #
# ---------------------------------------------------------------------------- #

#? Pense em pelo menos, tres tipos de animais diferentes que compartilhem uma caracteristica em comum.
#? Armazene o nome desses animais em uma lista e em seguida, use um loop for para exibir o nome de cada animal.
#? Modifique seu programa a fim de exibir uma afirmacao sobre cada animal.
#? Adicione uma linha no final do seu programa indicando que esses animais compartilham ago em comum.

pets = ['cachorro', 'gato', 'hamster']

for pet in pets:
    print(f'{pet.title()}')
    print(f'Um {pet.title()} é um ótimo animal de estimacao')
print('Todos esses animais sao otimos para serems animais de estimacao com crianças em casa')