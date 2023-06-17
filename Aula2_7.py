# Faça um programa que inicialmente receba 2 notas parciais de um aluno (prova 1 e prova 2). Se a média de ambas as notas for superior ou igual a 7, o programa retorna "APROVADO". Senão, o programa solicita uma nota adicional, a nota do provão. Tendo a nota do provão, se a média das 3 notas for maior ou igual a 7 ou se pelo menos duas das 3 notas for maior ou igual a 6, imprima "APROVADO POR POUCO!". Senão, imprima "QUE PENA! TENTE FAZER A SÉTIMA SÉRIE OUTRA VEZ!".

nota1 = float((input("Digite a nota da prova 1: ")).replace(",", "."))
nota2 = float((input("Digite a nota da prova 2: ")).replace(",", "."))
media_final = round(((nota1 + nota2)/2), 1)

if media_final>=7:
    print("APROVADO!")
else:
    nota3 = float((input("Digite a nota do provão: ")).replace(",", "."))
    media_rec = round(((nota1 + nota2 + nota3)/3), 1)
    if media_rec>=6:
        print("APROVADO POR POUCO!")
    else: 
        print("QUE PENA! TENTE FAZER A SÉTIMA SÉRIE OUTRA VEZ!")