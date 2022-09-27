mat = input('Digite a matrícula do aluno (0 para finalizar): ')

while mat != 0:
    nome = input('Digite o nome do aluno: ')
    nota1 = float (input('Digite a nota da 1ª avaliação: '))
    nota2 = float (input('Digite a nota da 2ª avaliação: '))
    media = (nota1+nota2)/2
    if media >= 7:
        sit = 'Aprovado(a)!'
    else:
        sit = 'Reprovado(a)!'
    print (f'\nAluno(a): {nome}')
    print (f'Matrícula: {mat}')
    print (f'Média: {media:.2f}')
    print (f'Situação: {sit}\n')
    print('Para finalizar o programa digite 0 no campo da matrícula!\n')
    mat = int (input('Digite a matrícula do aluno: '))     

print('Programa finalizado!')
    
