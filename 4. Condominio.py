# Cadastro dos workshops
workshops = []

quantidade_workshops = int(input('Quantos workshops deseja cadastrar? '))

for contador in range(quantidade_workshops):
    dia = input('Digite o dia da semana do workshop: ')
    horario = input('Digite o horario do workshop: ')

    workshop = {
        'dia': dia,
        'horario': horario
    }

    workshops.append(workshop)

print(workshops)


# Cadastro de voluntarios

def cadastrar_voluntario():
    try:
        nome = input('Digite o nome do voluntario: ')
        if nome == '':
            raise ValueError('O nome nao pode estar vazio')

        idade = input('Digite a idade do voluntario: ')

        try:
            idade = int(idade)
        except ValueError:
            try:
                float(idade)
                raise ValueError('A idade nao pode ser float')
            except ValueError as erro:
                if str(erro) == 'A idade nao pode ser float':
                    raise erro
                raise ValueError('A idade precisa ser um numero inteiro')

        if idade <= 0:
            raise ValueError('A idade precisa ser maior que zero')

        periodo = input('Digite o periodo disponivel (manha, tarde, noite): ')
        if periodo == '':
            periodo = 'tarde'

        return {
            'nome': nome,
            'idade': idade,
            'periodo': periodo
        }

    except ValueError as erro:
        print(f'Erro: {erro}')
        return None


voluntarios = []
voluntario = cadastrar_voluntario()

if voluntario is not None:
    voluntarios.append(voluntario)

print(voluntarios)


# Lambda que calcula a quantidade de lixo gerada por dia
calcular_lixo = lambda pessoas: {
    'kg_minimo': pessoas * 0.8,
    'kg_maximo': pessoas * 1,
    'litros_minimo': pessoas * 4,
    'litros_maximo': pessoas * 6
}

quantidade_pessoas = int(input('Digite a quantidade de pessoas do condominio: '))
print(calcular_lixo(quantidade_pessoas))


# Lambda que informa a cor correta do recipiente
cor_recipiente = lambda item: 'azul' if item == 'papel' else \
    'vermelho' if item == 'plastico' else \
    'verde' if item == 'vidro' else \
    'amarelo' if item == 'metal' else \
    'preto' if item == 'madeira' else \
    'marrom' if item == 'organico' else \
    'branco' if item == 'hospitalar' else 'tipo nao encontrado'

produtos_lixo = [
    'papel', 'organico', 'metal', 'metal', 'metal', 'madeira',
    'vidro', 'papel', 'papel', 'vidro', 'organico', 'hospitalar',
    'plastico', 'plastico', 'madeira'
]

cores_recipientes = list(map(cor_recipiente, produtos_lixo))
print(cores_recipientes)
