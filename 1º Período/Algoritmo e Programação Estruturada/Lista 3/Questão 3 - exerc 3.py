num = int (input('Digite um número inteiro: '))

i = 0
N = 1

print (f'{num}! =', end=' ')

for i in range (1, num+1, 1):
    N *= i
    if i < num:
        print (i, end=' x ')
    else:
        print (i, end='')
        
print(f' = {N}')
