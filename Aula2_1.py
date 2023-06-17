# Faça um programa que receba o nome e a idade de um usuário e no final diga algo do tipo "Thiago já está apto a tirar sua habilitação de motorista e esta será válida até que ele complete 39 anos". Considere 10 anos como o período de validade de uma habilitação no Brasil.

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
idade_apta = 18
idade_futura = idade + 10
tempo_que_falta = idade_apta - idade

if idade >= idade_apta:
    print(f"{nome} já está apto(a) a tirar sua cnh e esta será válida até que ele(a) complete {idade_futura} anos.")
else:
    print(f"{nome} ainda não está apto(a) a tirar sua cnh. Ainda faltam {tempo_que_falta} anos.")
