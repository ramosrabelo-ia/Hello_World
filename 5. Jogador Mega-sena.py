import random


def mega_sena():
    nome = input("Digite o nome do jogador: ")
    idade = int(input("Digite a idade do jogador: "))

    numeros = random.sample(range(1, 61), 6)
    numeros.sort()

    print(f"Jogador: {nome}")
    print(f"Idade: {idade}")
    print(f"Numeros da Mega-Sena: {numeros}")


mega_sena()