# Lambda que retorna o oposto de um numero
oposto = lambda numero: numero * -1
print(oposto(10))

# Lambda que retorna o inverso de um numero
inverso = lambda numero: 1 / numero
print(inverso(5))

# Lambda que calcula a metade de um numero
metade = lambda numero: numero / 2
print(metade(20))

# Lambda que calcula a soma de quadrados de dois numeros
soma_quadrados = lambda numero1, numero2: numero1 ** 2 + numero2 ** 2
print(soma_quadrados(3, 4))

# Lambda que calcula o volume de uma esfera
volume_esfera = lambda raio: (4 / 3) * 3.14 * raio ** 3
print(volume_esfera(5))

# Lambda que imprime o nome e idade de uma pessoa
pessoa = lambda nome, idade: print(f"Nome: {nome}, Idade: {idade}")
pessoa("Ana", 25)

# Lambda que calcula a media da lista
listaOriginal = [234, 64, 13467, 45.89, 23]
media = lambda lista: sum(lista) / len(lista)
print(media(listaOriginal))

# Lambda que retorna True se o valor for par
eh_par = lambda numero: numero % 2 == 0
print(eh_par(10))

# Lambda que retorna o proprio valor se ele for par
retorna_par = lambda numero: numero if numero % 2 == 0 else None
print(retorna_par(10))
print(retorna_par(11))

# Lambda que calcula o modulo/absoluto de um numero
absoluto = lambda numero: numero * -1 if numero < 0 else numero
print(absoluto(-15))

# Lambda que retorna se a pessoa e maior de idade
maior_idade = lambda idade: idade >= 18
print(maior_idade(20))
print(maior_idade(15))
