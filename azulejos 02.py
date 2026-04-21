comprimento = float(input("Digite o comprimento da cozinha em metros: "))
largura = float(input("Digite a largura da cozinha em metros: "))
altura = float(input("Digite a altura da cozinha em metros: "))

area_parede_maior = comprimento * altura
area_parede_menor = largura * altura

area_total_paredes = (2 * area_parede_maior) + (2 * area_parede_menor)

area_por_caixa = 1.5
quantidade_caixas = area_total_paredes / area_por_caixa

print(f"Área total das paredes: {area_total_paredes:.2f} m²")
print(f"Quantidade de caixas de azulejo: {quantidade_caixas:.2f}")