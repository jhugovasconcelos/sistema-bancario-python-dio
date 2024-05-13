from cliente import Cliente
from historico import Historico

class Conta():
    
    def __init__(self, saldo: float, numero: int, agencia: str, cliente: Cliente, historico: Historico) -> None:
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico
        
    def saldo() -> float:
        pass
    
    @classmethod
    def nova_conta(cls, cliente:Cliente, numero:int):
        return cls()

    def sacar(valor:float) -> bool:
        #TODO: chamar a classe Saque
        pass

    def depositar(valor: float) -> bool:
        #TODO: chamar a classe Deposito
        pass

    #TODO: botar na classe Cliente?
    def nova_conta(cpf, numero_conta):
        account = {"Ag.": "0001", "C/C." : {numero_conta},  "CPF": {cpf}}
        LISTA_CONTAS.append(account)