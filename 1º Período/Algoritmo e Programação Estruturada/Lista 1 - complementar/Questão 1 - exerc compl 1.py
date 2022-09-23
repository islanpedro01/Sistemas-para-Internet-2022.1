nome = input("Digite o nome do vendedor:")
ncarros = int(input("Digite o número de carros vendidos:"))
vtotal = float(input("Digite o valor total das vendas:"))

salário = (ncarros*200)+(vtotal*(5/100))+1000

print(f"O salário total do(a) {nome} foi de: {salário:.2f} reais")
