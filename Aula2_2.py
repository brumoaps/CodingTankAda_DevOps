# Escreva um programa que recebe um número e diz se este é par ou ímpar.

num = int(input("Digite um número: "))

if num%2 == 0:
   print(f"{num} é um número par.")
else:
   print(f"{num} é um número ímpar.")