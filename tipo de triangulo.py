lado1 = float(input("Informe o primeiro lado do triangulo: "))
lado2 = float(input("Informe o segundo lado do triangulo: "))
lado3 = float(input("Informe o terceiro lado do triangulo: "))

if lado1 == lado2 == lado3:
    print("O triangulo e equilatero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triangulo e isosceles.")
else:
    print("O triangulo e escaleno.")
