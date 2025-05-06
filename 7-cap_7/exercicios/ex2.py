# ---------------------------------------------------------------------------- #
#!                        7.2 Reservas em restaurante:                         #
# ---------------------------------------------------------------------------- #

# Crie um programa que pergunte quantos lugares uma mesa o usuário precisa.

# Se a resposta for mais de oito, exiba uma mensagem informando que é necessário aguardar por uma mesa.
    
# Caso contrário, informe que a mesa já está disponível.

lugares = int(input("Quantos lugares você deseja? "))

if lugares > 8:
    print("No momento não há mesas disponiveis, aguarde!")
else:
    print("Sua mesa já está disponivel!")