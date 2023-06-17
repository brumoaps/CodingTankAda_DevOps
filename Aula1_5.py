#Construa um programa que receba uma idade e um nome e imprima uma saída do tipo "Adriele tem 22 anos.". No entanto, desta vez, considere a idade que o usuário terá daqui a 15 anos e não a idade que o usuário tem no momento da execução do programa.

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

idade_futuro = str(idade + 15)

print(nome + " terá " + idade_futuro + " anos daqui 15 anos.")