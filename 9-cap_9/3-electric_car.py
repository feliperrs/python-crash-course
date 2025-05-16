 # --------------------------------------------------------------------------# 
 #!                   Método __init__() para uma classe filha                #  
 # --------------------------------------------------------------------------#

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

#     def increment_odometer(self, miles):
#         """ adiciona a quantidade fornecida á leitura do hodometro """
#         self.odometer_reading += miles


# class ElectricCar(Car):
#     """Representa aspectos de um carro, especificos para veiculos elétricos"""
#     def __init__(self, make, model, year):
#         """Inicializa os atributos da classe-pai"""
#         super().__init__(make, model, year)


# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# ---------------------------------------------------------------------------- #
#!              Definindo atributos e métodos para a classe-filha              #
# ---------------------------------------------------------------------------- #

# class ElectricCar(Car):
#     """Representa aspectos de um carro, especificos para veiculos elétricos"""
#     def __init__(self, make, model, year):
#         """Inicializa os atributos da classe-pai"""
#         super().__init__(make, model, year)
#         """Inicializa os atributos especificos para um carro elétrico"""
#         self.battery_size = 40

#     def describe_battery(self):
#         """Exibe uma frase descrevendo o tamanho da bateria"""
#         print(f"This car has a {self.battery_size}-kWh battery")

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()

# ---------------------------------------------------------------------------- #
#!                 Sobscrevendo métodos a partir da classe-pai                 #
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

#     def increment_odometer(self, miles):
#         """ adiciona a quantidade fornecida á leitura do hodometro """
#         self.odometer_reading += miles

#     def fill_gas_tank(self):
#         """ exibe uma frase sobre o tanque do carro """
#         print('The tank is full!')


# class ElectricCar(Car):
#     """Representa aspectos de um carro, especificos para veiculos elétricos"""
#     def __init__(self, make, model, year):
#         """Inicializa os atributos da classe-pai"""
#         super().__init__(make, model, year)
#         """Inicializa os atributos especificos para um carro elétrico"""
#         self.battery_size = 40

#     def describe_battery(self):
#         """Exibe uma frase descrevendo o tamanho da bateria"""
#         print(f"This car has a {self.battery_size}-kWh battery")

#     def fill_gas_tank(self):
#         """ altera um método da classe-pai """
#         print("This car doesn't have a gas tank!")


# normal_car = Car('subaru', 'outback', 2019)
# electric_car = ElectricCar('nissan', 'leaf', 2024)

# normal_car.fill_gas_tank()
# electric_car.fill_gas_tank()
# normal_car.fill_gas_tank()

# ---------------------------------------------------------------------------- #
#!                          Instancias como atributos                          #
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

    def fill_gas_tank(self):
        """ exibe uma frase sobre o tanque do carro """
        print('The tank is full!')

class Battery:
    """Simples tentativa de modela uma bateria para um carro eletrico"""
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def descibre_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kWh battery!")

    def get_range(self):
        """Exibe frase sobre a distancia que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Inicializa os atributos especificos para um carro elétrico"""
        super().__init__(make, model, year)
        """Usa a classe battery"""
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.descibre_battery()
my_leaf.battery.get_range()