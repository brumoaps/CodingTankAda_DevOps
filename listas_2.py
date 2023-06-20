#Com a lista criada no exercício anterior, use o método append para:
#a) Adicionar um booleano ao fim da lista.
#b) Adicionar uma lista com as três primeiras letras do alfabeto ao fim da lista.
#c) Adicionar um booleano ao fim da lista criada no item (b)

lista = [5.5, "Boa noite!", [1, 2, 3], True]

#a)

lista.append(False)
print(lista)

#b)

lista.append(["a", "b", "c"])
print(lista)

#c)

lista[5].append(True)
print(lista)