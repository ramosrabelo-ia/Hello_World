def perfeito(numero: int) -> int:
    soma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor

    if soma == numero:
        return 1
    else:
        return 0


print(perfeito(6))
print(perfeito(10))
print(perfeito(28))