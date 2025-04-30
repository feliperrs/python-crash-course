# ---------------------------------------------------------------------------- #
#!                                 4.13 Buffet                                 #
# ---------------------------------------------------------------------------- #

#? Um restaurante com serviço de buffet oferece somente cinco refeições básicas. Pense em cinco refeições simples e armazene-as em uma tupla.
#? Use um loop for para exibir cada refeição que o restaurante oferece.
#? Tente modificar um dos elementos e verifique se o Python rejeita a mudança.
#? O restaurante muda seu cardápio, substituindo dois dos elementos por refeições diferentes. Adicione uma linha que rescreva a tupla e, depois, use um loop for para exibir cada um dos elementos no menu reformulado.

cardapio = (
    "filé mignon ao molho madeira",
    "frango grelhado com ervas finas",
    "lasanha à bolonhesa",
    "strogonoff de carne",
    "espaguete ao pesto",
)

for prato in cardapio:
    print(prato.title())

# cardapio.append("Moqueca de Peixe")

cardapio = (
    "filé mignon ao molho madeira",
    "frango grelhado com ervas finas",
    "lasanha à bolonhesa",
    "peixe assado com limão e lcaparras",
    "bobó de camarão"
)

for prato in cardapio:
    print(prato.title())