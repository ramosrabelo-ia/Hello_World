votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_validos = int(input("Digite a quantidade de votos válidos: "))

total_votos = votos_brancos + votos_nulos + votos_validos

percentual_brancos = (votos_brancos / total_votos) * 100
percentual_nulos = (votos_nulos / total_votos) * 100
percentual_validos = (votos_validos / total_votos) * 100

print(f"Percentual de votos brancos: {percentual_brancos:.2f}%")
print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos válidos: {percentual_validos:.2f}%")