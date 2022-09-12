i = 0
maior = 0

for i in range (20):
    num = int(input("Digite um número inteiro: "))
    if num > maior:
        maior = num
print (f'O maior número digitado foi {maior}!')
