#Inclua no programa do exercício anterior a possibilidade de o usuário entrar com o par de números desejados quantas vezes quiser, até digitar -1 para sair.

lista_multiplos = []
i = 100

while i<=300:
    if i%10 == 0:
        lista_multiplos.append(i)
        i += 1
    else:
        i+=1

#intervalo

continuation = True
while continuation == True: 
    intervalo1 = int(input("Digite um número entre 0 e 21 para o primeiro marcador (ou -1 para sair): "))
    if intervalo1 == -1:
        break
    intervalo2 = int(input("Digite outro número entre 0 e 21 para o segundo marcador (ou -1 para sair): "))
    if intervalo2 == -1:
        break
    else:
        if intervalo1 > intervalo2:
            intervalo1= int(input("Escolhas inválidas. Tente novamente. Digite um número entre 0 e 21 (ou -1 para sair):  "))
            if intervalo1 == -1:
                break
            else:
                intervalo2= int(input("Digite um número entre 0 e 21 maior que o anterior (ou -1 para sair): "))
            if intervalo2 == -1:
                continuation = False
            else:
                print(f"De {intervalo1} a {intervalo2}, temos: {lista_multiplos[intervalo1:intervalo2]}")
        else:
            print(f"De {intervalo1} a {intervalo2}, temos: {lista_multiplos[intervalo1:intervalo2]}")
    

    
    
        



