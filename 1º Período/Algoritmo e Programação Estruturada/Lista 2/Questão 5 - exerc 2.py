vtotal = float(input("Digite o valor total de vendas: "))
salmin = 1212.00
porcent = 5/100
saltotal = porcent * vtotal

if saltotal < salmin:
    saltotal = salmin

print (f"O salário total é de {saltotal} reais!")
    

