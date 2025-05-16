# ---------------------------------------------------------------------------- #
#!                            Criando a classe Dog                             #
# ---------------------------------------------------------------------------- #

# class Dog:
#     """Simples tentativa de modelar um cachorro"""

#     def __init__(self, name, age):
#         """Inicializa os atributos de nome e idade"""
#         self.name = name
#         self.age = age


#     def sit(self):
#         """Simula um cachorro sentado em respota a um comando"""
#         print(f"{self.name} is now sitting!")

#     def roll_over(self):
#         """Simula um cachorro rolando em resposta a um comando"""
#         print(f"{self.name} rolled over!")


# ---------------------------------------------------------------------------- #
#!               Como criar uma instância a partir de uma classe               #
# ---------------------------------------------------------------------------- #

# class Dog:
#     """Simples tentativa de modelar um cachorro"""

#     def __init__(self, name, age):
#         """Inicializa os atributos de nome e idade"""
#         self.name = name
#         self.age = age


#     def sit(self):
#         """Simula um cachorro sentado em respota a um comando"""
#         print(f"{self.name} is now sitting!")

#     def roll_over(self):
#         """Simula um cachorro rolando em resposta a um comando"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)

# print(f"My dog's name is {my_dog.name}")
# print(f"My dog's is {my_dog.age} years old")

# ---------------------------------------------------------------------------- #
#!                              Chamando métodos                               #
# ---------------------------------------------------------------------------- #

# class Dog:
#     """Simples tentativa de modelar um cachorro"""

#     def __init__(self, name, age):
#         """Inicializa os atributos de nome e idade"""
#         self.name = name
#         self.age = age


#     def sit(self):
#         """Simula um cachorro sentado em respota a um comando"""
#         print(f"{self.name} is now sitting!")

#     def roll_over(self):
#         """Simula um cachorro rolando em resposta a um comando"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)

# my_dog.sit()
# my_dog.roll_over()

# ---------------------------------------------------------------------------- #
#!                        Criando múltiplas instancias                         #
# ---------------------------------------------------------------------------- #

class Dog:
    """Simples tentativa de modelar um cachorro"""

    def __init__(self, name, age):
        """Inicializa os atributos de nome e idade"""
        self.name = name
        self.age = age


    def sit(self):
        """Simula um cachorro sentado em respota a um comando"""
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your is {your_dog.age} years old")
your_dog.sit()