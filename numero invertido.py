numero = int(input("Informe um número com 3 dígitos: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10

invertido = unidade * 100 + dezena * 10 + centena

print("Número invertido:", invertido)