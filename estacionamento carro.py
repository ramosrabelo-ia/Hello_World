horas = float(input("Informe o periodo de permanencia em horas: "))

total_pagar = horas * 5

if total_pagar > 35:
    total_pagar = 35

print(f"Total a pagar: R$ {total_pagar:.2f}")
