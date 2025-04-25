# ---------------------------------------------------------------------------- #
#!                          2.8 Extensoes de arquivo                           #
# ---------------------------------------------------------------------------- #

#? O Python tem um metodo removesuffix() que funciona exatamente como o removeprefix().
#? Atribua o valor 'python_notes.txt' a uma variavel chamada filename.
#? Depois utilize o metodo removesuffix() para exibir o nome do arquivo sem a extensao do arquivo.

filename = 'python_notes.txt'

filename = filename.removesuffix('.txt')

print(filename)