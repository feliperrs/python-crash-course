
# ---------------------------------------------------------------------------- #
#!                               5.5 Olá, admin                                #
# ---------------------------------------------------------------------------- #

#? Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. Imagine que está escrevendo um código que exibirá uma mensagem de boas-vindas aos usuários, após cada um deles logar em um site. Percorra a lista de nomes em um loop e exiba uma mensagem de boas-vindas para cada usuário.

#? Se o nome de usuário for 'admin', exiba uma mensagem especial, tipo: Olá administrador, gostaria de ver um relatório de status?

#? Caso contrário, exiba uma mensagem genérica, como: Olá Jaden, obrigado por fazer login novamente.


users = ['rydenfelt', 'singertown', 'grewyule','admin', 'illdrain']

for user in users:
    if user != 'admin':
        print(f'Hello {user}, obrigado por fazer login novamente')
    elif user == 'admin':
        print('Olá administrador, gostaria de ver um relatório de status?')