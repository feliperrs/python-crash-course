# ---------------------------------------------------------------------------- #
#!                               4.12 Mais loops                               #
# ---------------------------------------------------------------------------- #

#? Nesta seção, todas as versões de food.py evitaram o uso de loops for para exibição, a fim de economizar espaço. 
#? Escolha uma versão de food.py e escreva dois loops for para exibir cada lista de alimentos.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
for food in my_foods:
    print(food.title())

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food.title())