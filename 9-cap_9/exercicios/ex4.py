# ---------------------------------------------------------------------------- #
#!                            9.4 Pessoas atendidas                            #
# ---------------------------------------------------------------------------- #

# Comece com o seu programa do Exercício 9.1 (página 210). 

# Adicione um atributo chamado number_served com um valor default de 0. 

# Crie uma instância chamada restaurant a partir dessa classe. 

# Exiba o número de clientes que o restaurante atendeu e, em seguida, altere este valor e o exiba novamente.

# Adicione um método chamado set_number_served(), o qual possibilita definir o número de clientes atendidos. 

# Chame esse método com um novo número e exiba mais uma vez o valor.

# Adicione um método chamado increment_number_served(), o qual possibilita aumentar o número de clientes atendidos. 

# Chame esse método com qualquer número que quiser que possivelmente quantos clientes foram atendidos em, digamos, um dia de atividade comercial.

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

restaurant = Restaurant('Coco Bambu', 'Sea Food')
print(restaurant.number_served)
restaurant.number_served = 10
print(restaurant.number_served)
restaurant.set_number_served(50)
print(restaurant.number_served)
restaurant.increment_number_served(25)
print(restaurant.number_served)