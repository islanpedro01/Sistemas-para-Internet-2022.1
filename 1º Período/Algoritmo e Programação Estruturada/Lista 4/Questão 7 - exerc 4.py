idade = int(input('INFORME A IDADE (Digite 0 para encerrar o programa): '))
total = 0
menor = idade
soma = 0
num = 0

if idade == 0:
    print ('\nPrograma finalizado!')
else:
    while idade != 0:
        soma += idade
        total += 1
        if idade <= menor:
            menor = idade
        if idade >= 18 and idade <= 21:
            num += 1
        idade = int(input('INFORME A IDADE (Digite 0 para encerrar o programa): ' ))
    media = soma/total
    perc = (num/total)*100

    print (f'\nA média de idade do público é: {media:.1f} anos.')
    print (f'A porcentagem de pessoas na faixa entre 18 e 21 anos é: {perc:.1f}%')
    print (f'A idade do visitante mais jovem é: {menor} anos.')
    print ('\nPrograma finalizado!')
