def dobro(num:int) -> int:
    """
    funcao que calcula o dobro de um numero
    :param num: numero inteiro
    :return: o dobro do numero
    """
    return num * 2

print(dobro(5))
print(dobro(9.3))
help(dobro)

#type hint - boa pratica para assinatura de funcoes
#indica o tipo de dado esperado, mas nao impede o uso com outros tipos de dados
#type hint nao é muito utilizado para declaracao de variaveis simples, mas é muito
#usado com funcoes
nom = 'Daniela'
#com type hint
nome:str = 'Patricia'
print(nome)
nome = 23
print(nome)

#docstring para documentacao de funcoes
#para uso no help

#Lambda é uma pequena funcao para uso imediato
#Voce atribuir a lambda criada para uma variavel se vc for usar algumas vezes
#em lugares proximos na hora de codar
print('\nLambda')
ldobro = lambda num:num*2
print(ldobro(7))

print((lambda num:round(num/2,2))(9))
print((lambda num:round(num/2,2))(76))

#lambda condicional é o lambda com o if interno
def aumento_salario(salario:float) -> float:
    if salario > 15000:
        return salario * 1.07
    elif salario > 10000:
        return salario * 1.10
    else:
        return salario * 1.15
print(f'Meu salario reajustado R${aumento_salario(10000):.2f}')

lreajuste_salarial = lambda salario:salario*1.07 if salario > 15000 else salario*1.15
print(f'Meu salario reajustado R${lreajuste_salarial(10000):.2f}')
print(f'Meu salario reajustado R${(lambda salario: 
                                   round(salario*1.07, 2) if salario > 15000 else 
                                   (round(salario*1.10, 2) 
                         if salario > 10000 else round(salario*1.15, 2)))(9000):.2f}')

#lambda e map sao um bom casamento
#o map aplica uma funcao em todos os elementos de uma lista

def quintuplo(num:int) -> int:
    """
    Funcao que calcula o quintuplo de um numero
    :param num: numero inteiro
    :return: o quintuplo do numero
    """
    return num * 5

print(f'Quintuplo:{quintuplo(3)}')
variosnumeros = [5, 4, 78, -9]

#exercicio: transforma a funcao triplo em quintuplo ja usando lambda
# e aplica o map ja tudo direto no print

print(list(map(lambda num: num * 5, variosnumeros)))

listanum = [5,4,78,-9]
lquintoplo = lambda num: num*5

lquintuplos2 =  list(map(quintuplo, listanum))
print(lquintuplos2)
