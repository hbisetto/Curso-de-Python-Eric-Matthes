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
        
class User:
    """Atributos first_name, last_name, phone, age. Métodos: describe_user(), que exibe um resumo das informações do usuário; e greet_user(), que exibe um cumprimento personalizado ao usuário."""
    
    def __init__(self, first_name, last_name, phone, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.age = age
        self.gender = gender
        self.login_attempts = 0
        
    def describe_user(self):
        print(f'Cliente: {self.first_name}, {self.age} anos, {self.login_attempts} logins')
        
    def greet_user(self):
        if self.gender.lower() == 'm':
            print(f'Olá, senhor {self.last_name}. Bem vindo ao nosso restaurante!')
        elif self.gender.lower() == 'f':
            print(f'Olá, senhora {self.last_name}. Bem vinda ao nosso restaurante!')
        else:
            print(f'Olá, {self.last_name}. Nosso fica feliz em te receber!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
# restaurante1 = Restaurant('Quagliato', 'comercial')
# # print(restaurant.restaurant_name)
# # print(restaurant.cuisine_type)
# # restaurant.describe_restaurant()
# # restaurant.open_restaurant()
# restaurante2 = Restaurant('Cartola', 'executivo')
# restaurante3 = Restaurant('Dorighello', 'italiana')

# restaurante1.describe_restaurant()
# restaurante2.describe_restaurant()
# restaurante3.describe_restaurant()

# user1 = User('Henrique', 'Bisetto', '12371232132', 35, 'M')
# user2 = User('Helga', 'Peres', '813812382', 35, 'F')
# user3 = User('Darci', 'Valares', '2131231293', 40, 'O')

# lista = user1, user2, user3

# for nome in lista:
#     nome.describe_user()
#     nome.greet_user()
    
# print()

# print(restaurante1.number_served)
# restaurante1.increment_number_served()
# print(restaurante1.number_served)
# restaurante1.set_number_served(5)
# print(restaurante1.number_served)
# restaurante1.increment_number_served(12)
# print(restaurante1.number_served)
# restaurante1.describe_restaurant()

# print()

# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.describe_user()
# user1.reset_login_attempts()
# user1.describe_user()