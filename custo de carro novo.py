custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

percentual_distribuidor = 0.28
percentual_impostos = 0.45

valor_distribuidor = custo_fabrica * percentual_distribuidor
valor_impostos = custo_fabrica * percentual_impostos

custo_consumidor = custo_fabrica + valor_distribuidor + valor_impostos

print(f"Custo de fábrica: R$ {custo_fabrica:.2f}")
print(f"Percentual do distribuidor (28%): R$ {valor_distribuidor:.2f}")
print(f"Impostos (45%): R$ {valor_impostos:.2f}")
print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")