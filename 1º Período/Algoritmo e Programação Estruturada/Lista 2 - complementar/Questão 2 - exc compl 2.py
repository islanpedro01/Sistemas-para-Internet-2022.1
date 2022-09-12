carac = input("Digite um caractere: ").upper()


if (carac >= 'A') and (carac <= 'Z'):
    definição = 'consoante'
    if carac in ('A', 'E', 'I', 'O', 'U'):
        definição = 'vogal'
        
elif (carac >= '0') and (carac <= '9'):
    definição = 'número'
       
else:
    definição = 'caractere especial'

print(f'O caractere digitado é um(a) {definição}!')
    
