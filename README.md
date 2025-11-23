
TaskFlow – Sistema de Controle de Tarefas Colaborativo 📝
🔹 Descrição

O TaskFlow é um sistema de controle de tarefas colaborativo desenvolvido em Python, permitindo cadastro de usuários, autenticação, gerenciamento de tarefas e geração de relatórios.
O sistema utiliza persistência em JSON (data/usuarios.json e data/tarefas.json) e exibe informações de forma visualmente agradável no terminal, com cores e emojis.

📂 Estrutura do Projeto
TaskFlow/
│
├── main.py               # Módulo principal com menus
├── utils/
│   └── arquivos.py       # Funções auxiliares de leitura/escrita
│   └── usuarios.py           # Cadastro e autenticação de usuários
│   └── tarefas.py            # Gerenciamento de tarefas (CRUD)
│   └── relatorios.py         # Geração de relatórios
├── data/
│   ├── usuarios.json
│   └── tarefas.json
└── README.md

🎯 Funcionalidades
# Usuários
- Cadastro de usuários com nome, e-mail, login e senha.
- Autenticação de login com validação de senha.

# Tarefas
- Criação de tarefas com:
- Título
- Descrição
- Responsável (usuário logado)
- Prazo (dd/mm/aaaa)
- Validações:
- Título duplicado não permitido para o mesmo usuário
- Prazo inválido ou anterior a hoje não permitido
- Conclusão e exclusão de tarefas apenas pelo responsável
- Listagem de tarefas por usuário
- Status das tarefas: pendente (vermelho) e concluída (verde)

# Relatórios
- Geração de relatórios simples por usuário, exibindo:
- Tarefas pendentes
- Tarefas concluídas
- Tarefas atrasadas

🎨 Layout Moderno no Terminal

Cores ANSI:

Verde ✅ para sucesso

Vermelho ❌ para erros

Amarelo ⚠️ para alertas

Azul / Magenta para títulos

Negrito para títulos e campos importantes

Emojis para feedback visual: ✅ ❌ ⚠️ 📝 📊

Exemplo de menu:

=== TASKFLOW ===
1 - Login
2 - Cadastrar usuário
3 - Criar tarefa
4 - Listar tarefas
5 - Concluir tarefa
6 - Excluir tarefa
7 - Gerar relatórios
0 - Sair
Escolha: 


Exemplo de lista de tarefas:

ID: 1 | Título: Revisar código | Responsável: admin1 | Prazo: 22/11/2025 | Status: pendente
ID: 2 | Título: Testes Unitários | Responsável: admin2 | Prazo: 23/11/2025 | Status: concluída

⚙️ Instruções de Uso

Clone o repositório:

git clone https://github.com/seuusuario/taskflow-equipeX.git
cd taskflow-equipeX


Execute o sistema:

python main.py

- Navegue pelo menu usando os números das opções.
- Faça login antes de criar, concluir ou excluir tarefas.
- Use Listar tarefas para visualizar suas tarefas.
- Gere relatórios para acompanhar produtividade.

🧩 Divisão de Módulos
- Desenvolvedor	Módulo Responsabilidade

- Dev1	main.py	Menu principal, fluxo do tarefas.py, Gerenciamento de tarefas (CRUD, validações), Relatórios e persistência de dados

- Dev2	usuarios.py	Cadastro e autenticação de usuário, relatorios.py, utils/arquivos.py