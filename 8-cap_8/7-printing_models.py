# ---------------------------------------------------------------------------- #
#!                     Modificando uma lista em uma função                     #
# ---------------------------------------------------------------------------- #

# # começa com alguns designs que precism ser impressos
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # simula a impressao de cada design, até que não reste nennhum
# # passa cada design para completed_models aopós a impressão

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # exibe todos os modelos concluidos
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    simula a impressão de cada design, até que não reste nenhum
    passa cada design para completed_models após a impressao
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """ exibe todos os modelos impressos"""
    print(f"\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)