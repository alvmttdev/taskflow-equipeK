from utils import usuarios, tarefas, relatorios
import os
import readchar  # pip install readchar

# ---------------- Cores ---------------- #
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ---------------- Utilitários ---------------- #
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu_interativo(titulo, opcoes):
    index = 0
    while True:
        limpar_tela()
        print(titulo + "\n")
        for i, opcao in enumerate(opcoes):
            print(f"{GREEN}> {opcao}{RESET}" if i == index else f"  {opcao}")
        tecla = readchar.readkey()
        if tecla == readchar.key.UP:
            index = (index - 1) % len(opcoes)
        elif tecla == readchar.key.DOWN:
            index = (index + 1) % len(opcoes)
        elif tecla == readchar.key.ENTER:
            return opcoes[index]

# ---------------- Menus Auxiliares ---------------- #
def menu_login():
    print(f"\n{BOLD}{BLUE}=== LOGIN ==={RESET}")
    usuario = usuarios.login_usuario()
    if usuario:
        print(f"{GREEN}✅ Login realizado com sucesso! Bem-vindo(a) {usuario['nome']}.{RESET}")
    else:
        print(f"{RED}❌ Login ou senha incorretos!{RESET}")
    return usuario

def menu_cadastrar_usuario():
    print(f"\n{BOLD}{BLUE}=== CADASTRAR USUÁRIO ==={RESET}")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()
    
    sucesso = usuarios.cadastrar_usuario(nome, email, login, senha)
    if sucesso:
        print(f"{GREEN}✅ Usuário {nome} cadastrado com sucesso!{RESET}")
    else:
        print(f"{RED}❌ Login '{login}' já existe!{RESET}")

def menu_criar_tarefa(usuario):
    print(f"\n{BOLD}{GREEN}=== NOVA TAREFA ==={RESET}")
    tarefas.criar_tarefa(usuario["login"], usuario["nome"])

def menu_listar_tarefas(usuario=None):
    print(f"\n{BOLD}{CYAN}=== LISTAR TAREFAS ==={RESET}")

    if usuario:
        login = usuario.get("login", "")
        if not tarefas.verificar_tarefas(login):
            print(f"{YELLOW}⚠️ Você não possui tarefas cadastradas.{RESET}")
            return
        lista = tarefas.listar_tarefas(login)
    else:
        lista = tarefas.listar_tarefas()
        if not lista:
            print(f"{YELLOW}⚠️ Não há tarefas cadastradas.{RESET}")
            return

    for t in lista:
        status = "✅ Concluída" if t.get("concluida", False) else "❌ Pendente"
        nome_usuario = t.get("nome_usuario", "Desconhecido")
        print(f"[{t.get('id', '?')}] {t.get('titulo', 'Sem título')} - {t.get('descricao', '')} | Prazo: {t.get('prazo', 'Não definido')} | Criado por: {nome_usuario} | {status}")

    print(f"{BOLD}{CYAN}======================{RESET}")

def menu_concluir_tarefa(usuario):
    print(f"\n{BOLD}{GREEN}=== CONCLUIR TAREFA ==={RESET}")
    try:
        id_tarefa = int(input("ID da tarefa: ").strip())
        tarefas.concluir_tarefa(id_tarefa, usuario["login"])
    except ValueError:
        print(f"{RED}❌ ID inválido! Digite um número.{RESET}")

def menu_excluir_tarefa(usuario):
    print(f"\n{BOLD}{GREEN}=== EXCLUIR TAREFA ==={RESET}")
    try:
        id_tarefa = int(input("ID da tarefa: ").strip())
        tarefas.excluir_tarefa(id_tarefa, usuario["login"])
    except ValueError:
        print(f"{RED}❌ ID inválido! Digite um número.{RESET}")

def logout(usuario):
    if usuario:
        usuarios.logout_usuario(usuario["login"])
        print(f"{MAGENTA}✅ Usuário {usuario['nome']} deslogado com sucesso!{RESET}")
    return None

# ---------------- Menu Principal ---------------- #
def menu_principal():
    usuario_logado = None
    tarefas.corrigir_tarefas_antigas()  # Corrige tarefas sem nome de usuário

    while True:
        if usuario_logado:
            opcoes = [
                "Criar tarefa",
                "Listar tarefas",
                "Concluir tarefa",
                "Excluir tarefa",
                "Gerar relatórios",
                "Logout",
                "Sair"
            ]
            titulo = f"{BOLD}{CYAN}=== TASKFLOW (Usuário: {usuario_logado['nome']}) ==={RESET}"
        else:
            opcoes = [
                "Login",
                "Registrar usuário",
                "Listar tarefas",
                "Sair"
            ]
            titulo = f"{BOLD}{CYAN}=== TASKFLOW ==={RESET}"

        escolha = menu_interativo(titulo, opcoes)

        if not usuario_logado:
            if escolha == "Login":
                usuario_logado = menu_login()
            elif escolha == "Registrar usuário":
                menu_cadastrar_usuario()
            elif escolha == "Listar tarefas":
                menu_listar_tarefas(usuario_logado)
            elif escolha == "Sair":
                print(f"{MAGENTA}Saindo... Até logo!{RESET}")
                break
        else:
            if escolha == "Criar tarefa":
                menu_criar_tarefa(usuario_logado)
            elif escolha == "Listar tarefas":
                menu_listar_tarefas(usuario_logado)
            elif escolha == "Concluir tarefa":
                menu_concluir_tarefa(usuario_logado)
            elif escolha == "Excluir tarefa":
                menu_excluir_tarefa(usuario_logado)
            elif escolha == "Gerar relatórios":
                relatorios.gerar_relatorio(usuario_logado["login"])
            elif escolha == "Logout":
                usuario_logado = logout(usuario_logado)
            elif escolha == "Sair":
                usuario_logado = logout(usuario_logado)
                print(f"{MAGENTA}Saindo... Até logo!{RESET}")
                break

        input(f"\n{YELLOW}Pressione ENTER para continuar...{RESET}")

# ---------------- INÍCIO ---------------- #
if __name__ == "__main__":
    menu_principal()
