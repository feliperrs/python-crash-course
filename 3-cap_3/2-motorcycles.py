# ---------------------------------------------------------------------------- #
#!                            Modificando elementos                            #
# ---------------------------------------------------------------------------- #

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)


motorcycles[0] = 'ducati'
print(motorcycles)

# ---------------------------------------------------------------------------- #
#!                 Adicionando elementos ao final de uma lista                 #
# ---------------------------------------------------------------------------- #

motorcycles.append('honda')
print(motorcycles)

motorcycles_2 = []
motorcycles_2.append('honda')
motorcycles_2.append('yamaha')
motorcycles_2.append('suzuki')

print(motorcycles_2)

# ---------------------------------------------------------------------------- #
#!                   Inserindo elementos em uma dada posicao                   #
# ---------------------------------------------------------------------------- #

# adiciona 'ducati' na posicao 0
motorcycles_2.insert(0, 'ducati')
print(motorcycles_2)

# ---------------------------------------------------------------------------- #
#!                       Removendo um elemento com 'del'                       #
# ---------------------------------------------------------------------------- #

# remove um elemento que tem posicao conhecida
del motorcycles_2[0]
print(motorcycles_2)
# após remover com 'del' o elemento nao é mais acessado de nenhuma forma


# ---------------------------------------------------------------------------- #
#!                       Removendo um elemento com 'pop'                       #
# ---------------------------------------------------------------------------- #

# remove o ultimo elemento da lista
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# após remover com pop() ainda é possivel ter acesso ao elemento
print(f'The last motorcycle I owned was a {popped_motorcycle.title()}')

# ---------------------------------------------------------------------------- #
#!              Removendo um elemento de qualquer posicao com pop              #
# ---------------------------------------------------------------------------- #

# é possivel remover um elemento de qualquer posicao com pop para manter o acesso a este elemento
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}')

# ---------------------------------------------------------------------------- #
#!                       Removendo um elemento por valor                       #
# ---------------------------------------------------------------------------- #

# usado quando nao sabemos a posicao do elemento mas sabemos o seu valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

# ---------------------------------------------------------------------------- #
#!               Trabalhando com um valor removido com 'remove'                #
# ---------------------------------------------------------------------------- #

# assim como com o 'pop()', o valor removido ainda é possivel de ser acessado

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(f'\nA {too_expensive.title()} is too expensive for me')

# o metodo remove() deleta somente a primeira ocorrencia do valor especificado, sendo necessario um loop para remover mais de 1 ocorrencia