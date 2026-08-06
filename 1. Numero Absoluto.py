def absoluto(numero:int) -> int:
    """
    Funcao que calcula o numero absoluto.
    :param numero: numero inteiro
    :return: numero absoluto
    """
    if numero < 0:
        return numero * -1
    else:
        return numero


print(absoluto(-10))
print(absoluto(10))
