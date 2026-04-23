soma_impares = 0

for contador in range(1, 16):
    numero = int(input(f"Digite o {contador}o numero: "))

    if numero % 2 != 0:
        soma_impares += numero

print(f"O somatorio dos numeros impares digitados e {soma_impares}.")
