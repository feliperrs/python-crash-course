# ---------------------------------------------------------------------------- #
#!                                 8.14 Carros                                 #
# ---------------------------------------------------------------------------- #

# Crie uma função que armazene informações sobre um carro em um dicionário. 

# A função deve sempre receber um fabricante e um nome de modelo. 

# Em seguida, deve aceitar um número arbitrário de argumentos nomeados. 

# Chame a função com as informações necessárias e dois outros pares nome-valor, como uma cor ou um recurso opcional. 

# Sua função deve funcionar mais ou menos assim:

# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Exiba o dicionário retornado para garantir que todas as informações foram corretamente armazenadas.


def make_car(fabricante, modelo, **car_info):
    car_info['fabricante'] = fabricante
    car_info['modelo'] = modelo
    return car_info


car = make_car(
    'subaru', 
    'outback', 
    color='blue', 
    tow_package=True
    )
print(car)


car  = make_car(
    'Toyota', 
    'Corolla', 
    color='prata', 
    motor='1.8 Flex'
    )  
print(car)

car = make_car(
    'Volkswagen', 
    'Golf', 
    year=2022, 
    transmission='automática', 
    fuel='gasolina', 
    color='preto'
    )  
print(car)

car = make_car(
    'Porsche', '911 GT3', 
    horsepower=510, 
    traction='4x4', 
    top_speed=318
    )
print(car)

car = make_car(
    'Tesla', 
    'Model S', 
    electric=True, 
    battery='100 kWh', 
    range_km=637
    )
print(car) 