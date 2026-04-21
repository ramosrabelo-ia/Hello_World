nome = input("Nome do vendedor: ")
quantidade_carros = int(input("Quantidade de carros vendidos: "))
valor_vendas = float(input("Valor total das vendas: "))

salario_base = 2500
comissao_carros = quantidade_carros * 200
comissao_vendas = valor_vendas * 0.02

salario_final = salario_base + comissao_carros + comissao_vendas

print(f"O vendedor {nome} receberá um salário de R$ {salario_final}")