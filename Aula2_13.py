# Para entrar em um carro de palhaço, os palhaços precisarão respeitar as seguintes condições:
# Ter entre 20 e 30 anos, entre 40 e 50 anos ou entre 70 e 75 anos apenas;
# Os palhaços mais velhos irão no banco da frente, os mais novos no porta-malas e a idade que restou irá no banco de trás.
#Crie um programa que receba a idade do palhaço e imprima os seguintes passos, NESTA ORDEM:
#1) Indique se o palhaço poderá entrar no carro;
#2) Indique onde o palhaço ficará no carro.

idade = int(input("Digite sua idade: "))

if 20<=idade<=30 or 40<=idade<=50 or 70<=idade<=75:
    print("O palhaço pode entrar no carro.")
else:
    print("O palhaço não pode entrar no carro.")

if 20<=idade<=30:
    print("O palhaço irá no pota-malas.")
elif 40<=idade<=50:
    print("O palhaço irá no banco de trás.")
elif 70<=idade<=75:
    print("O palhaço irá no banco da frente.")
else:
    print("")
