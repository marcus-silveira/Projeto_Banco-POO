from datetime import date
from utils.helper import date_for_str, str_for_date


class Cliente:
    contador: int = 101

    def __init__(self, nome: str, email: str, cpf: str, data_nascimento: str):
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_for_date(data_nascimento)
        self.__data_cadastro: date = date.today()

        Cliente.contador += 1

    def __str__(self: object) -> str:
        return f'\nCódigo: {self.codigo}\nNome: {self.nome}' \
               f'\nCPF: {self.cpf}' \
               f'\nData de Nascimento: {self.data_nascimento}' \
               f'\nCadastro: {self.data_cadastro}\nE-mail: {self.email}'

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return date_for_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return date_for_str(self.__data_cadastro)
