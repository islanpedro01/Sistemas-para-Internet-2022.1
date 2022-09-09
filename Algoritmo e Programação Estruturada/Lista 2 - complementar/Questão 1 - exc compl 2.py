num = int(input("Digite um número de 1 até 7: "))

if (num == 1):
    dia = "Domingo"
    util = "Não é dia útil!"
elif (num == 2):
    dia = "Segunda-Feira"
    util = "Dia útil!"
elif (num == 3):
    dia = "Terça-Feira"
    util = "Dia útil!"
elif (num == 4):
    dia = "Quarta-Feira"
    util = "Dia útil!"
elif (num == 5):
    dia = "Quinta-Feira"
    util = "Dia útil!"
elif (num == 6):
    dia = "Sexta-Feira"
    util = "Dia útil!"
elif (num ==7):
    util = "Não é dia util!"
else:
    print('Informe um número válido!')
print (f'O dia da semana é {dia}!')
print (f'{util}')
