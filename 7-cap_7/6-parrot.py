# ---------------------------------------------------------------------------- #
#!                Permitindo que o usuário encerre um programa                 #
# ---------------------------------------------------------------------------- #

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

message = ''

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# ---------------------------------------------------------------------------- #
#!                                Usando flags                                 #
# ---------------------------------------------------------------------------- #

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter 'quit' to end the program: "

# definindo a flag
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False

    else:
        print(message)
