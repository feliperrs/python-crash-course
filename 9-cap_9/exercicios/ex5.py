# ---------------------------------------------------------------------------- #
#!                           9.5 Tentativas de login                           #
# ---------------------------------------------------------------------------- #

# Adicione um atributo chamado login_attempts à sua classe User do Exercício 3.3 (página 211). 

# Crie um método chamado increment_login_attempts() que incrementa o valor de login_attempts em 1. 
 
# Crie outro método chamado reset_login_attempts() que redefine o valor de login_attempts para 0.

# Crie uma instância da classe User e chame increment_login_attempts() diversas vezes. 

# Exiba o valor de login_attempts para verificar que foi incrementado corretamente e, em seguida, chame reset_login_attempts(). 

# Exiba login_attempts novamente a fim de ter certeza de que foi redefinido para 0.

class User:
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Information:")
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tUsername: {self.username}")
        print(f"\tAge: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    
user1 = User('João', 'Silva', 'joao.silva', 28)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)