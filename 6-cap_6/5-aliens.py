# ---------------------------------------------------------------------------- #
#!                          Uma lista de dicionários                           #
# ---------------------------------------------------------------------------- #

alien_0 = {'color' : 'green', 'points' : 5}
alien_1 = {'color' : 'yellow', 'points' : 10}
alien_2 = {'color' : 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# cria uma lista vazia para armazenar alienigenas
aliens = []

# cria 30 alienigenas verdes
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

# exibe os primeiros 5 alienigenas 
for alien in aliens[:5]:
    print(alien)
print('...\n')

# exibe quantos alienigenas foram criados
print(f'Total number of aliens: {len(aliens)}\n')

# altera a cor, os pontos e a velocidade dos 3 primeiros aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[:5]:
    print(alien)
print('...\n')

# exibe quantos alienigenas foram criados
print(f'Total number of aliens: {len(aliens)}\n')