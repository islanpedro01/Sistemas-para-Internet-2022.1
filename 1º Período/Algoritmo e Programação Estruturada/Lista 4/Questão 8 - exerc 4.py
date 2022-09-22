print('             CARDÁPIO            ')
print('\nCÓDIGO ------- ITEM -------------- PREÇO')
print('\n  H -------- Hamburguer --------- R$ 5,00')
print('  C ------ Cheese Burguer ------- R$ 6,00')
print('  B ------- Cheese Bacon -------- R$ 7,00')
print('  F ------- Cheese Frango ------- R$ 4,00')
print('\n  X -------------------- ENCERRA PEDIDO')

cod = input('\nDigite o código do pedido: ').upper()
total = 0
soma = 0

while cod != 'X':
    qnt = int (input('Digite a quantidade: '))
    if cod == 'H':
        total = qnt * 5
        soma += total
    elif cod == 'C':
        total = qnt * 6
        soma += total
    elif cod == 'B':
        total = qnt * 7
        soma += total
    elif cod == 'F':
        total = qnt * 4
        soma += total
    else:
        print('Digite um código presente no cardápio!')
        
    cod = input('\nDigite o código do pedido (X encerra o pedido): ').upper()
        
print (f'\nTotal a pagar: R$ {soma:.2f}')
print ('\nPrograma finalizado!')
