# ---------------------------------------------------------------------------- #
#!                                9.3 Usuários                                 #
# ---------------------------------------------------------------------------- #

# Crie uma classe chamada User. 

# Crie dois atributos chamados first_name e last_name e diversos outros atributos que normalmente são armazenados em um perfil de usuário.

# Crie um método chamado describe_user() que exiba um resumo das informações do usuário.

# Crie outro método chamado greet_user() que exiba um cumprimento personalizado ao usuário.

# Crie diversas instâncias que representem usuários distintos e chame ambos os métodos para cada um.

class User:
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age

    def describe_user(self):
        print(f"User Information:")
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tUsername: {self.username}")
        print(f"\tAge: {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome!\n")


user1 = User('João', 'Silva', 'joao.silva', 28)
user2 = User('Maria', 'Santos', 'maria.santos', 34)
user3 = User('Carlos', 'Oliveira', 'carlos.oliveira', 22)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()