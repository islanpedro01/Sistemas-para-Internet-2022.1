from math import*

i = 0

for i in range (50,301,1):
    mult = i%5
    if mult == 0:
        raiz = sqrt(i)
        cubo = i**3
        print(f'Múltiplo de 5: {i} / Raíz: {raiz:.2f} / Cubo: {cubo}')
        
        
    
