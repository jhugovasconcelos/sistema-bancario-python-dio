# Requisitos para o Desafio

- A função saque deve receber os argumentos na forma **keyword only**; sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques; sugestão de retorno: saldo e extrato; 
- A função depósito deve receber os argumentos apenas por posição **positional only**; sugestão de argumentos: saldo, valor, extrato; sugestão de retorno: saldo e extrato
- A função extrato deve receber os argumentos por posição e nome **positional only e keyword only**; argumentos posicionais: saldo; argumentos nomeados: extrato;
- Criar usuário: o programa deve armazenar os usuários em uma **lista**, um usuário é composto por: 
    1. **nome**, 
    2. **data de nascimento**, 
    3. **cpf**, e 
    4. **endereço**. 
    - O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla do estado; 
    - Devem ser armazenados somente os números do CPF; 
    - Não podemos cadastrar 2 usuários com o mesmo CPF; 
- O programa deve armazenar contas em uma **lista**, uma conta é composta por:
    1. agência
    2. número da conta
    3. usuário
    - O número da conta é **sequencial**, iniciando em 1; 
    - O número da agência é fixo: "0001"
    - O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário
### *DICAS*
- Para vincular um usuário a uma conta, filtre a lista de usuários, buscando o número do CPF informado para cada usuário da lista. 
- Armazenar os dados completos de cada usuário em um dicionário, e apenas os CPFs em uma lista separada, para quando for filtrar; 
