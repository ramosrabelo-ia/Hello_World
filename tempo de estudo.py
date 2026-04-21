# Nome: Luana Ramos Rabelo
# RM: 570351
# Exercicio: estudo

# entrada de dados
domingo = float(input("Horas estudadas no domingo: "))
segunda = float(input("Horas estudadas na segunda-feira: "))
terca = float(input("Horas estudadas na terça-feira: "))
quarta = float(input("Horas estudadas na quarta-feira: "))
quinta = float(input("Horas estudadas na quinta-feira: "))
sexta = float(input("Horas estudadas na sexta-feira: "))
sabado = float(input("Horas estudadas no sábado: "))

# total semanal
total_semana = domingo + segunda + terca + quarta + quinta + sexta + sabado

# cálculos
media_dia = total_semana / 7
total_mes = total_semana * 4
total_ano = total_semana * 52
total_minutos = total_semana * 60

# saída
print("Total de horas na semana:", total_semana)
print("Média de horas por dia:", media_dia)
print("Total de horas no mês:", total_mes)
print("Total de horas no ano:", total_ano)
print("Total semanal em minutos:", total_minutos)