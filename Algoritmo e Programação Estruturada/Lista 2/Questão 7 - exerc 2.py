peso = float(input("Digite o peso (kg) do indivíduo: "))
altura = float(input("Digite a altura (m) do indivíduo: "))

imc = peso/(altura**2)
print (imc)

if imc < 26:
    print("Sua situação é considerada Normal.")
elif imc >= 26 and imc < 30:
    print("Você é considerado(a) Obeso(a).")
else:
    print("Você sofre de obesidade mórbida.")
