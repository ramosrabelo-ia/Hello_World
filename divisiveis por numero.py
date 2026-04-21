divisor = int(input("Digite um numero divisor: "))

if divisor == 0:
    print("Nao e possivel dividir por zero.")
else:
    print("Numeros divisiveis por", divisor)

    for numero in range(0, 101):
        if numero % divisor == 0:
            print(numero)
