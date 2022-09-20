N = int (input("Digite um número inteiro: "))

i = 1

for i in range (1, N+1, 1):
    qper = i*i
    if qper <= N:
        maior = qper
print (f'O maior quadrado perfeito menor ou igual a {N} é {maior}')
