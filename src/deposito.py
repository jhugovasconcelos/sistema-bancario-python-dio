from transacao import Transacao
from conta import Conta

class Deposito(Transacao):

    def __init__(self, valor:float) -> None:
        self._valor = valor
    
    def registrar(conta: Conta):
        return super().registrar()
    
    def deposito(valor):
    if valor >= 0:
        global SALDO; 
        SALDO += valor
        EXTRATO.append("Depósito: R$" + str(f'{valor:.2f}'))
        print(f'''Depósito efetuado com sucesso!
                 Saldo total: {SALDO}''')
    else:
        print('Por favor, digite um valor positivo')