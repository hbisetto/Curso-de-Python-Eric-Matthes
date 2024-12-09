from exercise_9_14 import loteria

win = False
my_ticket = [0, 3, 4, 'E']
# my_ticket_teste = ['E', 3, 4, 0]
possibilities = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'A', 'B', 'C', 'D', 'E') 
contagem = 0

while not win:
    contagem += 1
    sorteados = loteria(possibilities)
    if set(sorteados) == set(my_ticket):
        win = True
    
print(f'Número de vezes que foi sorteado até vencer: {contagem}')