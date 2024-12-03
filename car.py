""" Classe que pode ser usada para representar um carro"""

class Car:
    """ Tentativa de representar um carro"""
    
    def __init__(self, make, model, year):
        """Inicializa os atributos para descrevr m carro"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro, em milhas"""
        print(f'Este carro tem {self.odometer_reading} milhas rodadas.')
    
    def update_odometer(self, mileage):
        """Define a leitura do hodômetro para o valor fornecido"""
        #self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Não é possível retroceder o hodômetro')
    
    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida à leitura do hodômetro"""
        self.odometer_reading += miles
    
# class Battery:
#     """Bateria do carro elétrico"""
    
#     def __init__(self, battery_size=40):
#         """Inicializa os atributos da bateria"""
#         self.battery_size = battery_size
        
#     def describe_battery(self):
#         """Exibe uma frase descrevendo o tamanho da bateria."""
#         print(f'Este carro tem uma bateria {self.battery_size}-kWh.')
    
#     def get_range(self):
#         """Exibe frase sobre a distância que o carro percorre com essa bateria"""
#         if self.battery_size == 40:
#             range_ = 150
#         elif self.battery_size == 65:
#             range_ = 225
        
#         print(f'Este carro percorre aproximadamente {range_}  milhas com a bateria completamente carregada.')

#     def upgrade_battery(self):
#         if self.battery_size != 65:
#             self.battery_size = 65
#         print(f'Upgrade battery ok. Tamanho da bateria = {self.battery_size}.')
    
# class EletricCar(Car):
#     """Representa aspectos de um carro, específicos para veículos elétricos"""
    
#     def __init__(self, make, model, year):
#         """inicia os atributos da classe-pai.
#         Em seguida, inicializa os atributos específicos para um carro elétrico."""
#         super().__init__(make, model, year)
#         self.battery = Battery()
        
#     def describe_battery(self):
#         """Exibe uma frase descrevendo o tamanho da bateria"""
#         print(f'Este carro tem uma {self.battery_size}-kWh bateria.')
    
#     def fill_gas_tank(self):
#         """Carros elétricos não tem tanque de gasolina"""
#         print('Este carro não tem tanque de gasolina')
