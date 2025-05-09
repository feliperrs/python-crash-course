# ---------------------------------------------------------------------------- #
#!                               8.12 Sanduíches                               #
# ---------------------------------------------------------------------------- #

# Crie uma função que aceite uma lista de itens que uma pessoa quer em um sanduíche. 

# A função deve ter um parâmetro que colete todos os itens fornecidos na chamada de função e deve exibir um resumo do sanduíche que está sendo solicitado. 

# Chame a função três vezes, com um número diferente de argumentos a cada vez.


def fazer_sanduiche(*ingredientes):
    print("\nFazendo um sanduiche com os seguintes ingredientes:")
    for ingrediente in ingredientes:
        print(f"\t- {ingrediente}")


fazer_sanduiche('picles', 'cebola', 'tomate')
fazer_sanduiche('tomate', 'alface')
fazer_sanduiche('agrião')
