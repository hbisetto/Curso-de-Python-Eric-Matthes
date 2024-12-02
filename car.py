class Car:
    """Classe carro, atributos make, model, year. Métodos: get_descriptive_name."""
    
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
    
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.update_odometer(10)
# my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

