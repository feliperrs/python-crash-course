# ---------------------------------------------------------------------------- #
#!                                    Tupla                                    #
# ---------------------------------------------------------------------------- #

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

dimensions = (200,)
print(dimensions[0])


# ---------------------------------------------------------------------------- #
#!             Percorrendo todos os valores de uma tupla com loop              #
# ---------------------------------------------------------------------------- #

dimensions = (200,50)
for dimension in dimensions:
    print(dimension)

# ---------------------------------------------------------------------------- #
#!                           Sobscrevendo uma tupla                            #
# ---------------------------------------------------------------------------- #

dimensions = (200,50)

print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)