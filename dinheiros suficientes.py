valor_mercadoria = float(input("Informe o valor da mercadoria: R$ "))
valor_disponivel = float(input("Informe quanto dinheiro voce tem em maos: R$ "))

if valor_disponivel >= valor_mercadoria:
    print("O dinheiro e suficiente para adquirir a mercadoria.")
else:
    print("O dinheiro nao e suficiente para adquirir a mercadoria.")
