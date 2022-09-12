N = int (input("Digite um número inteiro: "))

i = 0

for i in range (1, N, 1):
    qper = i*i
    if qper <= N:
        maior = qper
print (f'O maior quadrado perfeito menor que {N} é {maior}')
