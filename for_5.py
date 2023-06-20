#Crie um programa que retorne o somatório de todos os números entre 1 e um número fornecido pelo usuário.

soma = 0
i = 1
num = int(input("Digite um número inteiro positivo: "))

for i in range(1, num + 1):
    soma = soma + i
print(soma)
