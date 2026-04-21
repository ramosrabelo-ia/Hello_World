#estacionamento
#calcular valor
#limitar valor máximo
#ler horas valor = horas * 5
#SE valor > 35
#    valor = 35
#mostrar valor

horas = int(input("Quantas horas ficou? "))

valor = horas * 5

if valor > 35:
    valor = 35

print(f"Total a pagar: R$ {valor}")