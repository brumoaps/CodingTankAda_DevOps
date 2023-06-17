# Você quer pintar sua casa e está em dúvida entre as cores Azul, Vermelhor e Magenta. Sabendo que a tinta Azul custa 25,00 reais por metro quadrado, Vermelho custa 35 e Magenta custa 45, faça o seguinte:

# b) Crie um programa que recebe largura, altura, número de paredes e a cor da tinta escolhida e então retorne quanto gastará com tinta.

custo_azul = 25
custo_vermelho = 35
custo_magenta = 45

cor_selecionada = input("Informe a cor desejada: ").lower()
n_paredes = int(input("Quantas paredes serão pintadas com esta cor? Digite: "))
metragem_total = 0

for i in range(1, n_paredes + 1):
    altura_parede = float((input(f"Digite a altura da parede {i}: ")).replace(",", "."))
    largura_parede = float((input(f"Digite a largura da parede {i}: ")).replace(",", "."))
    metragem_parede = altura_parede*largura_parede
    metragem_total = round((metragem_total + metragem_parede),2)

if cor_selecionada == "azul":
    valor_azul = round((custo_azul*metragem_total),2) 
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_azul} ")
elif cor_selecionada == "vermelho":
    valor_vermelho = round((custo_vermelho*metragem_total),2)
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_vermelho} ")
elif cor_selecionada == "magenta":
    valor_magenta = round((custo_magenta*metragem_total),2)
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_magenta} ")
else:
    valor_novacor = float((input("Não conheço o valor desta tinta. Informe o valor: ")).replace(",", "."))
    valor_tinta = round((valor_novacor * metragem_total),2)
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_tinta} ")
        
