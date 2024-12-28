class Employee:
    """ Classe empregado: nome, sobrenome e salário anual. Métodos: give_raise()"""
    def __init__(self, nome, sobrenome, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.salario = salario
        
    def give_raise(self, aumento=5000):
        self.salario += aumento
        return f'O novo salário de {self.nome} {self.sobrenome} é {self.salario}'
        
    
        
        
    
        
    
        