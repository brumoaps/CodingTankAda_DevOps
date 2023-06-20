#Crie uma lista que tenha todos os números múltiplos de 7, de 0 a 100, usando o WHILE.

lista_multiplos = []
i = 0

while i<=100:
    if i%7 == 0:
        lista_multiplos.append(i)
        i += 1
    else:
        i+=1
print(lista_multiplos)
    