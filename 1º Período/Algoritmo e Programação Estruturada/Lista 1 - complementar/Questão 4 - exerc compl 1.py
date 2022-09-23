hinicial = float(input("Digite a marcação inicial do hodômetro: "))
hfinal = float (input("Digite a marcação final do hodômetro: "))
combgast = float (input("Digite a quantidade de combustível consumidos (em litros): ")
capac = float(input("Informe a capacidade total do tanque:")
preço = float(input("Informe o valor do litro do combustível:")


kmtotal = hfinal - hinicial
kmlit = kmtotal/combgast
auto = capac*kmlit
custo = combgast*preço

print(f"A quilometragem rodada foi de: {kmtotal:.2f}.")
print(f"O veículo faz {kmlit:.2f} km por litro.")
print(f"A autonomia do veículo é de {auto:.2f} quilômetros.")
print(f"O custo da viagem foi de {custo:.2f} reais.")
       

              
