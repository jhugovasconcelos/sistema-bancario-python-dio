"""
TODO: separar as opções de saque, depósito e extrato em funções.
TODO: criar 2 novas funções, de cadastrar usuário e cadastrar conta bancária.
Idea: a variável CONTA é um dicionário, você irá adicionar um usuário com chave "Usuário" e valor "Nome" toda vez que
for chamado o comando "u"; além disso, toda vez que as outras opções forem chamadas, elas entrarão abaixo dessa chave
e valor; Se for chamado outro, elas entrarão abaixo do outro, e assim por diante;
"""

print(''' ----------- Bem vindo ao Sistema Bancário!--------
 *************************************************
Digite uma das opções a seguir: 
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
[u] Cadastrar Usuário
[b] Cadastrar Conta Bancária
''')


def dep(deposit, SALDO, EXTRATO):
    if deposit >= 0:
        SALDO += deposit
        EXTRATO.append("Depósito: R$" + str(f'{deposit:.2f}'))
    else:
        print('Por favor, digite um valor positivo')
    return 0


def saq(wdrw, SALDO, COUNT, CONTA):
    if wdrw > SALDO:
        print('Saldo insuficiente, não foi possível realizar o saque')
    elif wdrw < 0:
        print('Por favor, digite um valor positivo')
    elif COUNT < 3:
        if wdrw <= 500:
            SALDO -= wdrw
            EXTRATO = list("Saque"+ str(f'{wdrw:.2f}'))
            CONTA |= EXTRATO
            COUNT += 1
        else:
            print('Limite de saque diário: R$ 500.00')
    else:
        print('Limite de saques diário atingido')


def ext(EXTRATO, CONTA):
    print('Opção Extrato')
    EXTRATO = list('Saldo Atual: R$' + str(f'{SALDO:.2f}'))
    CONTA |= EXTRATO
    print(CONTA)


def usu(new_user, COUNT, CONTA, SALDO):
    COUNT, SALDO = 0
    CONTA |= {"Usuário": new_user}


CONTA = {}
SALDO = 0
EXTRATO = []
COUNT = 0
while True:
    option = input('Opção >> ')
    if option == 'q':
        print('Opção Sair')
        break
    elif option == 'd':
        print('Opção Depósito')
        deposit = int(input('Digite o valor: '))
        dep(deposit, SALDO, EXTRATO)
    elif option == 's':
        print('Opção Saque')
        wdrw = int(input('Digite o valor: '))
        saq(wdrw, SALDO, COUNT, CONTA)
    elif option == 'e':
        ext(EXTRATO, CONTA)
    elif option == 'u':
        print('Opção Cadastrar Usuário')
        new_user = input('Digite o nome do Usuário: ')
        usu(new_user, COUNT, CONTA, SALDO)
    else:
        print('Opção inválida, por favor digite novamente')
