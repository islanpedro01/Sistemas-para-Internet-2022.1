bits = int(input("Digite a quantidade de bits desejado: "))

bit50 = bits//50
bit10 = (bits%50)//10
bit5 = (bits%50)%10//5
bit1 = ((bits%50)%10)%5//1

print(f"- {bit50} nota(s) de B$ 50.\n- {bit10} nota(s) de B$ 10.\n- {bit5} notas(s) de B$ 5.\n- {bit1} nota(s) de B$1.")
