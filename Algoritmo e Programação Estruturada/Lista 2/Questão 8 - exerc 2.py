num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Informe abaixo a operação que deseja realizar:")
op = input("-> Adição: +\n-> Subtração: -\n-> Multiplicação: x\n-> Potenciação: *\n-> Divisão: /\n-> Porcentagem: %\n ")

if (op == '+'):
    soma = num1+num2
    result = soma
elif(op == '-'):
    sub = num1-num2
    result = sub
elif(op == 'x'):
    mult = num1*num2
    result = mult
elif(op == '*'):
    pot = num1**num2
    result = pot
elif(op == '/'):
    div = num1/num2
    result = div
elif(op == '%'):
    porc = (num1/100)*num2
    result = porc
else:
    print("Digite um operador válido!")

print("O resultado é: ",result)
    

