from datetime import date, datetime


def date_for_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_for_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def format_float_str_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'
