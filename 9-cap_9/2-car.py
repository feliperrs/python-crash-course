# ---------------------------------------------------------------------------- #
#!                    Trabalhando com classes e instancias                     #
# ---------------------------------------------------------------------------- #

# class Car:
#     """Simples tentativa de representar um carro"""

#     def __init__(self, make, model, year):
#         """inicializa os atributos para descrever um carro"""
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         """retorna um nome descritivo, formatando elegantemente"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name
       
# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())

# ---------------------------------------------------------------------------- #
#!                 Definindo um valor default para um atributo                 #
# ---------------------------------------------------------------------------- #

# class Car:
#     """Simples tentativa de representar um carro"""

#     def __init__(self, make, model, year):
#         """inicializa os atributos para descrever um carro"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0


#     def get_descriptive_name(self):
#         """retorna um nome descritivo, formatando elegantemente"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name
    
#     def read_odometer(self):
#         """ exibe uma frase mostrando a quilometragem do carro, em milhas"""
#         print(f"This car has {self.odometer_reading} miles on it")
    


# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# ---------------------------------------------------------------------------- #
#!                Modificando valores de atributos diretamente                 #
# ---------------------------------------------------------------------------- #

# class Car:
#     """Simples tentativa de representar um carro"""

#     def __init__(self, make, model, year):
#         """inicializa os atributos para descrever um carro"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0


#     def get_descriptive_name(self):
#         """retorna um nome descritivo, formatando elegantemente"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name
    
#     def read_odometer(self):
#         """ exibe uma frase mostrando a quilometragem do carro, em milhas"""
#         print(f"This car has {self.odometer_reading} miles on it")
    


# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# ---------------------------------------------------------------------------- #
#!           Altereando o valor de um atributo por meio de um metodo           #
# ---------------------------------------------------------------------------- #

# class Car:
#     """Simples tentativa de representar um carro"""

#     def __init__(self, make, model, year):
#         """inicializa os atributos para descrever um carro"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0


#     def get_descriptive_name(self):
#         """retorna um nome descritivo, formatando elegantemente"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name
    
#     def read_odometer(self):
#         """ exibe uma frase mostrando a quilometragem do carro, em milhas"""
#         print(f"This car has {self.odometer_reading} miles on it")

#     def update_odometer(self, mileage):
#         """Define a eitura do hodometro para o valor fornecido"""
#         self.odometer_reading = mileage


# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

# ---------------------------------------------------------------------------- #
#!         Incrementando o valor de um atributo por meio de um metodo          #
# ---------------------------------------------------------------------------- #

class Car:
    """Simples tentativa de representar um carro"""

    def __init__(self, make, model, year):
        """inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """retorna um nome descritivo, formatando elegantemente"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """ exibe uma frase mostrando a quilometragem do carro, em milhas"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Define a eitura do hodometro para o valor fornecido"""
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """ adiciona a quantidade fornecida á leitura do hodometro """
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(499)
my_used_car.read_odometer()