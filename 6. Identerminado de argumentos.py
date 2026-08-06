def imprimir_dados(**dados):
    print(f"Nome: {dados['pnome']}")
    print(f"Sobrenome: {dados['psobrenome']}")
    print(f"Idade: {dados['pidade']}")


imprimir_dados(pnome="Ana", psobrenome="Silva", pidade=25)
