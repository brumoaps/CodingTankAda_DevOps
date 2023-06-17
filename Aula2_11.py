#Faça um programa que leia três números e mostre o maior e o menor deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1>num2 and num1>num3:
    valor_maior = num1
elif num2>num1 and num2>num3:
    valor_maior = num2
elif num3>num1 and num3>num2:
    valor_maior = num3

if num1<num2 and num1<num3:
    valor_menor = num1
elif num2<num1 and num2<num3:
    valor_menor = num2
elif num3<num1 and num3<num2:
    valor_menor = num3

print(f"O maior número é {valor_maior} e o menor número é {valor_menor}")
