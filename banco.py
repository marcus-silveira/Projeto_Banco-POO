from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta
from utils.helper import armazenar_dados, tratar_nome, tratar_cpf, confirmar_dados, tratar_data

contas: List[object] = []


def main() -> None:
    menu()


def menu() -> None:
    print('======================================')
    print('================ ATM =================')
    print('============== POA Bank ==============')
    print('======================================')

    print('Selecione uma opção no menu: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema')

    opcao = (input('\nDigite uma opção: \n'))

    if opcao.isnumeric() and 0 < int(opcao) < 7:
        opcao = int(opcao)

        if opcao == 1:
            criar_conta()
        elif opcao == 2:
            efetuar_saque()
        elif opcao == 3:
            efetuar_deposito()
        elif opcao == 4:
            efetuar_transferencia()
        elif opcao == 5:
            listar_contas()
        elif opcao == 6:
            print('Volte sempre!')
            sleep(2)
            exit()
    else:
        print('Opção inválida')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do Cliente: ')

    nome: str = input('Nome do cliente: ')
    nome = tratar_nome(nome)
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    cpf = tratar_cpf(cpf)
    data_nascimento: str = input('Data de nascimento: ')
    data_nascimento = tratar_data(data_nascimento, criar_conta)

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    if not confirmar_dados(cliente):
        criar_conta()
    else:

        contas.append(conta)
        armazenar_dados(cliente)

    print(f'\nConta criada com sucesso!\nDados da conta: \n--------------------------\n{conta}\n')
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do depósito: '))

            conta.depositar(valor)
        else:
            print(f'Conta {numero} não foi encontrada')
    else:
        print('Ainda não existem contas cadastradas.')
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem: int = int(input('Informe o número da sua conta: '))
        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino: int = int(input('Informe o número da conta de destino: '))
            conta_destino: Conta = buscar_conta_por_numero(numero_destino)

            if conta_destino:
                valor: float = float(input('Informe o valor da transferência: '))
                conta_origem.transferir(conta_destino, valor)
            else:
                print(f'Conta de destino {numero_origem} não foi encontrada')
        else:
            print(f'Conta {numero_origem} não foi encontrada')
    else:
        print('Ainda não há contas registradas')
    sleep(2)
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Contas: \n')
        for conta in contas:
            print(conta)
            print('---------------')
            sleep(1)
    else:
        print('Ainda não há contas cadastradas')
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    menu()
