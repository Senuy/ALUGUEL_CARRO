from CLASSES.Conta import Conta
from DB_CLIENTES.dbConta import ContaDb


import random



#cliente = []

while 1==1:
    opcao = int(input(''''
            Banco 24 horas estácio
            [1] - Cadastrar
            [2] - Mostrar Dados
            [3] - Depositar
            [4] - Sacar
            [5] - Sair
            Informe a função desejada: '''))
    if opcao == 0:
        break
    elif opcao == 1:
        num_conta = random.randint(1000,9999)
        nome = input('Digite nome do cliente: ')
        saldo = 0
        conta = Conta(num_conta, nome, saldo)
        conta.cadastrar()

        conta = ContaDb(num_conta, nome, saldo)
        conta.cadastro()

        #cliente.append(conta)
        print(f'número conta: {num_conta}')
    elif opcao == 2:
        numeroConta = int(input('Digite o número da Conta: '))
        for objeto in cliente:
            if(numeroConta == objeto.num_conta):
                dados = objeto.listarDados()
                print(dados)

    elif opcao == 3:
        numeroConta = int(input("Digite o número da Conta: "))
        valor = float(input("Digite o valor a ser depositado R$"))
        for objeto in cliente:
            if(numeroConta == objeto.num_conta):
                dados = objeto.depositar(valor)
                print(f'O valor depositado foi de R${valor}')


    elif opcao == 4:
        numeroConta = int(input("Digite o número da conta"))
        for objeto in cliente:
            if(valor <= objeto.saldo):
                dados = objeto.sacar(valor)
            else:
                print("Salso insuficiente")