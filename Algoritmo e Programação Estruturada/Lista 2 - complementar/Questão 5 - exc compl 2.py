from math import*

A = float(input('Digite o valor de A: '))
B = float(input('Digite o valor de B: '))
C = float(input('Digite o valor de C: '))

delta = (B**2)-(4*A*C)

if delta >= 0:
    x1 = (-B + sqrt(delta))/2*A
    x2 = (-B - sqrt(delta))/2*A
else:
    print('A raíz da equação é inexistente!')

print(f'As raízes da equação são: {x1:.2f} e {x2:.2f}')
    
