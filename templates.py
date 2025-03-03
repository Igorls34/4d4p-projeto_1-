from models import *
from views import *
from datetime import date, timedelta, datetime

class UI:
    def start(self):
        while True:
            print('''
            [1] -> Criar Conta
            [2] -> Desativar Conta
            [3] -> Transferir Dinheiro
            [4] -> Movimentar Dinheiro
            [5] -> Total Contas
            [6] -> Filtrar Historico
            [7] -> Gráfico
                ''')
            
            choice = int(input("Escolha uma opção: "))

            if choice == 1:
                self._criar_conta()
            elif choice == 2:
                self._desativar_conta()
            elif choice == 3:
                self._transferir_saldo()
            elif choice == 4:
                self._movimentar_dinheiro()
            elif choice == 5:
                self._total_contas()
            elif choice == 6:
                self._filtrar_movimentacoes()
            elif choice == 7:
                self._criar_grafico()
            else:
                break

    def _criar_conta(self):
        print('digite o nome de algum dos bancos abaixo: ')

        for banco in Bancos:
            print(f'---{banco.value}---')

        banco = input().title()
        valor = float(input('Digite o valor atual em sua conta: '))

        conta = Conta(banco=Bancos(banco), valor=valor)
        criar_conta(conta)
    
    def _desativar_conta(self):
        print('Escolha o ID da conta que deseja desativar: ')

        listar_contas()

        for i in listar_contas():
            print(f'--- ID: {i.id} | Banco: {i.banco.value} | Saldo: {i.valor} | Status: {i.status.value}---')

        id_conta = int(input())

        try:
            desativar_conta(id_conta)
            print('conta desativada com sucesso')
        except ValueError:
            print('Essa conta ainda possui saldo! Por favor, realize uma transferencia e tente novamente')
            
    def _transferir_saldo(self):
        listar_contas()
        for i in listar_contas():
            print(f'--- ID: {i.id} | Banco: {i.banco.value} | Saldo: {i.valor} | Status: {i.status.value}---')    
        conta_saida = input('defina uma conta de saida: ')
        
        listar_contas()
        for i in listar_contas():
            print(f'--- ID: {i.id} | Banco: {i.banco.value} | Saldo: {i.valor} | Status: {i.status.value}---')
        conta_entrada = input('defina uma conta de entrada: ')
        
        if conta_entrada == conta_saida:
            print('a conta de entrada e de saida precisam ser duas contas diferentes...')

        valor = int(input('defina o valor da transferencia: '))
        if valor <= 0:
            raise ValueError('Valor invalido, tente novamente')
        
        transferir_saldo(conta_saida,conta_entrada,valor)

    def _movimentar_dinheiro(self):
        print('Escolha a conta:')
        for i in listar_contas():
            print(f'{i.id}  -> {i.banco} -> R${i.valor}')

        conta_id = int(input())

        valor = float(input('digite o valor movimentação: '))

        print('selecionte o tipo de movimentação')
        for tipo in Tipos:
            print(f'---{tipo.value}---')
        
        tipo = input().title()
        historico = Historico(conta_id=conta_id, tipo=Tipos(tipo), valor=valor, data=date.today())
        movimentar_dinheiro(historico)
    
    def _total_contas(self):
        print(f'R${total_contas()}')

    def _filtrar_movimentacoes(self):
        data_inicio = input('Digite uma data de inicio: ')
        data_fim = input('digite uma data final: ')

        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()

        for i in buscar_historico_entre_datas(data_inicio, data_fim):
            print(f'{i.valor} - {i.tipo.value}')
    
    def _criar_grafico(self):
        criar_grafico_por_conta()

UI().start()