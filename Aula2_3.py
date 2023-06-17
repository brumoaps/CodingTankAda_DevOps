# Crie um programa que receba um número e imprima "fuzz" se o número for múltiplo de 3, "buzz" se deixar resto 1 na divisão por 3 e "nada" se deixar resto 2 na divisão por 3.

num = float(input("Digite um número: "))

if num%3 == 0:
    print("fuzz")
elif num%3 == 1:
    print("buzz")
elif num%3 == 2:
    print("nada")