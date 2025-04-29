# ---------------------------------------------------------------------------- #
#!                             3.6 Mais Convidados                             #
# ---------------------------------------------------------------------------- #

#? Voce acabou de encontrar uma mesa maior de jantar, agora há mais espaço disponivel, convide mais tres pessoas para o jantar
#? Use um insert() para adicionar um convidado novo no inicio da lista
#? Use um insert() para adicionar um convidado novo no meio da lista
#? Use um append() para adicionar um convidado novo no final da lista
#? Exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista

lista_convidados = ['papa francisco', 'galileu galilei', 'albert einstein']


print(f'{lista_convidados[0].title()}, teria a bondade de nos honrar com sua presença em um jantar simples, onde poderíamos compartilhar não apenas o pão, mas também palavras de sabedoria e esperança?')
print(f'Mestre {lista_convidados[1].title()}, que tal um jantar onde os pratos sejam tão fascinantes quanto suas descobertas, e a conversa, tão livre quanto seu pensamento?')
print(f'Caro {lista_convidados[2].title()}, imagine uma noite com boa comida, ótimo vinho e discussões que desafiem o tempo e o espaço - aceita o convite?')

lista_convidados.insert(0, 'cleópatra')
lista_convidados.insert(2, 'william shakespeare')
lista_convidados.append('frida kahlo')

print(f'Majestade {lista_convidados[0].title()}, que honra seria recebê-la para um banquete digno de seu paladar requintado, onde os sabores do Nilo se misturariam a conversas sobre poder, amor e eternidade')
print(f'{lista_convidados[2].title()}, aceitaria um jantar onde o vinho fluiria como suas palavras, e cada brinde seria um novo ato em sua comédia humana?')
print(f'Querida {lista_convidados[5].title()}, que tal uma noite colorida com comida picante, tequila e conversas tão vibrantes e profundas quanto suas telas?')