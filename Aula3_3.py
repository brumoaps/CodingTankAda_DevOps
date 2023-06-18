#Usando o comando while, crie um script que retorne o somatório de todos os números pares entre 0 e 100.

i = 0
soma = 0
while i<=100:
   if i%2 == 0:
      soma = soma + i
   i +=1

print(f"A soma de todos os números pares entre 0 e 100 é igual a {soma}.")