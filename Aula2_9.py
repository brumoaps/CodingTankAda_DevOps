# Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino, V-vespertino ou N-noturno. Imprima a mensagem "Bom dia!", "Boa tarde!", "Boa noite!" ou "Valor inválido!", conforme o caso.

M = "matutino"
V = "vespertino"
N = "noturno"

print("""
M = 'matutino'
V = 'vespertino'
N = 'noturno'
""")

turno = (input("Digite a letra que identifica o seu turno: ")).capitalize()


if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")

