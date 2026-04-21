bloco = int(input("Informe o bloco em que voce mora (1 a 20): "))

if bloco < 1 or bloco > 20:
    print("Bloco invalido. Digite um numero entre 1 e 20.")
elif bloco <= 10:
    print(f"O sindico responsavel pelo bloco {bloco} e o sr Jose.")
else:
    print(f"O sindico responsavel pelo bloco {bloco} e o sr Hamilton.")
