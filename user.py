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
