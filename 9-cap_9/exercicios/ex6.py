# ---------------------------------------------------------------------------- #
#!                               9.6 Sorveteria                                #
# ---------------------------------------------------------------------------- #

# Uma sorveteria é um tipo específico de restaurante. 

# Escreva uma classe chamada IceCreamStand que herde da classe Restaurant do Exercício 9.1 (página 210) ou Exercício 9.4 (página 216). 

# Qualquer uma das versões da classe funcionará; basta escolher a que você mais gosta. 

# Adicione um atributo chamado flavors que armazene uma lista de sabores de sorvete. 

# Adicione um método que exiba esses sabores. 

# Crie uma instância a partir de IceCreamStand e chame esse método.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is now open")

    def set_number_served(self, person_served):
        self.number_served = person_served

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['blue ice', 'morango', 'chocolate', 'pistache']

    def get_flavors(self):
        print('Lista de sabores:')
        for flavor in self.flavors:
            print(f"\t- {flavor.title()}")

sorveteria = IceCreamStand('Amoriê', 'Doceria')
sorveteria.describe_restaurant()
sorveteria.get_flavors()