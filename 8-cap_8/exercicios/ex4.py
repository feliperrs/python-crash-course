# ---------------------------------------------------------------------------- #
#!                            8.4 Camisetas grandes                            #
# ---------------------------------------------------------------------------- #

# Modifique a função make_shirt() para que as camisetas sejam grandes por padrão com a seguinte frase estampada: Eu amo Python. 

# Escreva uma camiseta grande e uma média com a mensagem padrão e uma camiseta de qualquer tamanho com uma frase diferente.

def make_shirt(tamanho='G', frase='Eu amo Python'):
    print(f'Camiseta tamanho {tamanho.upper()} com a estampa: "{frase}"')


make_shirt()
make_shirt('M')

make_shirt('PP', 'Eu odeio Python')