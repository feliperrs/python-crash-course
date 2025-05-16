# ---------------------------------------------------------------------------- #
#!                            9.2 Três restaurantes                            #
# ---------------------------------------------------------------------------- #

# Comece com sua classe do Exercício 9.1. 

# Crie três instâncias diferentes da classe e chame describe_restaurant() para cada instância.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}\n")

    def open_restaurant(self):
        print("The restaurant is now open")

restaurant0 = Restaurant('Coco Bambu', 'Sea Food')
restaurant1 = Restaurant('McDonalds', 'Fast food')
restaurant2 = Restaurant('China in Box', 'Chinese')

restaurant0.describe_restaurant()
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()