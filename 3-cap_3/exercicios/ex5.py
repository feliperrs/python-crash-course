# ---------------------------------------------------------------------------- #
#!                      3.5 Mudando a lista de convidados                      #
# ---------------------------------------------------------------------------- #

#? Você acabou de ficar sabendo que um dos convidados nao conseguira ir ao jantar, assim precisa enviar um conjunto novo de conviter, é necessario convidar outra pessoa.
#? Comece com o programa do exercicio 3.4, no final do proigrama adicione um print(), informando o nome do convidado que nao irá mais vir
#? Modifique sua lista substituindo o nome do convidado que nao pode comparecer pelo nome da pessoa nova que voce esta convidando.
#? Exiba um segundo conjunto de mensagens de convite, uma para cada pessoa que nao consta em sua lista

lista_convidados = ['papa francisco', 'galileu galilei', 'albert einstein']


print(f'{lista_convidados[0].title()}, teria a bondade de nos honrar com sua presença em um jantar simples, onde poderíamos compartilhar não apenas o pão, mas também palavras de sabedoria e esperança?')
print(f'Mestre {lista_convidados[1].title()}, que tal um jantar onde os pratos sejam tão fascinantes quanto suas descobertas, e a conversa, tão livre quanto seu pensamento?')
print(f'Caro {lista_convidados[2].title()}, imagine uma noite com boa comida, ótimo vinho e discussões que desafiem o tempo e o espaço - aceita o convite?')

# Galileu Galilei nao ira comparecer

convidado_antigo = 'galileu galilei'
lista_convidados.remove(convidado_antigo)
print(f'\nInfelizmente, {convidado_antigo.title()} não irá comparecer!')

lista_convidados.insert(1,'Mahatma Gandhi')
print(f'\n{lista_convidados[1]} irá vir em seu lugar!')