# ---------------------------------------------------------------------------- #
#!                               6.4 Glossário 2                               #
# ---------------------------------------------------------------------------- #


# Agora você sabe como percorrer um dicionário com um loop, limpe o código do Exercício 6.3 (página 140) substituindo sua série de print() por um loop que percorre as chaves e os valores do dicionário. 
# Quando tiver certeza de que seu loop funciona, adicione mais cinco termos Python ao seu glossário. 
# Quando executar seu programa novamente, essas palavras e significados novos devem ser incluídos automaticamente na saída.


glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word,definition in glossary.items():
    print(f'{word.title()}: {definition}\n')