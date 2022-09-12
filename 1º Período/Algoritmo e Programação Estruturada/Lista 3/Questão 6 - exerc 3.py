N = int (input('Digite o 1º número: '))
X = int (input('Digite o 2º número: '))
Y = int (input('Digite o 3º número: '))

i = 0

for i in range (X, Y+1, 1):
    if i%N == 0:
        print (i, end=' ')

        
