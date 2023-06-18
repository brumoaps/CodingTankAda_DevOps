# Crie o programa "Bart Simpson": ele recebe um número de vezes e uma frase, e imprime na tela a mesma frase até atingir o número de vezes solicitado.

frase = input("Digite a frase que você quer que seja repetida: ")
num = int(input("Digite o número de vezes que você quer que a frase seja repetida: "))

i = 1

while i<=num:
    print(frase)
    i +=1