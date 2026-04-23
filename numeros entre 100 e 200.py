quantidade = 0

for contador in range(1, 11):
    numero = float(input(f"Digite o {contador}o numero: "))

    if numero >= 100 and numero <= 200:
        quantidade += 1

print(f"Foram digitados {quantidade} numeros entre 100 e 200.")
