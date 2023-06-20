#A lista resultados abaixo representa 10 vezes em que foi lançado um dado com 6 lados. Usando o FOR juntamente com a função RANGE, crie um programa para contar quantas vezes apareceu um determinado número escolhido pelo usuário.

resultados = [2, 1, 1, 1, 4, 3, 4, 2, 6, 6]
quantidade = 0
escolha = int(input("Digite um número de 1 a 6: "))

for i in range(0, len(resultados)):
    if resultados[i] == escolha:
        quantidade += 1
print(f"O número {escolha} aparece {quantidade} vez(es).")
