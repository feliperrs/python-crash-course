# ---------------------------------------------------------------------------- #
#!               Transferindo elementos de uma lista para outra                #
# ---------------------------------------------------------------------------- #

# Começa com usuários que precisam ser verificados.
unconfirmed_users = ['alice', 'brian', 'candace']

# E uma lista vazia a fim de armazenar os usuarios confirmados.
confirmed_users = []

# Faz a verificação de cada usuário até que não se tenha mais usuarios não confirmados
while unconfirmed_users:
    # Remove um usuário da lista não confirmados e salva em uma variavel
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    # Adiciona a variavel na lista de usuarios confirmados
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())