# ---------------------------------------------------------------------------- #
#!                     Acessando valores em um dicionario                      #
# ---------------------------------------------------------------------------- #

alien_0 = {'color' : 'green' , 'points' : 5}

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

# ---------------------------------------------------------------------------- #
#!                     Adicionando novos pares chave-valor                     #
# ---------------------------------------------------------------------------- #

alien_0 = {'color' : 'green' , 'points' : 5}

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# ---------------------------------------------------------------------------- #
#!                      Começando com um dicionário vazio                      #
# ---------------------------------------------------------------------------- #

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# ---------------------------------------------------------------------------- #
#!                    Modificando valores em um dicionário                     #
# ---------------------------------------------------------------------------- #

alien_0 = {'color' : 'green'}
print(f'The alien is {alien_0['color']}.')

alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0['color']}.')

alien_0 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}

print(f'Original x-position: {alien_0["x_position"]}')

# Descola o alienigena para direita
# Estipula a distancia que o alienigena dever percorrer conforme sua velocidade

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Com isso, o alienigena fica veloz
    x_increment = 3

# A posição nova é a posição antiga mais o incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'New x-position: {alien_0["x_position"]}')

# ---------------------------------------------------------------------------- #
#!                        Removendo pares chaves-valor                         #
# ---------------------------------------------------------------------------- #

alien_0 = {'color' : 'green' , 'points' : 5}
print(alien_0)

del alien_0['points']
print(alien_0)