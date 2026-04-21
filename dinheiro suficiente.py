#dinheiro suficiente
#compara valores
#ler valor_produto
#ler dinheiro
#SE dinheiro >= valor_produto    mostrar "Suficiente"
#SENAO                           mostrar "Insuficiente"

produto = float(input("Digite o valor do produto: "))
dinheiro = float(input("Quanto você tem? "))

if dinheiro >= produto:
    print("Dinheiro suficiente")
else:
    print("Dinheiro insuficiente")
