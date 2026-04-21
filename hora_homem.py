dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

valor_por_dia = 80.00
valor_bruto = dias_trabalhados * valor_por_dia
desconto_ir = valor_bruto * 0.08
valor_liquido = valor_bruto - desconto_ir

print(f"Valor líquido a receber: R$ {valor_liquido:.2f}")