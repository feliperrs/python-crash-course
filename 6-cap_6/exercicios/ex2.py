# ---------------------------------------------------------------------------- #
#!                            6.2 Números favoritos                            #
# ---------------------------------------------------------------------------- #

#? Use um dicionário para armazenar os números favoritos das pessoas. 
#? Pense em cinco nomes e os utilize como chaves em seu dicionário. 
#? Pense em um número favorito para cada pessoa e armazene cada um como um valor em seu dicionário. 
#? Exiba o nome de cada pessoa e seu número favorito. 

favorite_number = {
    'joao': 23,
    'bento' : 16,
    'marina' : 99,
    'paulo' : 12,
    'adriana' : 8
}

print(f'O numero favorito do Joao é: {favorite_number["joao"]}')
print(f'O numero favorito do Bento é: {favorite_number['bento']}')
print(f'O numero favorito da Marina é: {favorite_number["marina"]}')
print(f'O numero favorito do Paulo é: {favorite_number["paulo"]}')
print(f'O numero favorito da Adriana é: {favorite_number["adriana"]}')

