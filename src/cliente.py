from conta import Conta
from transacao import Transacao

class Cliente():
    
    def __init__(self, endereco: str, contas: list) -> None:
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass
    
    def adicionar_conta(conta: Conta):
        pass

    
    # def endereco_input(self):
    #     logradouro = input("Digite o logradouro > ")
    #     numero = input("Digite o número > ")
    #     bairro = input("Digite o bairro > ")
    #     cidade = input("Digite a cidade > ")
    #     estado = input("Digite o estado no formato EE > ")
    #     endereco = logradouro + ',' + numero + '-' + bairro + '-' + cidade + '/' + estado.upper()
    #     if len(endereco) <= 256:
    #         self._endereco = endereco
    #         print("Endereço salvo!")
    #     else:
    #         print("Tamanho máximo ultrapassado! Favor reescrever o endereço")
    #         Cliente.endereco_input()