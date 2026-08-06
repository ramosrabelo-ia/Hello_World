listaOriginal = [234, 64, 13467, 45.89, 23]
listaDescontos = [0.3, 0.004, 0.5, 0.03, 0.8]

precos_finais = []

for preco, desconto in zip(listaOriginal, listaDescontos):
    preco_final = preco - (preco * desconto)
    precos_finais.append(preco_final)

print(listaOriginal)
print(listaDescontos)
print(precos_finais)
