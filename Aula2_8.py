# Faça um programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite mais um número: "))
num3 = int(input("Digite um outro número: "))

if num1>num2>num3:
    print(f"{num1}, {num2}, {num3}")
elif num1>num3>num2:
    print(f"{num1}, {num3}, {num2}")
elif num2>num1>num3:
    print(f"{num2}, {num1}, {num3}")
elif num2>num3>num1:
    print(f"{num2}, {num3}, {num1}")
elif num3>num1>num2:
    print(f"{num3}, {num1}, {num2}")
elif num3>num2>num1:
    print(f"{num3}, {num2}, {num1}")