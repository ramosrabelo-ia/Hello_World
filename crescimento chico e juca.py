altura_chico = 1.50
altura_juca = 1.10
anos = 0

while altura_juca <= altura_chico:
    altura_chico += 0.02
    altura_juca += 0.05
    anos += 1

print(f"Serao necessarios {anos} anos para Juca ser mais alto que Chico.")
