bloco = int(input("Informe o bloco em que voce mora (1 a 4): "))

if bloco < 1 or bloco > 4:
    print("Bloco invalido. Digite um numero entre 1 e 4.")
elif bloco % 2 == 0:
    print(f"O bloco {bloco} e abastecido pela caixa A.")
else:
    print(f"O bloco {bloco} e abastecido pela caixa B.")
