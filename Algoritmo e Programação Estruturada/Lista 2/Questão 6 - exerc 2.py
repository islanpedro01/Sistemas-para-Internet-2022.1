nome = input("Digite o nome do(a) aluno(a): ")
conceito = input("Digite o conceito do(a) aluno(a): ")

if conceito == 'A':
    print(f"Aluno(a) {nome} fortemente recomendado(a).")
elif conceito == 'B' or conceito == 'C':
    print(f"Aluno(a) {nome} recomendo(a).")
elif conceito =='D':
    print(f"Aluno(a) {nome} não recomendado(a).")
else:
    print(f"Por gentileza, digite um conceito válido.\nOBS: O programa entende apenas letras maiúsculas.")
    
