salario_fixo = float(input("Informe o salario fixo: R$ "))
valor_vendas = float(input("Informe o valor total das vendas: R$ "))

if valor_vendas <= 1500:
    comissao = valor_vendas * 0.03
else:
    comissao = (1500 * 0.03) + ((valor_vendas - 1500) * 0.05)

salario_total = salario_fixo + comissao

print(f"Comissao: R$ {comissao:.2f}")
print(f"Salario total: R$ {salario_total:.2f}")
