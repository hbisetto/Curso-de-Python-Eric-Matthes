class Restaurant:
    """ A classe Restaurant tem como atributos: restaurat_name e cuisine_type. E tem como métodos describe_restaurant(), que exibe estas duas informações, e open_restaurant(), que exibe uma mensagem sinalizando que o restaurante está aberto"""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Inicializa os atributos"""
        self.restaurant_name =  restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Método que descreve o restaurante com as informações de restaurant_name e cuisine_type"""
        print(f'Informações sobre o restaurante: Nome: {self.restaurant_name}, tipo de cozinha: {self.cuisine_type}, total de atendimentos: {self.number_served}')
                
    def open_restaurant(self):
        """Mensagem avisando que o restaurante está aberto"""
        print(f'O restaurante {self.restaurant_name} está aberto!')
        
    def increment_number_served(self, num=1):
        """Adiciona ao numero de serviços"""
        self.number_served += num
        
    def set_number_served(self, num):
        self.number_served = num
