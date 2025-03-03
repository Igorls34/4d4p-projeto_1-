from models import Conta, engine, Bancos, Status, Historico, Tipos
from sqlmodel import Session, select
from datetime import date, timedelta


def criar_conta(conta: Conta):
    """cria uma nova conta se não existir outra com o mesmo banco."""
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco == conta.banco)
        results = session.exec(statement).all()

        if results:
            print('Ja existe uma conta neste banco')
            return

        session.add(conta)
        session.commit()

        return conta


def listar_contas():
    """Retorna todas as contas cadastradas."""
    with Session(engine) as session:
        statement = select(Conta)
        results = session.exec(statement).all()
    return results

def desativar_conta(id):
    """Desativa uma conta se o saldo for 0"""
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id)
        conta = session.exec(statement).first()
        if conta.valor >0:
            raise ValueError('Essa conta ainda possui saldo.')
        conta.status = Status.INATIVO
        session.commit()

def transferir_saldo(id_conta_saida, id_conta_entrada, valor):
    """Realiza a transferencia de saldo entre duas contas."""
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id_conta_saida)
        conta_saida = session.exec(statement).first()
        if conta_saida.valor < valor:
            raise ValueError('saldo insuficiente')
        statement = select(Conta).where(Conta.id==id_conta_entrada)
        conta_entrada = session.exec(statement).first()

        conta_saida.valor -= valor
        conta_entrada.valor += valor
        session.commit()
        print('TRANSFERENCIA EFETUADA COM SUCESSO!!! :)')

def movimentar_dinheiro(historico : Historico):
    """movimenta o dinheiro entre duas contas, conforme o tipo de operação, CASO ELA ESTEJA ATIVA   """
    with Session(engine) as session:  
        statement = select(Conta).where(Conta.id == historico.conta_id)
        conta = session.exec(statement).first()
        if conta.status == Status.INATIVO:
              raise ValueError('Não é possivel efetuar a operação pois esta conta esta inativa')
        if historico.tipo == Tipos.ENTRADA:
            conta.valor += historico.valor
        else:
            if conta.valor < historico.valor:
                raise ValueError('saldo insuficiente')
            conta.valor -= historico.valor

        descricao = ""
        while not descricao.strip():
            descricao = input('defina uma descrição para esta operação: ')
            if not descricao:
                print('este campo não pode ficar vazio!!')
        historico.descricao = descricao

        session.add(historico)
        session.commit()
        return historico

def total_contas():
    with Session(engine) as session:
        statement = select(Conta)
        contas = session.exec(statement).all()
    
    total = 0
    for conta in contas:
        total += conta.valor
    
    return float(total)

def buscar_historico_entre_datas(data_inicio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Historico).where(
            Historico.data >= data_inicio,
            Historico.data <= data_fim
        )
        resultados = session.exec(statement).all()
        return resultados
    
def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status == Status.ATIVO)
        contas = session.exec(statement).all()
        bancos = [i.banco.value for i in contas]
        total =  [i.valor for i in contas]
        import matplotlib.pyplot as plt
        plt.bar(bancos,total)
        plt.show()

# criar_grafico_por_conta()
# x = buscar_historico_entre_datas(date.today() - timedelta(days=1), date.today() + timedelta(days=1))
# print(x)
# conta = Conta(valor=0, banco= Bancos.PICPAY)
# criar_conta(conta)
# desativar_conta(4)
# transferir_saldo(1,2,1)
# historico = Historico(conta_id=5, tipo=Tipos.SAIDA, valor=2000, data=date.today(), descricao="")
# movimentar_dinheiro(historico)
# print(total_contas())

# import matplotlib.pyplot as plt
# plt.bar(['NUBANK', 'SANTANDER'], [30, 50])
# plt.show()