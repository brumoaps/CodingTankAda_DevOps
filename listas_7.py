#Faça um Programa que leia uma lista de 5 números reais e mostre-os na ordem inversa. NÃO VALE USAR REVERSE

lista_reais = []
lista_reversa = []
i=1
j = 4
while 1<=i<=5:
    num = int(input("Digite um número: "))
    lista_reais.append(num)
    i += 1
print(lista_reais)

while j>=0:
    lista_reversa.append(lista_reais[j])
    j -= 1
print(lista_reversa)
