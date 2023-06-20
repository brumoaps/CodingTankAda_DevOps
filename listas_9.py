#a) Faça um programa que permita ao usuário inserir quantos números quiser em uma lista, até que ele passe -1.

#b) Depois disso, crie um programa em que o usuário possa solicitar, por quantas vezes quiser qualquer uma das seguintes opções, até que pressione "S" ou "s" para encerrar:

#"med" para ver a média dos números da lista
#"max" para ver o maior número da lista
#"min" para ver o menor número da lista
#"list" para ver a lista
#"tsil" para ver a lista invertida

lista_num = []

continuation = True
while continuation == True:
    num = int(input("Digite um número positivo para adicionar à lista (ou -1 para fechar a lista): "))
    if num == -1:
        break
    else:
        lista_num.append(num)

print("""
Digite:
'med' para ver a média dos números da lista
'max' para ver o maior número da lista
'min' para ver o menor número da lista
'list' para ver a lista
'tsil' para ver a lista invertida
""")
continuation_2 = True
while continuation_2 == True:
    opcao = (input("Digite a opção desejada ou 'S' para sair: ")).lower()
    if opcao == "s":
        continuation_2 = False
    elif opcao == "med":
        sum = 0
        for _ in lista_num:
            sum +=_
            media = sum/len(lista_num)
        print(f"A média dos números da lista é igual a {media}")
        
    elif opcao == "max":
        max = lista_num[0]
        for _ in lista_num:
            if _ > max:
                max = _
        print(f"O maior número da lista é {max}.")
        
    elif opcao == "min":
        min = lista_num[0]
        for _ in lista_num:
            if _ < min:
                min = _
        print(f"O menor número da lista é {min}.")
        
    elif opcao == "list":
        print(f"A lista informada é: {lista_num}.")
        
    elif opcao == "tsil":
        j = len(lista_num) - 1
        lista_reversa = []
        while j>=0:
            lista_reversa.append(lista_num[j])
            j -= 1
        print(f"A lista invertida é {lista_reversa}.")
        
