nota1 = float(input("Informe a nota da primeira prova: "))
nota2 = float(input("Informe a nota da segunda prova: "))
nota3 = float(input("Informe a nota da terceira prova: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Media aritmetica: {media:.2f}")

if media >= 6:
    print("Aluno Aprovado.")
else:
    print("Aluno Reprovado.")
