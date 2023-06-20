# Faça um Programa que leia 20 números inteiros e armazene-os em duas listas: números pares em uma lista PARES e números ímpares em uma uma lista ÍMPARES.

lista_pares = []
lista_impares = []

i = 1

while i <=20:
    num = int(input(f"Digite o número aleatório {i} de 20: "))
    i += 1
    if num%2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f"Os números pares digitados são: {lista_pares}")
print(f"Os números ímpares digitados são: {lista_impares}")