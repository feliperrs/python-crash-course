# ---------------------------------------------------------------------------- #
#!                           3.8 Conhecendo o mundo                            #
# ---------------------------------------------------------------------------- #

#? Pense em pelo menos cinco lugares do mundo que voce gostaria de conhecer
#? Armazene esses locais em uma lista e verifique se ela nao esta em ordem afabetica
#? Exiba sua lista na ordem original, nao se preocupe em exibir a lista ordenadamente, basta exibi-la como uma lista crua do Python
#? Use sorted() para exibir sua lista em ordem alfabetica, sem alterar a lista original
#? Mostre que sua lista ainda esta na ordem original, exibindo-a
#? Use o sorted() para exibir sua lista em ordem alfabetica reversa, sem alterar a ordem original dela
#? Use o reverse() para alterar a ordem de sua lista. Exiba-a a fim de mostrar que ela foi alterada.
#? Use o reverse() para alterar a ordem de sua lista novamente. Exiba-a a fim de mostrar que voltou á ordem original
#? Use o sort() para alterar a sua lista para que ela seja armazenada em ordem alfabetica. Exiba a lista para mostrar que a ordem foi alterada
#? Use o sort() para alterar a sua lista para que ela seja armazenada em ordem alfabetica inversa. Exiba a lista para mostrar que a ordem foi alterada


places = ['piramides do egito', 'everest', 'muralha da china', 'machu picchu', 'taj mahal']

print(places)

print(sorted(places))

print(places)

print(sorted(places, reverse=True))

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)