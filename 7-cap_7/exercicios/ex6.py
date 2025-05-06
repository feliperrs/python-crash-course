# ---------------------------------------------------------------------------- #
#!                               7.6 Três saídas                               #
# ---------------------------------------------------------------------------- #

# Crie diferentes versões do Exercício 7.4 ou 7.5 que executem cada uma das seguintes tarefas, pelo menos uma vez:

# Use um teste condicional na instrução while para interromper o loop.

# Use uma variável active para controlar o tempo que o loop é executado.

# Use uma instrução break para sair do loop quando o usuário inserir o valor 'quit'.

age = ""

while age != 'quit':
    age = input("Informe sua idade (ou 'quit' para sair): ")
    if age == 'quit':
        break
    if age.isdigit():
        age = int(age)
        if age < 3:
            print("O ingresso é gratuito.")
        elif age < 13:
            print("O ingresso custa US$10.")
        else:
            print("O ingresso custa US$15.")
    else:
        print("Digite uma idade válida ou 'quit'.")


active = True

while active:
    age = input("Informe sua idade (ou 'quit' para sair): ")
    if age == 'quit':
        active = False
    elif age.isdigit():
        age = int(age)
        if age < 3:
            print("O ingresso é gratuito.")
        elif age < 13:
            print("O ingresso custa US$10.")
        else:
            print("O ingresso custa US$15.")
    else:
        print("Digite uma idade válida ou 'quit'.")

while True:
    age = input("Informe sua idade (ou 'quit' para sair): ")
    if age == 'quit':
        break
    elif age.isdigit():
        age = int(age)
        if age < 3:
            print("O ingresso é gratuito.")
        elif age < 13:
            print("O ingresso custa US$10.")
        else:
            print("O ingresso custa US$15.")
    else:
        print("Digite uma idade válida ou 'quit'.")
