#Crie um script que retorne o somatório de todos os números pares entre 0 e 100, usando o FOR.

soma = 0
i = 0

for i in range(0, 101):
    if i%2 == 0:
        soma = soma + i
        i += 1
    else:
        i += 1

print(soma)