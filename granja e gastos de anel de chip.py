quantidade_frangos = int(input("Digite a quantidade de frangos: "))

anel_chip = 0.40
aneis_alimento = 2 * 0.35

gasto_por_frango = anel_chip + aneis_alimento
gasto_total = quantidade_frangos * gasto_por_frango

print(f"O gasto total da granja é: R$ {gasto_total:.2f}".replace(".", ","))