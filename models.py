from sqlmodel import SQLModel, Field, create_engine, Relationship # type: ignore
from enum import Enum
from datetime import date

class Bancos(Enum):
    """Enumeração para os Bancos disponiveis."""
    NUBANK = 'Nubank'
    SANTANDER = 'Santander'
    INTER = 'Inter'
    PICPAY = 'PicPay'
    CAIXA = 'Caixa'

class Status(Enum):
    """Enumeração para os status da conta."""
    ATIVO = 'Ativo'
    INATIVO= 'Inativo'

class Tipos(Enum):
    """Enumeração para os tipos de movimentação(entrada, saida)"""
    ENTRADA = 'Entrada'
    SAIDA = 'Saída'

class Conta(SQLModel, table=True):
    """Classe que representa a tabela com as contas bancarias"""
    id: int = Field(primary_key=True)
    valor: float
    banco : Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

class Historico (SQLModel, table=True):
    """Classe que representa a tabela com o historico de movimentações de uma conta"""
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    conta: Conta = Relationship()
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor : float
    data: date
    descricao: str = Field(max_length=50)

#configuração do banco de dados
sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=False)

if __name__=='__main__':
    SQLModel.metadata.create_all(engine)