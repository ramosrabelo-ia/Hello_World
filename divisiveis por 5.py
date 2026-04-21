numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 <= numero2:
    inicio = numero1
    fim = numero2
else:
    inicio = numero2
    fim = numero1

print("Numeros divisiveis por 5:")

for numero in range(inicio, fim + 1):
    if numero % 5 == 0:
        print(numero)
