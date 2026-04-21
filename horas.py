horas = int(input("Informe as horas: "))
minutos = int(input("Informe os minutos: "))

if 0 <= horas <= 23 and 0 <= minutos <= 59:
    print(f"Horario valido: {horas:02d}:{minutos:02d}")
else:
    print("Horario invalido.")
