num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if(num1>num2 and num1>num3):
    print(f"O maior número é o {num1}.")
elif(num2>num1 and num2>num3):
    print(f"O maior número é o {num2}.")
else:
    print(f"O maior número é o {num3}.")
