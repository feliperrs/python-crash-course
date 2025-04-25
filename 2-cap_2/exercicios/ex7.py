# ---------------------------------------------------------------------------- #
#!                             2.7 Removendo nomes                             #
# ---------------------------------------------------------------------------- #

#? Use uma váriavel para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no inicio e no final do nome.
#? Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez
#? Exiba o nome uma vez para que o espaço em branco ao redor do nome seja mostrado.
#? Em seguida, printe o nome usando cada uma das tres funçoes de remocao, lstrip(), rstrip() e strip()

name = '\tFelipe Santos\n\n\n\n\n'


print(name.lstrip())    # tirou o "\t"
print(name.rstrip())    # tirou os "\n"
print(name.strip())     # tirou tudo