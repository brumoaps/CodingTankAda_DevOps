# Crie um programa que recebe sua altura e seu peso, calcula o imc e retorna um status (abaixo do peso, no peso, acima do peso).

peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))
imc = round(peso/(altura*2),1)

if imc<18.5:
    print("Esta pessoa está abaixo do peso")
elif 18.5<=imc<=24.9:
    print("Esta pessoa está no peso normal")
elif imc>=25:
    print("Esta pessoa está acima do peso")
