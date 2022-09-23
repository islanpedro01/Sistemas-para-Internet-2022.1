num = int(input("Digite a quantidade de segundos: "))
horas = num // 3600
minutos = (num%3600)//60
seg = (num%3600)%60

print(f"{horas} horas, {minutos} minutos e {seg} segundos")
