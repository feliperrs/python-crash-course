# ---------------------------------------------------------------------------- #
#!                            Definindo uma função                             #
# ---------------------------------------------------------------------------- #

def greeter_user():
    """exibe um simples cumprimento"""
    print("Hello!")

greeter_user()

# ---------------------------------------------------------------------------- #
#!                    Passando informações para uma função                     #
# ---------------------------------------------------------------------------- #

def greeter_user(username):
    """exibe um simples cumprimento"""
    print(f"Hello, {username.title()}!")

greeter_user('jesse')
greeter_user('sarah')