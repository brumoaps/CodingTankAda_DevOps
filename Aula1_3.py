#Crie um programa que receba altura e peso e retorne o IMC.

peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))

print("Seu IMC é: " + str(peso/(altura*altura)))