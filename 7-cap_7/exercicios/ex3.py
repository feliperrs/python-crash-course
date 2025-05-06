# ---------------------------------------------------------------------------- #
#!                            7.3 Múltiplos de dez                             #
# ---------------------------------------------------------------------------- #

# Solicite ao usuário um número e informe se o número é múltiplo de 10 ou não.

number = int(input("Insira um número: "))

if number % 10 == 0:
    print("Seu número é divisivel por 10!")
else:
    print("Seu número não é divisivel por 10!")
