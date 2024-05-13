from abc import ABC, abstractmethod
from datetime import date

######### Aqui começam as classes de objetos #####

class Conta():
    AGENCIA = "0001"

    def __init__(self, cliente, numero) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = Conta.AGENCIA
        self._cliente = cliente
        self._historico = Historico()
        
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @property
    def numero(self) -> int:
        return self._numero
 
    @property
    def agencia(self) -> int:
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero): 
        """
        Classe Factory para criação de objetos do tipo Conta.
        """ 
        return cls(cliente, numero)
    
    def sacar(self, valor) -> bool:
        saldo = self._saldo
        if valor > saldo:
            print("Valor ultrapassa o saldo na conta!")
        else:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        return False

    def depositar(self, valor) -> bool:
        self._saldo += valor
        print("Depósito realizado com sucesso!")
        return True

class ContaCorrente(Conta):
       
    def __init__(self, numero, cliente) -> None:
        super().__init__(numero, cliente)
        self._limite = 500.0
        self._limite_saques = 3
        self._limite_conta = 250000.0

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    

    def sacar(self, valor) -> bool:
        limite = self._limite
        limite_saques = self._limite_saques
        historico = self._historico
        numero_saques = len([transacao for transacao in historico.transacoes if transacao["tipo"] == "Saque"])+1 # Esse acréscimo de 1 é para compensar o fato de que a função que adiciona a transação na lista só o faz após a verificação

        if valor > limite:
            print("Valor ultrapassa o limite!")
        elif numero_saques > limite_saques:
            print("Número de saques ultrapassou o limite diário!")
        else:
            return super().sacar(valor)
        return False
    

    def depositar(self, valor) -> bool:
        limite_conta = self._limite_conta
        saldo = self._saldo
        saldo_atualizado = saldo + valor
        if saldo_atualizado > limite_conta:
            print("Limite da conta ultrapassado!")
            return False
        return super().depositar(valor)

    def __str__(self) -> str:
        return f'\t\tAgência {self._agencia}\n\t\tC/C: {self._numero}\n\t\tTitular: {self._cliente.nome}\n{30*"*"}'
    
class Cliente():
    
    def __init__(self, endereco) -> None:
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas

    def realizar_transacao(self, conta, transacao):
        """
        Chama a função registrar() de transação, de acordo com o tipo
        """
        transacao.registrar(conta)

        
    def adicionar_conta(self, conta): 
        """
        Faz um append na lista de contas do cliente
        """
        self._contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, endereco, cpf, nome, data_nascimento) -> None:
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def datanasc(self):
        return self._data_nascimento

    @classmethod
    def criar_pessoa(cls, endereco, cpf, nome, datanasc):
        return cls(endereco=endereco, cpf=cpf, nome=nome, data_nascimento=datanasc)
    
    def __str__(self) -> str:
        return f'\t\tNome: {self._nome}\n\t\tCPF: {self._cpf}\n\t\tData Nascimento: {self._data_nascimento}\n{30*"*"}'
    
class Transacao(ABC):
    
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(conta):
        pass

class Saque(Transacao):

    def __init__(self, valor) -> None:
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):    
        conseguiu_sacar = conta.sacar(self._valor)
        if conseguiu_sacar:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):

    def __init__(self, valor:float) -> None:
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        conseguiu_depositar = conta.depositar(self._valor)
        if conseguiu_depositar:
            conta.historico.adicionar_transacao(self)

class Historico():
    
    def __init__(self) -> None:
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": date.today()
        })
        
###### Funções extras  ######

def opcao_nc(contas, clientes):
    print('>>>>>> Função Nova Conta')
    pergunta = input("Já é cliente do banco? [S/N] ")
    if pergunta.upper() == "S":
        cpf = input("Digite o CPF: ")
        existe_cliente = checar_cliente(cpf, clientes)
        if existe_cliente:
            numero = input('Digite o número: ')
            conta = ContaCorrente.nova_conta(cliente=existe_cliente, numero=numero)
            contas.append(conta)
        else: 
            escolha2 = input('Nome do cliente não encontrado, deseja cadastrar novo cliente? [S/N] ')
            if escolha2.upper() == 'S':
                opcao_nu()
            else: 
                print('Retornando ao menu anterior')
                return
    elif pergunta.upper() == 'N':
        escolha3 = input('Deseja cadastrar novo cliente? [S/N] ')
        if escolha3.upper() == 'S':
            opcao_nu()
        else:
            print('Retornando ao menu anterior')
            return
    else:
        print('Retornando ao menu anterior')
        return

def opcao_nu(clientes):
    print('>>>>>> Função Novo Usuário')
    cpf = input("Informe o CPF: ")
    cliente = cpf_validation(cpf, clientes)
    if cliente:
        nome = input("Digite o nome > ")
        datanasc = input("Digite a data de nascimento no formato dd-mm-aaaa> ")
        endereco = input("Digite o endereço> ")
        novo_cliente = PessoaFisica.criar_pessoa(endereco, cpf, nome.capitalize(), datanasc)
        clientes.append(novo_cliente)
        print("Usuário Adicionado")
    else:
        escolha = input("Deseja recomeçar[r] ou voltar ao menu anterior[v]? \n")
        if escolha.lower() == 'r':
            opcao_nu(clientes)
        elif escolha.lower() == 'v':
            return

def cpf_validation(cpf, clientes):
    existe_cpf = checar_cliente(cpf, clientes)
    cpf_de_acordo = cpf_cleaner(cpf)
    if cpf_de_acordo and not existe_cpf: 
        print("CPF validado com sucesso")
        return True
    elif not cpf_de_acordo:
        print("CPF não está de acordo")
        return False
    elif existe_cpf:
        print(f'O cliente {existe_cpf.nome} já existe')
        return False

def cpf_cleaner(cpf):
    if len(cpf) == 11 and isinstance(cpf, str):
        cpf.translate({ord(i): None for i in '.-'})
        return True
    elif len(cpf) == 11 and isinstance(cpf, int):
        str(cpf)
        cpf.translate({ord(i): None for i in '.-'})
        return True
    else:
        print('CPF incorreto')
        return False

def checar_cliente(cpf, clientes):
    """
    Função que checa se o cliente existe na lista de clientes pelo cpf fornecido
    """
    clientes_filtrados = [cliente for cliente in 
                          clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def checar_conta(numero, contas):
    """
    Função que checa se a conta existe na lista de contas pelo número fornecido
    """
    for conta in contas:
        if conta.numero == numero:
            return conta
        else:
            return None

def opcao_s():
    print('>>>>>> Função Saque')
    try:
        numero = input("Digite o número da conta ")
        existe_conta = checar_conta(numero, contas)
        if existe_conta: 
            valor = float(input('Digite o valor do saque > '))
            if valor > 0:
                transacao = Saque(valor)
                cliente = existe_conta.cliente
                cliente.realizar_transacao(conta=existe_conta, transacao=transacao)
            else:
                print("O valor é inválido")
    except ValueError:
        print("Por favor, digite um número")
      
def opcao_d(contas):
    print('>>>>>> Função Depósito')
    try:
        numero = input("Digite o número da conta ")
        existe_conta = checar_conta(numero, contas) 
        if existe_conta:
            try:
                valor = float(input('Digite o valor do depósito > '))
                if valor > 0:
                    # TODO: verificar se isso funciona! No do professor, ele pede primeiro o cliente e depois a conta; aqui, estou pedindo a conta 
                    # primeiro pra depois pegar o cliente a partir dela; 
                    transacao = Deposito(valor)
                    cliente = existe_conta.cliente
                    cliente.realizar_transacao(conta=existe_conta, transacao=transacao)
                else:
                    print("Por favor, digite um valor acima de zero")
            except ValueError:
                print("Por favor, digite um número")
        else:
            print("Conta não encontrada!")
    except ValueError:
        print("Digite um número!")

def opcao_e(contas):
    print('>>>>>> Função Extrato')
    numero_conta = input("Digite o número da conta: ")
    conta = checar_conta(numero_conta, contas)
    print('######## EXTRATO BANCO PYTHON ########')
    if conta:
        transacoes = conta.historico.transacoes
        for transacao in transacoes:
            print(f'Tipo: {transacao["tipo"]}\nValor: {transacao["valor"]}\nData: {transacao["data"]}\n{30*"*"}')
    else:
        print("Esta conta não existe")

####### Aqui começa a função main #######

if __name__ == '__main__':

   # listas de contas e clientes
    
    clientes = []
    contas = []
    
    # Logo do banco ao abrir o programa

    print('''
#  $$$$$$$\                                                $$$$$$$\              $$\     $$\                           
#  $$  __$$\                                               $$  __$$\             $$ |    $$ |                          
#  $$ |  $$ | $$$$$$\  $$$$$$$\   $$$$$$$\  $$$$$$\        $$ |  $$ |$$\   $$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$$$$$$\  
#  $$$$$$$\ | \____$$\ $$  __$$\ $$  _____|$$  __$$\       $$$$$$$  |$$ |  $$ |\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\ 
#  $$  __$$\  $$$$$$$ |$$ |  $$ |$$ /      $$ /  $$ |      $$  ____/ $$ |  $$ |  $$ |    $$ |  $$ |$$ /  $$ |$$ |  $$ |
#  $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |      $$ |  $$ |      $$ |      $$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |
#  $$$$$$$  |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ \$$$$$$  |      $$ |      \$$$$$$$ |  \$$$$  |$$ |  $$ |\$$$$$$  |$$ |  $$ |
#  \_______/  \_______|\__|  \__| \_______| \______/       \__|       \____$$ |   \____/ \__|  \__| \______/ \__|  \__|
#                                                                    $$\   $$ |                                        
#                                                                    \$$$$$$  |                                        
Digite uma das opções a seguir: 
[s] Saque
[d] Depósito
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta Bancária
[uc] Checar Usuário
[vu] Ver Usuários
[lc] Listar Contas
[q] Sair
''')
    # Laço principal do programa
    while True:
        option = input("****** Digite uma opção: \n")
        if option == 'q':
            print('Opção Sair')
            break
        elif option == 'nu':
            opcao_nu(clientes)
        elif option == 'nc':
            opcao_nc(contas, clientes)
            
        elif option == 'lc':
            print('>>>>>> Função Listar Contas')
            print('######## CONTAS CADASTRADAS BANCO PYTHON ########')
            for conta in contas:
                print(str(conta))
            
        elif option == 'vu':
            print('>>>>>> Função Ver Usuários')
            print('######## USUÁRIOS CADASTRADOS NO BANCO PYTHON ########')
            for cliente in clientes:
                print(str(cliente))

        elif option == 's':
            opcao_s()

        elif option == 'd':
            opcao_d(contas)

        elif option == 'e':
            opcao_e(contas)

        else:
            print('Por favor, selecione uma das opções abaixo')
            print("[s] Saque\n[d] Depósito\n[e] Extrato\n[nu] Novo Usuário\n[nc] Nova Conta Bancária\n[vu] Ver Usuários\n[lc] Listar Contas\n[q] Sair")
