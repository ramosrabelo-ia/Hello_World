valor_total = 780000.00

primeiro_ganhador = valor_total * 0.46
segundo_ganhador = valor_total * 0.32
terceiro_ganhador = valor_total - primeiro_ganhador - segundo_ganhador

print(f"Primeiro ganhador receberá: R$ {primeiro_ganhador:.2f}")
print(f"Segundo ganhador receberá: R$ {segundo_ganhador:.2f}")
print(f"Terceiro ganhador receberá: R$ {terceiro_ganhador:.2f}")