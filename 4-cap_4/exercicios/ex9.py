# ---------------------------------------------------------------------------- #
#!                           4.9 Cube Comprehension                            #
# ---------------------------------------------------------------------------- #

#? Use uma list comprehension para gerar uma lista dos primeiros 10 cubos.

cubes = [value ** 3 for value in range(1, 11)]
print(cubes)