from random import randint

class Die:
    """ Representa um dado com valor default de lados = 6"""
    
    def __init__(self, side=6):
        self.side = side
        
    def roll_die(self):
        """método que lança os dados e retorna um valor random"""
        number = randint(1, self.side)
        return number

def lancar_10x(die):  
    """ Função que lança um dado 10x, imprimindo os valores sorteados aleatoriamente entre as possibilidades de lados do dado. Recebe um objeto Die() como parâmetro"""  
    for x in range(10):
        number = die.roll_die()
        print(number)
    
dado = Die()
lancar_10x(dado)
print()
dado_10 = Die(10)
lancar_10x(dado_10)
print()
dado_20 = Die(20)
lancar_10x(dado_20)
    
