num = int (input('Digite um número inteiro: '))
i = 0
soma = 0
for i in range (1, num+1, 1):
    soma += i
print(f'A soma dos números de 1 até {num} é: {soma} ')
