print("Soma de dois números")

while True:
    try: 
        num_1 = int(input("Digite o primeiro número: "))
    except ValueError:
        print("Não foi digitado um número válido. Por favor, digite um número inteiro.")
    else:
        break

while True:
    try: 
        num_2 = int(input("Digite o segundo número: "))
    except ValueError:
        print("Não foi digitado um número válido. Por favor, digite um número inteiro.")
    else:
        break

print(f"Ok. Os números digitados foram {num_1} e {num_2}.")
result = num_1 + num_2
print(f"A soma de  {num_1} + {num_2} é {result}")    