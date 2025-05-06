# ---------------------------------------------------------------------------- #
#!                          Escrevendo prompts limpos                          #
# ---------------------------------------------------------------------------- #

name = input("Please enter yout name: ")
print(f"Hello, {name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhats is yout first name? "

name = input(prompt)
print(f"Hello, {name}!")