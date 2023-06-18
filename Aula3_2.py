#Crie um programa que retorne o somatório de todos os números entre 1 e um número fornecido pelo usuário.

num = int(input("Digite o número até o qual você quer que a soma seja feita: "))

i = 0
soma = 0
while i<=num:
    soma = soma + i
    i += 1

print(f"A soma de todos os números no intervalo de 1 a {num} é igual a {soma}.")
