entrada = input("Digite a media anual do aluno da FIAP: ")
entrada = entrada.replace("\ufeff", "").replace(chr(239) + chr(187) + chr(191), "")

try:
    media = float(entrada)
except ValueError:
    print("Nota invalida.")
else:
    if media < 0 or media > 10:
        print("Nota invalida.")
    elif media >= 6:
        print("Aluno aprovado.")
    elif media >= 4:
        print("Aluno de exame.")
    else:
        print("Aluno reprovado.")
