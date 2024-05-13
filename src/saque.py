from transacao import Transacao
from conta import Conta

class Saque(Transacao):

    def __init__(self, valor:float) -> None:
        self._valor = valor

    def registrar(conta: Conta):
        return super().registrar()
    
    def saque(valor):
    global SALDO, NUMERO_SAQUES;
    if valor > SALDO:
        print('Saldo insuficiente, não foi possível realizar o saque')
    elif valor < 0:
        print('Por favor, digite um valor positivo')
    elif valor <= 500:
        SALDO -= valor
        EXTRATO.append("Saque: "+ str(f'{valor:.2f}'))
        NUMERO_SAQUES += 1
        print(f'''Saque efetuado com êxito!
                    Limite disponível: {SALDO}''')
    else:
        print('Limite de saque diário: R$ 500.00')