# Nome: Luana Ramos Rabelo
# Exercicio: Calculo de Azulejos

print("Informe todas as medidas em METROS.")
print("Exemplo de azulejo: 0.30 representa 30 centimetros.")

comprimento = float(input("Digite o comprimento do banheiro (m): "))
largura = float(input("Digite a largura do banheiro (m): "))
altura = float(input("Digite a altura das paredes (m): "))

largura_azulejo = float(input("Digite a largura do azulejo (m): "))
altura_azulejo = float(input("Digite a altura do azulejo (m): "))

area_parede1 = comprimento * altura
area_parede2 = largura * altura

area_total = (2 * area_parede1) + (2 * area_parede2)

area_azulejo = largura_azulejo * altura_azulejo

quantidade_azulejos = area_total / area_azulejo

azulejos = int(quantidade_azulejos)

if quantidade_azulejos > azulejos:
    azulejos = azulejos + 1

caixas = azulejos // 10

if azulejos % 10 != 0:
    caixas = caixas + 1

print("Area total das paredes:", area_total, "m2")
print("Area de um azulejo:", area_azulejo, "m2")
print("Quantidade total de azulejos necessaria:", azulejos)
print("Quantidade aproximada de caixas:", caixas)