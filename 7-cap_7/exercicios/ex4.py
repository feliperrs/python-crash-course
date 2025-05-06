# ---------------------------------------------------------------------------- #
#!                          7.4 Ingredientes de pizza                          #
# ---------------------------------------------------------------------------- #

# Escreva um loop que solicite ao usuário uma série de ingredientes de pizza até que ele forneça o valor 'quit'.

# À medida que cada ingrediente é fornecido, exiba uma mensagem informando que esses ingredientes serão adicionados à pizza.

print("Por favor, insira quais ingredientes deseja na sua pizza")
print("Digite 'quit' para sair")

while True:
    topping = input('>> ')
    if topping == 'quit':
        break
    else:
        print(f"O ingrediente {topping} foi adicionado a lista!")
