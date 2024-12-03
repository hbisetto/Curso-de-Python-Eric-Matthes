""" Conjunto de classes que pode ser usado para representar carros elétricos"""
from car import Car    
class EletricCar(Car):
    """Representa aspectos de um carro, específicos para veículos elétricos"""
    
    def __init__(self, make, model, year):
        """inicia os atributos da classe-pai.
        Em seguida, inicializa os atributos específicos para um carro elétrico."""
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f'Este carro tem uma {self.battery_size}-kWh bateria.')
    
    def fill_gas_tank(self):
        """Carros elétricos não tem tanque de gasolina"""
        print('Este carro não tem tanque de gasolina')
            
class Battery:
    """Bateria do carro elétrico"""
    
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria."""
        print(f'Este carro tem uma bateria {self.battery_size}-kWh.')
    
    def get_range(self):
        """Exibe frase sobre a distância que o carro percorre com essa bateria"""
        if self.battery_size == 40:
            range_ = 150
        elif self.battery_size == 65:
            range_ = 225
        
        print(f'Este carro percorre aproximadamente {range_}  milhas com a bateria completamente carregada.')

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
        print(f'Upgrade battery ok. Tamanho da bateria = {self.battery_size}.')
            
            
# my_leaf = EletricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# #my_leaf.fill_gas_tank()
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

my_leaf = EletricCar('Nisan', 'leaf', 2024)
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
