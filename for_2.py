#Faça exatamente o que foi feito no exerćicio anterior, mas usando o FOR para percorrer diretamente a lista, isto é, sem usar a função RANGE.

resultados = [2, 1, 1, 1, 4, 3, 4, 2, 6, 6]
quantidade = 0
escolha = int(input("Digite um número de 1 a 6: "))
i=1
contador = len(resultados)
for resultado in resultados:
    if resultado == escolha:
        quantidade += 1
print(f"O número {escolha} aparece {quantidade} vez(es).")