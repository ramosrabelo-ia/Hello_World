numero1 = float(input("Informe o primeiro numero: "))
numero2 = float(input("Informe o segundo numero: "))

if numero1 > numero2:
    print(f"O maior numero e {numero1}.")
elif numero2 > numero1:
    print(f"O maior numero e {numero2}.")
else:
    print("Numeros Iguais")
