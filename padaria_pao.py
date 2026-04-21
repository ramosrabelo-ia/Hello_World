quantidade_paes = int(input("Digite a quantidade de pães vendidos: "))
quantidade_broas = int(input("Digite a quantidade de broas vendidas: "))

valor_paes = quantidade_paes * 0.38
valor_broas = quantidade_broas * 4.50

total_arrecadado = valor_paes + valor_broas
valor_poupanca = total_arrecadado * 0.10

print(f"Total arrecadado: R$ {total_arrecadado:.2f}")
print(f"Valor a guardar na poupança: R$ {valor_poupanca:.2f}")