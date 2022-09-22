num = 'S'
while num != 'N':
    num = int (input('Digite um número inteiro: '))
    if num%2 == 0:
        n = 'é par!'
    else:
        n = 'é ímpar!'
    print(f'O número {num} {n}')
    num = input('\nDeseja continuar o programa?(S/N): ').upper()
print('\nPrograma finalizado!')
