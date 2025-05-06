# ---------------------------------------------------------------------------- #
#!                                8.3 Camiseta                                 #
# ---------------------------------------------------------------------------- #

# Crie uma função chamada make_shirt() que aceita um tamanho e o texto que deve ser estampado na camiseta.

# A função deve exibir uma frase resumindo o tamanho da camiseta e a mensagem estampada nela.

# Chame a função uma vez usando argumentos posicionais para criar uma camiseta.

# Chame a função uma segunda vez usando argumentos nomeados.

def make_shirt(tamanho, frase):
    print(f'Você confirma que deseja uma camisa tamanho "{tamanho.upper()}" e com a frase "{frase}"?')

make_shirt('G', 'Que Deus perdoe essas pessoas ruins')
make_shirt(frase='PARE DE FICAR LENDO FRASES NA CAMISETA DOS OUTROS',
            tamanho='PP')