# Nome: Luana Ramos Rabelo
# Exercicio: Compra com Subtotal

preco_arroz = 22.90
preco_feijao = 7.50
preco_oleo = 6.80

qtd_arroz = int(input("Digite a quantidade de arroz: "))
qtd_feijao = int(input("Digite a quantidade de feijao: "))
qtd_oleo = int(input("Digite a quantidade de oleo: "))

total_arroz = qtd_arroz * preco_arroz
total_feijao = qtd_feijao * preco_feijao
total_oleo = qtd_oleo * preco_oleo

total_geral = total_arroz + total_feijao + total_oleo

print("Total com arroz: R$", total_arroz)
print("Total com feijao: R$", total_feijao)
print("Total com oleo: R$", total_oleo)
print("Total geral da compra: R$", total_geral)