num = float (input('Digite um número(999 para interromper):'))
media = 0
i = 0

if num == 999:
    i = 1
    
while num != 999:

    media += num
    i += 1
    num = float (input('Digite outro número: '))
                
calc = media/i

print (f'Programa finalizado!\nMédia calculada: {calc:.1f}')
    
