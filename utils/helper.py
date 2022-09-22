from datetime import date, datetime
from models.cliente import *


def date_for_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_for_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'


def armazenar_dados(cliente: object):
    dados = open(f'dados_usuarios/{cliente.nome}.txt', 'w', encoding='utf-8')
    dados.write(f'{cliente.__str__()}')
    dados.close()
