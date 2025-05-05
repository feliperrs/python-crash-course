# ---------------------------------------------------------------------------- #
#!                                6.3 Glossário                                #
# ---------------------------------------------------------------------------- #

#? Um dicionário Python pode ser usado para modelar um dicionário real.Contudo, para evitar confusão, vamos chamá-lo de glossário.

#? Pense em cinco palavras do mundo de programação que você aprendeu nos capítulos anteriores. 
#? Use essas palavras como chaves em seu glossário e armazene seus significados como valores.

#? Exiba cada palavra e seu significado como uma saída elegantemente formatada.
#?  É possível até mesmo exibir a palavra seguida por dois-pontos e depois seu significado ou a palavra em uma linha e, em seguida, exibir seu significado indentado em uma segunda linha. 
#? Use o caractere quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.

glossario = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

word = 'string'
print(f"\n{word.title()}: {glossario[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossario[word]}")

word = 'list'
print(f"\n{word.title()}: {glossario[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossario[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossario[word]}")