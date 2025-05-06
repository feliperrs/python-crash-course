# ---------------------------------------------------------------------------- #
#!                           7.5 Ingressos de cinema                           #
# ---------------------------------------------------------------------------- #

# Um cinema cobra preços de ingressos diferentes, dependendo da idade da pessoa.

# Se a pessoa tiver menos de 3 anos, o ingresso é gratuito; se tiver entre 3 e 12 anos, o ingresso custa US$10; se for maior de 12 anos, o ingresso custa US$15.

# Escreva um loop que pergunte a idade dos usuários, e, em seguida, informe o preço do ingresso do cinema.

print("Informe sua idade")
print("Digite 'quit' para sair")

while True:
    age = input('>> ')
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("O ingresso é gratuito")
    elif age < 13:
        print("O ingresso custa US$10")
    else:
        print("O ingresso custa US$15")


