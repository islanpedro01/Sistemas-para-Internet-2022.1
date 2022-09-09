ano = int(input("Digite um ano para saber se ele e bissexto ou não: "))

div4 = ano%4
div100 = ano%100
div400 = ano%400

print(div4, div100, div400)
if (div4 == 0) and (div100 != 0):
    biss = 'é bissexto'

elif (div4 == 0) and (div100 == 0) and (div400 == 0):
    biss = 'é bissexto'
    
else:
    biss = 'não é bissexto'

print(f'O ano {ano} {biss}!')
    
