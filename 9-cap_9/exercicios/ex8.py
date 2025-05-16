# ---------------------------------------------------------------------------- #
#!                               9.8 Privilégios                               #
# ---------------------------------------------------------------------------- #

# Crie uma classe Privileges separada. 

# A classe deve ter um atributo, privileges, que armazene uma lista de strings, conforme descrito no Exercício 9.7. 

# Passe o método show_privileges() para essa classe. 

# Crie uma instância de Privileges como um atributo na classe Admin. 

# Crie uma instância nova de Admin e use seu método para mostrar seus privilégios.

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

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Um Admin pode:')
        for privilege in self.privileges:
            print(f"\t- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges()

admin = Admin('João', 'Silva', 'joao.silva', 28)
admin.describe_user()
admin.privileges.show_privileges()