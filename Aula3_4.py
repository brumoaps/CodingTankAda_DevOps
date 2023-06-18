#Crie um programa que receba quantas notas o professor quiser de um aluno e pare quando o professor inserir a letra "S". Quando parar, o programa deve retornar a média das notas digitadas e dizer se o aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

inf = ""
i = 0
soma = 0
media = 0
while inf!="S":
    inf = (input("Digite uma nota de 0 a 10 ou S para sair: ")).capitalize()
    if inf != "S":
        inf = float((inf).replace(",", "."))
        soma = soma + inf
        i += 1
    media = soma/i

if media >=7:
   print (f"A média é igual a {round(media,1)} e, portanto, o aluno foi aprovado.")
else:
   print(f"A média é igual a {round(media,1)} e, portanto, o aluno foi reprovado.")