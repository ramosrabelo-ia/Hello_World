segundos = int(input("Digite o valor em segundos: "))

horas = segundos // 3600
resto = segundos % 3600
minutos = resto // 60
seg_restantes = resto % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", seg_restantes)
