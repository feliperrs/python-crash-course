# ---------------------------------------------------------------------------- #
#!                                  f-strings                                  #
# ---------------------------------------------------------------------------- #

first_name = 'ada'
last_name= 'lovelace'

full_name = f"{first_name} {last_name}"

print(full_name)

message = f'Hello, {full_name.title()}!'

print(message)

# ---------------------------------------------------------------------------- #
#!                              Espaços em branco                              #
# ---------------------------------------------------------------------------- #

print('Python')
print('\tPython')   # '\t' adiciona uma tabulacao

print('Languages:\nPython\nC\nJavaScript') # '\n' adiciona uma quebra de linha

print('Languages: \n\tPython\n\tC\n\tJavaScript')   # é possivel combinar o '\n' com o '\t'

# ---------------------------------------------------------------------------- #
#!                    Removendo espaços em branco - strip()                    #
# ---------------------------------------------------------------------------- #

teste = " 'Hello World !' "
print(teste.rstrip())   # remove os espaços em branco no final
print(teste.lstrip())   # remove os espaços em branco no começo
print(teste.strip())    # remove os espaços em branco no começo e no final

# ---------------------------------------------------------------------------- #
#!                             Removendo prefixos                              #
# ---------------------------------------------------------------------------- #

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')    # remove o prefixo 'https://'
print(simple_url)