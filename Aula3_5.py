#Usando o comando while, crie um programa que solicite um número inteiro ao usuário e imprima quantos números primos existem abaixo deste número.

num = int(input("Digite o número até o qual deseja a contagem de números primos: "))
i = 2
contador = 0
num_primos = []
while i<num:
    primo = True
    j = 2
    while j<i:
        if i%j == 0:
            primo = False
            break
        j +=1
    if primo:
        contador += 1
        num_primos.append(i)
    i+=1
print(f"Até o número {num} existem {contador} números primos.")
print(f"São eles: {num_primos}")
        