EXTRATO = []
USERS_LIST = []
USERS_FULL = []
LISTA_CONTAS = []
SALDO = 0
NUMERO_SAQUES = 0

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


class verify:
    def cleaner(cpf):
        if len(cpf) == 11:
            cpf.translate({ord(i): None for i in '.-'})
            return True
        else:
            print('CPF incorreto')
            return False
    def newcpf(cpf):
        if cpf not in USERS_LIST:
            USERS_LIST.append(cpf)
            return True
        else:
            print("Usuário já cadastrado")
            return False
    def usercheck(cpf):
        if cpf in USERS_LIST:
            print("Usuário cadastrado")
            print(USERS_LIST)
        else:
            print('Usuário não cadastrado')

        

def deposito(valor):
    if valor >= 0:
        global SALDO; 
        SALDO += valor
        EXTRATO.append("Depósito: R$" + str(f'{valor:.2f}'))
        print(f'''Depósito efetuado com sucesso!
                 Saldo total: {SALDO}''')
    else:
        print('Por favor, digite um valor positivo')


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



def newuser(cpf, nome, datanasc, endereco):
    novo_usuario = {"Nome":nome, "cpf":cpf, "Data de Nascimento": datanasc, "Endereço": endereco}
    USERS_FULL.append(novo_usuario)


def nova_conta(cpf, numero_conta):
    account = {"Ag.": "0001", "C/C." : {numero_conta},  "CPF": {cpf}}
    LISTA_CONTAS.append(account)



def address():
    logradouro = input("Digite o logradouro > ")
    numero = input("Digite o número > ")
    bairro = input("Digite o bairro > ")
    cidade = input("Digite a cidade > ")
    estado = input("Digite o estado no formato EE > ")
    endereco = logradouro + ',' + numero + '-' + bairro + '-' + cidade + '/' + estado
    if len(endereco) <= 256:
        return endereco
    else:
        print("Tamanho máximo ultrapassado! Favor reescrever o endereço")
        address()


def extrato():
    print('>>>>>> Função Extrato')
    EXTRATO.append('Saldo Atual: R$' + str(f'{SALDO:.2f}'))
    print('######## EXTRATO BANCO PYTHON ########')
    for saldo in EXTRATO:
        print(saldo)
        print('----------------------------------------')


if __name__ == '__main__':
    numero_conta = 0
    while True:
        option = input('Opção (Digite "o" para ver as opções)>> ')
        if option == 'o':
            print('''
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
            pass
        elif option == 'q':
            print('Opção Sair')
            break
        elif option == 'nu':
            print('>>>>>> Função Novo Usuário')
            while True:
                cpf = input("Digite o CPF> ")
                if verify.cleaner(cpf) and verify.newcpf(cpf): 
                    break
            nome = input("Digite o nome > ")
            datanasc = input("Digite a data de nascimento no formato dd-mm-aaaa> ")
            endereco = address()
            newuser(cpf, nome, datanasc, endereco)
        elif option == 'uc':
            print('>>>>>> Função Checar Usuário')
            while True:
                cpf = input("Digite o CPF> ")
                if verify.cleaner(cpf): 
                    break
            verify.usercheck(cpf)
        elif option == 'nc':
            numero_conta += 1
            print('>>>>>> Função Nova Conta')
            while True:
                cpf = input("Digite o CPF> ")
                if verify.cleaner(cpf): 
                    break
            nova_conta(cpf, numero_conta)
        elif option == 'lc':
            print('>>>>>> Função Listar Contas')
            print('######## CONTAS CADASTRADAS BANCO PYTHON ########')
            for conta in LISTA_CONTAS:
                print(conta)
            print('----------------------------------------')
        elif option == 'vu':
            print('>>>>>> Função Ver Usuários')
            print('######## USUÁRIOS CADASTRADOS NO BANCO PYTHON ########')
            for user in USERS_FULL:
                print(user)
            print('----------------------------------------')
        elif option == 's':
            if NUMERO_SAQUES < 3:
                print('>>>>>> Função Saque')
                try:
                    value = float(input('Valor do saque > '))
                    saque(valor=value)
                except ValueError:
                    print('Por favor, digite um número')
            else:
                print('Limite de saques diário atingido!')
        elif option == 'd':
            print('>>>>>> Função Depósito')
            try:
                valor = float(input('Digite o valor do depósito > '))
                deposito(valor)
            except ValueError:
                print("Por favor, digite um número")
        elif option == 'e':
            extrato()
        else:
            print('Opção inválida, por favor digite novamente')
