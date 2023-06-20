#Com o WHILE, crie uma lista que contenha os números múltiplos de 10 no intervalo de 100 a 300. Depois, peça dois números para o usuário e imprima na tela os elementos da lista cujos índices vão do primeiro ao segundo número digitados pelo usuário. Caso o usuário tente entrar com um intervalo maior do que o tamanho da lista (por exemplo, caso o usuário digite 15 e 25 para a nossa lista contendo apenas 20 elementos) ou caso o usuário entre com o primeiro número maior do que o segundo, digite "Escolhas inválidas".

lista_multiplos = []
i = 100

while i<=300:
    if i%10 == 0:
        lista_multiplos.append(i)
        i += 1
    else:
        i+=1

#intervalo

intervalo1 = int(input("Digite um número entre 0 e 21 para o primeiro marcador: "))
intervalo2 = int(input("Digite outro número entre 0 e 21 para o segundo marcador: "))

if intervalo1 > intervalo2:
    intervalo1= int(input("Escolhas inválidas. Tente novamente. Digite um número entre 0 e 21:  "))
    intervalo2= int(input("Digite um número entre 0 e 21 maior que o anterior: "))
    print(f"De {intervalo1} a {intervalo2}, temos: {lista_multiplos[intervalo1:intervalo2]}")
else:
    print(f"De {intervalo1} a {intervalo2}, temos: {lista_multiplos[intervalo1:intervalo2]}")
