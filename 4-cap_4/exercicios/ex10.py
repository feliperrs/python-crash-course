# ---------------------------------------------------------------------------- #
#!                                 4.10 Fatias                                 #
# ---------------------------------------------------------------------------- #

#? Use um dos programas que escreveu neste capítulo, adicione diversas linhas ao final do programa para executarem o seguinte:
#? Exiba a mensagem: Os três primeiros elementos da lista são: Em seguida, use uma fatia para exibir os três primeiros elementos da lista desse programa.
#? Exiba a mensagem: Os três elementos que ficam no meio da lista são: Depois, use uma fatia para exibir os três elementos do meio da lista.
#? Exiba a mensagem: Os três últimos elementos da lista são: Em seguida, utilize uma fatia para exibir os três últimos elementos da lista.

pizza_tastes = ['bacon', 'calabresa', 'napolitana', 'marguerita', '4 queijos',]

print('Os tres primeiros elementos da lista são:')
print(pizza_tastes[:3])
print('Os tres elementos que ficam no meio da lista são:')
print(pizza_tastes[1:4])
print('Os tres ultimos elementos da lista são:')
print(pizza_tastes[-3:])