print(''' ----------- Bem vindo ao Sistema Bancário!--------
 *************************************************
Digite uma das opções a seguir: 
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
''')

saldo = 0
extrato = []
count = 0
while True: 
    option = input('Opção >> ')
    if option == 'q':
        print('Opção Sair')
        break
    elif option == 'd':
        print('Opção Depósito')
        deposit = int(input('Digite o valor: '))
        if deposit >= 0:
            saldo += deposit
            extrato.append("Depósito: R$" + str(f'{deposit:.2f}'))
        else:
            print('Por favor, digite um valor positivo')
    elif option == 's':
        print('Opção Saque')
        wdrw = int(input('Digite o valor: '))
        if wdrw > saldo:
            print('Saldo insuficiente, não foi possível realizar o saque')
        elif wdrw < 0:
            print('Por favor, digite um valor positivo')
        elif count < 3:
            if wdrw <= 500:
                saldo -= wdrw
                extrato.append('Saque: R$ ' + str(f'{wdrw:.2f}'))
                count += 1
            else: 
                print('Limite de saque diário: R$ 500.00')
        else:
            print('Limite de saques diário atingido')
    elif option == 'e':
        print('Opção Extrato')
        extrato.append('Saldo Atual: R$' + str(f'{saldo:.2f}'))
        print(extrato)
    else:
        print('Opção inválida, por favor digite novamente')