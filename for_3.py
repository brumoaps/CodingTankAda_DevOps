#Crie uma lista que tenha todos os números múltiplos de 7, de 0 a 100, usando o FOR.

lista_multiplos = []
i = 0

for i in range(0,100):
    if i%7 == 0:
        lista_multiplos.append(i)
        i +=1
    else:
        i += 1
print(lista_multiplos)