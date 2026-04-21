# Nome: Luana Ramos Rabelo
# RM: 570351
# Exercicio: 02 - Compra

# preços fixos
preco_arroz = 22.90
preco_feijao = 7.50
preco_oleo = 6.80

# entrada de dados
qtd_arroz = int(input("Digite a quantidade de arroz: "))
qtd_feijao = int(input("Digite a quantidade de feijão: "))
qtd_oleo = int(input("Digite a quantidade de óleo: "))

# calculos
total_arroz = qtd_arroz * preco_arroz
total_feijao = qtd_feijao * preco_feijao
total_oleo = qtd_oleo * preco_oleo

total_geral = total_arroz + total_feijao + total_oleo

# saida
print("Total com arroz: R$", total_arroz)
print("Total com feijão: R$", total_feijao)
print("Total com óleo: R$", total_oleo)
print("Total da compra: R$", total_geral)