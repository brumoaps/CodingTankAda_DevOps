#Refaça o programa anterior, com a seguinte funcionalidade: caso o usuário insira um número negativo, o programa deve solicitar outra entrada, até que uma opção válida seja inserida.

num = int(input("Digite o número até o qual deseja a contagem de números primos: "))
while num < 0:
    num = int(input("Números negativos não podem ser primos. Insira um número inteiro positivo: "))
else:
    while num>0:
        i = 2
        contador = 0
        num_primos = []
        while i<num:
            primo = True
            j = 2
            while j<i:
                if i%j == 0:
                    primo = False
                    break
                j +=1
            if primo:
                contador += 1
                num_primos.append(i)
            i+=1
        print(f"Abaixo do número {num} existem {contador} números primos.")
        print(f"São eles: {num_primos}")
        break
