def capicua(numero: int) -> int:
    numero = str(numero)

    if numero == numero[::-1]:
        return 1
    else:
        return 0


print(capicua(2002))
print(capicua(2024))
print(capicua(1221))