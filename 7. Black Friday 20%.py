def desconto_black_friday(preco: float) -> float:
    return preco * 0.80


precos = [2500.00, 180.00, 350.00, 1200.00, 89.90]

# Sem MAP
precos_com_desconto = []
for preco in precos:
    precos_com_desconto.append(desconto_black_friday(preco))

print(precos)
print(precos_com_desconto)

# Com MAP
precos_com_desconto_map = list(map(desconto_black_friday, precos))
print(precos_com_desconto_map)
