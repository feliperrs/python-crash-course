# ---------------------------------------------------------------------------- #
#!                             9.9 Trocar bateria                              #
# ---------------------------------------------------------------------------- #

# Utilize a versão final do electric_car.py dessa seção. 

# Adicione um método à classe Battery chamado upgrade_battery(). 

# Esse método deve verificar o tamanho da bateria e definir a capacidade como 65, caso necessário. 

# Crie um carro elétrico com um tamanho default de bateria, chame get_range() uma vez e, depois, chame get_range() uma segunda vez, após atualizar a bateria.

# Você deve ver aumento no alcance de distância do carro.

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

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Inicializa os atributos especificos para um carro elétrico"""
        super().__init__(make, model, year)
        """Usa a classe battery"""
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()