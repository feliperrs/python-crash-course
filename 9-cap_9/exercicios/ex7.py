# ---------------------------------------------------------------------------- #
#!                                  9.7 Admin                                  #
# ---------------------------------------------------------------------------- #

# Um administrador é um tipo especial de usuário. 

# Crie uma classe chamada Admin que herde da classe User, mostrada no Exercício 9.3 (página 211) ou Exercício 9.5 (página 216). 

# Adicione um atributo, privileges, que armazene uma lista de strings como "can add post", "can delete post", "can ban user", e assim por diante. 

# Escreva um método chamado show_privileges() que enumere o conjunto de privilégios do administrador. 

# Crie uma instância de Admin e chame seu método.

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

class Admin(User):
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('Um Admin pode:')
        for privilege in self.privileges:
            print(f"\t- {privilege}")

admin = Admin('João', 'Silva', 'joao.silva', 28)
admin.describe_user()
admin.show_privileges()