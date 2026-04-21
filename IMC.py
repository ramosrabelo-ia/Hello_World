peso = float(input("Digite seu peso (ex: 58.00): "))
altura = float(input("Digite sua altura (ex: 1.63): "))

imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")