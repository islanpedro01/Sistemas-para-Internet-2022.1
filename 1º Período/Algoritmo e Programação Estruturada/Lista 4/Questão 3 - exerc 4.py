num = float (input('Digite um número (0 para sair): '))
maior = num
menor = num

while num != 0:
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num
   num = float (input('Digite um número (0 para sair): '))
    
print (f'O maior número é {maior}! O menor número é {menor}!')
    
