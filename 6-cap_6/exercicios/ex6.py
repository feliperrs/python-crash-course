# ---------------------------------------------------------------------------- #
#!                                6.6 Pesquisa                                 #
# ---------------------------------------------------------------------------- #

# Use o código de favorite_languages.py (página 137).

# Crie uma lista de pessoas que deveriam participar da pesquisa de linguagens favoritas. 
# Inclua alguns nomes que já estão no dicionário e outros que não estão.

# Percorra com um loop a lista de pessoas que devem participar da pesquisa. Se já tiverem respondido, exiba uma mensagem agradecendo a resposta.

# Se ainda não tiverem respondido, exiba uma mensagem as convidando a participar.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']


for coder in coders:
    if coder in favorite_languages:
        print(f'{coder.title()}, obrigado por participar da pesquisa!')
    else:
        print(f'{coder.title()}, por favor, responda a pesquisa!')
