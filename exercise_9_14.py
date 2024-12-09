from random import choice 

def loteria(possibilidades):
    # possibilities = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'A', 'B', 'C', 'D', 'E')
    list_winner = []
    add = False

    for x in range(4):
        add = False
        while not add:
            option_choose = choice(possibilidades)
            if option_choose in list_winner:
                add = False
            else:
                list_winner.append(option_choose)
                add = True
    return list_winner

# possibilities = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9,'A', 'B', 'C', 'D', 'E')    
# lista_vencedora = loteria(possibilities)

# print("O bilhete vencedor é: ")
# print(lista_vencedora)