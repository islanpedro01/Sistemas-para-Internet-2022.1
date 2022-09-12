num = int(input('Digite um número: '))

i = 0
cont = 0

for i in range (1, num+1, 1):
    
    if num%i == 0:
        cont += 1

if cont == 2:
    prim = 'é primo'

else:
    prim = 'não é primo'

print (f'O número {num} {prim}! ')
