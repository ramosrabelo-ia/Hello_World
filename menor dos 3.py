numero1 = float(input("Informe o primeiro numero: "))
numero2 = float(input("Informe o segundo numero: "))
numero3 = float(input("Informe o terceiro numero: "))

if numero1 == numero2 == numero3:
    print("Os numeros sao iguais.")
elif numero1 <= numero2 and numero1 <= numero3:
    print(f"O menor numero e {numero1}.")
elif numero2 <= numero1 and numero2 <= numero3:
    print(f"O menor numero e {numero2}.")
else:
    print(f"O menor numero e {numero3}.")
