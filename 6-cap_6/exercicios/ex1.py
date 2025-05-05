# ---------------------------------------------------------------------------- #
#!                                 6.1 Pessoa                                  #
# ---------------------------------------------------------------------------- #

#? Use um dicionário para armazenar informações sobre uma pessoa que você conhece. 
#? Armazene o nome, sobrenome, idade e a cidade onde mora. Nomeie as chaves como first_name, last_name, age e city. Exiba cada informação armazenada em seu dicionário.

person = {
    'first_name' : 'joão',
    'last_name' : 'pereira',
    'age' : 23,
    'city' : 'curitiba'
    }

print(f'Nome: {person["first_name"].title()}')
print(f'Sobrenome: {person["last_name"].title()}')
print(f'Idade: {person["age"]}')
print(f'Cidade: {person["city"].title()}')
