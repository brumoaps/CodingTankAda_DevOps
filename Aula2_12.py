# Crie um programa que faça as seguintes 5 perguntas e diagnostique o paciente:
# A. Sente dor no corpo?
# B. Tem febre?
# C. Tem tosse?
# D. Está com congestão nasal?
# E. Tem manchas no corpo?
#Condições: se apenas a primeira for verdade, o paciente não está doente; Se B, C e D forem verdade, o paciente está com gripe; Se todas forem verdade, paciente está com Dengue; Caso contrário, não temos o diagnóstico.

a = (input("Sente dor no corpo?: ")).lower()
b = (input("Tem febre? ")).lower()
c = (input("Tem tosse? ")).lower()
d = (input("Está com congestão nasal? ")).lower()
e = (input("Tem manchas no corpo? ")).lower()

if a == "sim" and b == "não" and c == "não" and d == "não" and e == "não":
    print("O paciente não está doente.")
elif a == "não" and b == "sim" and c == "sim" and d == "sim" and e == "não":
    print("O paciente está com dengue.")
else:
    print("Não temos o diagnóstico.")