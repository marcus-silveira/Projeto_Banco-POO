from datetime import date, datetime


def date_for_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_for_date(data: str) -> date or bool:
    try:
        return datetime.strptime(data, '%d/%m/%Y')
    except AttributeError:
        return False
    except ValueError:
        return False


def format_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def armazenar_dados(cliente: object):
    dados = open(f'dados_usuarios/{cliente.nome}.txt', 'w', encoding='utf-8')
    dados.write(f'{cliente.__str__()}')
    dados.close()


def tratar_informacoes(nome: str, cpf: str) -> list[str]:
    nomes = []
    for i in nome.split():
        nomes.append(i.capitalize())
        nomes.append(' ')
    nome = ''
    nome = nome.join(nomes)

    cpfs = []
    cpf = cpf.replace('.', '').replace('-', '')
    for i in cpf:
        cpfs.append(i)
    cpfs.insert(3, '.'), cpfs.insert(7, '.'), cpfs.insert(11, '-')
    cpf = ''
    cpf = cpf.join(cpfs)

    return [nome, cpf]
