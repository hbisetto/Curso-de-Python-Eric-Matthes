from random import randint, choice

# randint: Essa função aceita dois argumentos inteiros e retorna um número inteiro selecionado aleatoriamente entre (e incluindo) esses números.

# choice: Essa função aceita uma lista ou tupl a e retorna um elemento aleatoriamente escolhido:

print(randint(1, 6))

players = ['charles', 'martina', 'michal', 'florence', 'eli']
first_up = choice(players)
print(first_up)