#📌 Sistema de Gerenciamento Financeiro

Este projeto é um Sistema de Gerenciamento Financeiro que permite criar contas bancárias, transferir saldo, registrar movimentações financeiras e visualizar gráficos de saldo por conta.

🚀 Funcionalidades

✅ Criar Conta: Registra uma nova conta bancária associada a um dos bancos disponíveis.
✅ Desativar Conta: Desativa uma conta desde que seu saldo esteja zerado.
✅ Transferir Saldo: Permite transferências entre contas ativas.
✅ Movimentar Dinheiro: Adiciona ou retira saldo de uma conta com descrição obrigatória.
✅ Visualizar Total em Contas: Calcula o saldo total em todas as contas ativas.
✅ Filtrar Histórico: Permite consultar movimentações dentro de um período específico.
✅ Gerar Gráficos: Exibe um gráfico com o saldo das contas ativas.

📂 Estrutura do Projeto

📂 projeto
│── 📄 models.py       # Modelos de dados e configuração do banco
│── 📄 views.py        # Lógica de manipulação de dados
│── 📄 templates.py    # Interface de interação via terminal
│── 📄 database.db     # Banco de dados SQLite
│── 📄 README.md       # Documentação do projeto

🛠️ Tecnologias Utilizadas

Python 3

SQLModel (ORM baseado em SQLAlchemy)

SQLite (Banco de dados leve e integrado)

Matplotlib (Para gerar gráficos)

📥 Instalação e Configuração

1️⃣ Clone o repositório

git clone https://github.com/seu-usuario/projeto-financeiro.git
cd projeto-financeiro

2️⃣ Crie um ambiente virtual e ative

python -m venv ambiente_virtual
# No Windows
ambiente_virtual\Scripts\activate
# No Linux/macOS
source ambiente_virtual/bin/activate

3️⃣ Instale as dependências

pip install -r requirements.txt

4️⃣ Execute o programa

python templates.py

📊 Gerando Gráficos

Para visualizar o saldo das contas ativas graficamente, execute:

python views.py

📌 Como Usar

Ao rodar python templates.py, você verá o menu com opções. Basta escolher a opção desejada e seguir as instruções no terminal.

Exemplo de movimentação:
1️⃣ Escolha a opção [4] Movimentar Dinheiro
2️⃣ Escolha uma conta
3️⃣ Defina o valor
4️⃣ Escolha se é uma entrada ou saída
5️⃣ Adicione uma descrição

📜 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo!

📌 Desenvolvido por: Igor :)

