precos = [2500.00, 180.00, 350.00, 1200.00, 89.90]

# Funcao lambda com 20% de desconto
desconto_black_friday = lambda preco: preco * 0.80
precos_com_desconto = list(map(desconto_black_friday, precos))
print(precos_com_desconto)

# Lambda diretamente dentro do MAP
precos_com_desconto_map = list(map(lambda preco: preco * 0.80, precos))
print(precos_com_desconto_map)
