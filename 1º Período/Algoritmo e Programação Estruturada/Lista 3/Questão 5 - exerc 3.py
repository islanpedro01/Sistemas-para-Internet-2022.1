num = int(input('Digite a quantidade pessoas: '))
i = 1
f = 0
m = 0

for i in range (1,num+1,1):
    sexo = input(f'Digite o sexo da {i}ª pessoa (M ou F): ').upper()
    if (sexo == 'M'):
        m += 1
    if (sexo == 'F'):
        f += 1

percm = (100/num)* m
percf = (100/num)* f

print (f'\n{percm:.2f}% das pessoas são do sexo masculino.\n{percf:.2f}% das pessoas são do sexo feminino.')
 
