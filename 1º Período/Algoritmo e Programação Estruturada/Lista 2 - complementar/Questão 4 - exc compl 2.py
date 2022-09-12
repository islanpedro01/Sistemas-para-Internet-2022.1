hinicial = int(input("Digite o horário de início do jogo: "))
hfinal = int(input("Digite o horário de término do jogo: "))

htotal = hfinal - hinicial

if htotal <= 0:
    duração = 24 + htotal

else:
    duração = htotal
    
print(f'O jogo durou {duração} hora(s)!')
