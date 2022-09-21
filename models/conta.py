from models.cliente import Cliente
from utils.helper import format_float_str_moeda


class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100
        self.__saldo_total: float = self._calcula_saldo_total

        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero}\nCliente: {self.cliente.nome}\n' \
               f'Saldo: {self.saldo}\nLimite: {self.limite}'

    def extrato(self: object) -> None:
        return print(Conta.__str__(self))

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.saldo_total = self._calcula_saldo_total
            print('Depósito efetuado com sucesso!\n')
            self.extrato()
        else:
            print('Somente valores acima de R$ 0,00 são permitidos.')

    def sacar(self: object, valor: float) -> None:
        if 0 < valor <= self.saldo_total:
            if valor < self.saldo:
                self.saldo -= valor
                print('Saque realizado com sucesso')
                self.saldo_total = self._calcula_saldo_total
                self.extrato()
            else:
                saldo_negativo: float = self.saldo - valor
                self.limite += saldo_negativo
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                print('Saque realizado com sucesso')
                self.extrato()
        elif valor == 0:
            print('Não foi possível realizar o saque. Tente novamente')
        else:
            print('Saldo insuficiente')

    def transferir(self: object, destino: object, valor: float):
        if 0 < valor <= self.saldo_total:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = destino._calcula_saldo_total
                print('Transferência realizada com sucesso')
                self.extrato()
            else:
                saldo_negativo: float = self.saldo - valor
                self.limite += saldo_negativo
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
                destino.saldo += valor
                destino.saldo_total = destino._calcula_saldo_total
                print('Transferência realizada com sucesso')
                self.extrato()
        else:
            print('Transferência não realizada')

