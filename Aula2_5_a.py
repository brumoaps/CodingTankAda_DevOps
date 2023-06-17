# Você quer pintar sua casa e está em dúvida entre as cores Azul, Vermelhor e Magenta. Sabendo que a tinta Azul custa 25,00 reais por metro quadrado, Vermelho custa 35 e Magenta custa 45, faça o seguinte:

# a) Crie um programa que recebe metros quadrados da sua parede e a cor da tinta e então retorne quanto gastará com tinta.

custo_azul = 25
custo_vermelho = 35
custo_magenta = 45

metragem = float((input("Informe a metragem das paredes a serem pintadas: ")).replace(",", "."))
cor_selecionada = input("Informe a cor desejada: ").lower()

if cor_selecionada == "azul":
    valor_azul = custo_azul*metragem 
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_azul} ")
elif cor_selecionada == "vermelho":
    valor_vermelho = custo_vermelho*metragem
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_vermelho} ")
elif cor_selecionada == "magenta":
    valor_magenta = custo_magenta*metragem
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_magenta} ")
else:
    valor_novacor = float(input("Não conheço o valor desta tinta. Informe o valor: "))
    valor_tinta = valor_novacor * metragem
    print(f"O custo total de tinta {cor_selecionada} será de R${valor_tinta} ")