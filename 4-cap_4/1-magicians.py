# ---------------------------------------------------------------------------- #
#!                    LOOPS: percorrendo uma lista inteira                     #
# ---------------------------------------------------------------------------- #

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician)

# ---------------------------------------------------------------------------- #
#!                 Fazendo mais tarefas dentro de um loop for                  #
# ---------------------------------------------------------------------------- #

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see yout next trick, {magician.title()}\n")

# ---------------------------------------------------------------------------- #
#!                 Fazendo mais tarefas após usar um loop for                  #
# ---------------------------------------------------------------------------- #

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can't wait to see yout next trick, {magician.title()}\n")

print('Thak you everyone. That was a great magic show!')