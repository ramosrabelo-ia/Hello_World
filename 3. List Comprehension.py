# Remova os espacos da lista
lOriginal = [' vermelho', ' verde', 'azul ', ' amarelo ']
sem_espacos = [cor.strip() for cor in lOriginal]
print(sem_espacos)

# Acrescente um \n em cada item da lista
lOriginal = ['vermelho', 'verde', 'azul', 'amarelo']
com_quebra_linha = [cor + '\n' for cor in lOriginal]
print(com_quebra_linha)

# Calcule a metade dos numeros
lNumeros = [10, 20, 30, 40, 50]
metades = [numero / 2 for numero in lNumeros]
print(metades)

# Exclua os negativos da lista
lNumeros = [-4, -2, 0, 2, 4]
sem_negativos = [numero for numero in lNumeros if numero >= 0]
print(sem_negativos)

# Exclua as letras da lista
lMix = [-4, 'v', 'X', 'cacto', -2, 0, 'y', 2, 4]
sem_letras = [item for item in lMix if type(item) == int or type(item) == float]
print(sem_letras)

# Quadrados de numeros de 1 a 10
quadrados = {numero: numero ** 2 for numero in range(1, 11)}
print(quadrados)

# Filtre os pares
pares = {numero: numero ** 2 for numero in range(1, 11) if numero % 2 == 0}
print(pares)

# De 1 a 10 informe qual e par, qual e impar
par_ou_impar = {numero: 'par' if numero % 2 == 0 else 'impar' for numero in range(1, 11)}
print(par_ou_impar)

# A partir da lista, calcule qual o tamanho de cada palavra
palavras = ['gato', 'elefante', 'cachorro']
tamanho_palavras = {palavra: len(palavra) for palavra in palavras}
print(tamanho_palavras)

# Conte quantas vezes aparece cada letra em uma palavra
palavra = 'banana'
contagem_letras = {letra: palavra.count(letra) for letra in palavra}
print(contagem_letras)

# Inverta chave com valor
alunos = {'Ana': 10, 'Bruno': 8, 'Carla': 9}
notas_alunos = {nota: nome for nome, nota in alunos.items()}
print(notas_alunos)

# Limpe os espacos em branco
dados = {' Nome ': ' Ana ', ' Idade ': ' 20 '}
dados_limpos = {chave.strip(): valor.strip() for chave, valor in dados.items()}
print(dados_limpos)

# Use o enumerate para criar dicionarios
nomes = ['Alice', 'Bob', 'Carlos']
dicionario_nomes = {indice: nome for indice, nome in enumerate(nomes)}
print(dicionario_nomes)
