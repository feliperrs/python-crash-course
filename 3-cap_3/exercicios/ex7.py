# ---------------------------------------------------------------------------- #
#!                     3.7 Reduzindo a lista de convidados                     #
# ---------------------------------------------------------------------------- #

#? Voce acabaou de descobrir que sua mesa de jantar nova nao chegara a tempo e agora tem espaço para somente 2 pessoas
#? Use o pop() para removeer convidados de sua lista, um de cada vez, até que restem somente dois nomes nela.
#? Sempre que remoer um nome de sua lista, exiba uma mensagem para essa pessoa informando que lamenta por nao poder convida-la para o jantar
#? Exiba uma mensagem para cada uma das 2 pessoas que ainda estao na lista, informando que ainda estao convidados
#? Use o del para remover os 2 ultimos nomes de sua lista, para que ela fique vazia
#? Exiba sua lista para ter certeza que voce realmente te uma lista vazia no final do seu programa

lista_convidados = ['papa francisco', 'galileu galilei', 'albert einstein']


print(f'{lista_convidados[0].title()}, teria a bondade de nos honrar com sua presença em um jantar simples, onde poderíamos compartilhar não apenas o pão, mas também palavras de sabedoria e esperança?')
print(f'Mestre {lista_convidados[1].title()}, que tal um jantar onde os pratos sejam tão fascinantes quanto suas descobertas, e a conversa, tão livre quanto seu pensamento?')
print(f'Caro {lista_convidados[2].title()}, imagine uma noite com boa comida, ótimo vinho e discussões que desafiem o tempo e o espaço - aceita o convite?')

lista_convidados.insert(0, 'cleópatra')
lista_convidados.insert(2, 'william shakespeare')
lista_convidados.append('frida kahlo')

print(f'Majestade {lista_convidados[0].title()}, que honra seria recebê-la para um banquete digno de seu paladar requintado, onde os sabores do Nilo se misturariam a conversas sobre poder, amor e eternidade')
print(f'{lista_convidados[2].title()}, aceitaria um jantar onde o vinho fluiria como suas palavras, e cada brinde seria um novo ato em sua comédia humana?')
print(f'Querida {lista_convidados[5].title()}, que tal uma noite colorida com comida picante, tequila e conversas tão vibrantes e profundas quanto suas telas?\n')

desconvidado = lista_convidados.pop()
print(f'Desculpe, {desconvidado.title()}, o jantar nao ira mais ocorrer')
desconvidado = lista_convidados.pop()
print(f'Desculpe, {desconvidado.title()}, o jantar nao ira mais ocorrer')
desconvidado = lista_convidados.pop()
print(f'Desculpe, {desconvidado.title()}, o jantar nao ira mais ocorrer')
desconvidado = lista_convidados.pop()
print(f'Desculpe, {desconvidado.title()}, o jantar nao ira mais ocorrer\n')

print(f'Olá {lista_convidados[0].title()}, o jantar ainda esta de pé')
print(f'Olá {lista_convidados[1].title()}, o jantar ainda esta de pé\n')

del lista_convidados[0] 
del lista_convidados[0]

print(lista_convidados)