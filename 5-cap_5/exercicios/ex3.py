# ---------------------------------------------------------------------------- #
#!                         5.3 Cores de alienígenas 3                          #
# ---------------------------------------------------------------------------- #

#? Converta sua sequência if-else do Exercício 5.2 em uma sequência if-elif-else.

#? Se o alienígena for verde, exiba uma afirmação de que o jogador ganhou 5 pontos.

#? Se o alienígena for amarelo, exiba uma afirmação de que o jogador ganhou 10 pontos.

#? Se o alienígena for vermelho, exiba uma afirmação de que o jogador ganhou 15 pontos.

#? Escreva três versões desse programa, assegurando que cada afirmação exibida seja correspondente à cor adequada do alienígena.

alien_color = 'green'

if alien_color == 'green':
    print('Você ganhou 5 pontos!')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos!')
else:
    print('Você ganhou 15 pontos!')

alien_color = 'yellow'

if alien_color == 'green':
    print('Você ganhou 5 pontos!')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos!')
else:
    print('Você ganhou 15 pontos!')

alien_color = 'red'

if alien_color == 'green':
    print('Você ganhou 5 pontos!')
elif alien_color == 'yellow':
    print('Você ganhou 10 pontos!')
else:
    print('Você ganhou 15 pontos!')
