nota1 = float(input('Digite a nota da primeira prova do candidato: '))
nota2 = float(input('Digite a nota da segunda prova do candidato: '))

media = (nota1+nota2)/2

if media >= 7:
    nota3 = float(input('O aluno foi aprovado para a segunda etapa.\n\nAgora, digite a nota da segunda etapa: '))
    if nota3 >= 8:
        sit = 'APROVADO'
    else:
        sit = 'REPROVADO'
else:
    sit = 'REPROVADO'

print (f'O aluno foi {sit} no concurso!')
    
