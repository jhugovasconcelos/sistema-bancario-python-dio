from datetime import date
from cliente import Cliente

class PessoaFisica(Cliente):
    
    def __init__(self, endereco: str, contas: list, cpf: str, nome: str, data_nascimento: date) -> None:
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def cleaner(self, cpf):
        if len(cpf) == 11:
            cpf.translate({ord(i): None for i in '.-'})
            return True
        else:
            print('CPF incorreto')
            return False
    
    def newcpf(self, cpf):
        #TODO: achar como definir os objetos já instanciados, talvez chamar o PessoaFisica.dict()?
        if cpf not in USERS_LIST:
            USERS_LIST.append(cpf)
            return True
        else:
            print("Usuário já cadastrado")
            return False
    
    def usercheck(self, cpf):
        if cpf in USERS_LIST:
            print("Usuário cadastrado")
            print(USERS_LIST)
        else:
            print('Usuário não cadastrado')
    
    def newuser(cpf, nome, datanasc, endereco):
        novo_usuario = {"Nome":nome, "cpf":cpf, "Data de Nascimento": datanasc, "Endereço": endereco}
        USERS_FULL.append(novo_usuario)
    
    # @classmethod
    # def add_user(cls):
    #     cpf = input("Digite o CPF \nou r para retornar ao menu anterior> ")
    #     if PessoaFisica.cleaner(cpf) and PessoaFisica.newcpf(cpf): 
    #         return
    #     nome = input("Digite o nome > ")
    #     datanasc = input("Digite a data de nascimento no formato dd-mm-aaaa> ")
    #     endereco = Cliente.endereco_input()
    #     PessoaFisica.newuser(cpf, nome, datanasc, endereco)
    #     return cls()