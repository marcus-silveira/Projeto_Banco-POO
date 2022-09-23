from datetime import date, datetime


def date_for_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_for_date(data: str) -> date or bool:
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def armazenar_dados(cliente: object):
    dados = open(f'dados_usuarios/{cliente.nome}.txt', 'w', encoding='utf-8')
    dados.write(f'{cliente.__str__()}')
    dados.close()


def tratar_nome(nome: str) -> str:
    nomes = []
    for i in nome.split():
        nomes.append(i.capitalize())
        nomes.append(' ')
    nome = ''
    nome = nome.join(nomes)
    return nome


def tratar_cpf(cpf: str) -> str:
    cpfs = []
    cpf = cpf.replace('.', '').replace('-', '')
    for i in cpf:
        cpfs.append(i)
    cpfs.insert(3, '.'), cpfs.insert(7, '.'), cpfs.insert(11, '-')
    cpf = ''
    cpf = cpf.join(cpfs)

    return cpf


def tratar_data(data: str, arg) -> date or str:
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return str(data)
    except ValueError:
        print('\nData de nascimento inválida!\n'
              'Use dia/mês/ano\n')
        return arg()


def confirmar_dados(conta: object):
    print(f'{conta}')
    resposta = input('\nAs informações estão corretas? S/N: ').upper()

    if resposta == 'S':
        return True
    elif resposta == 'N':
        print('\nTente novamente: ')
        return False
    else:
        print('Escolha S/N para prosseguir: \n')
        confirmar_dados(conta)
