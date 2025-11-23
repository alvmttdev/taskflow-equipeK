from utils import usuarios, tarefas, relatorios

# ---------------- Cores ---------------- #
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def menu_principal():
    usuario_logado = None

    while True:
        print(f"\n{BOLD}{CYAN}=== TASKFLOW ==={RESET}")
        print(f"{YELLOW}1{RESET} - Login")
        print(f"{YELLOW}2{RESET} - Cadastrar usuário")
        print(f"{YELLOW}3{RESET} - Criar tarefa")
        print(f"{YELLOW}4{RESET} - Listar tarefas")
        print(f"{YELLOW}5{RESET} - Concluir tarefa")
        print(f"{YELLOW}6{RESET} - Excluir tarefa")
        print(f"{YELLOW}7{RESET} - Gerar relatórios")
        print(f"{YELLOW}0{RESET} - Sair")

        opcao = input(f"{GREEN}Escolha: {RESET}").strip()

        if opcao == "1":
            if usuario_logado:
                print(f"{RED}❌ Já existe um usuário logado ({usuario_logado['nome']})!{RESET}")
            else:
                usuario_logado = menu_login()
        elif opcao == "2":
            menu_cadastrar_usuario()
        elif opcao == "3":
            if usuario_logado:
                menu_criar_tarefa(usuario_logado["login"])
            else:
                print(f"{RED}❌ Faça login antes de criar tarefas!{RESET}")
        elif opcao == "4":
            menu_listar_tarefas(usuario_logado)
        elif opcao == "5":
            if usuario_logado:
                menu_concluir_tarefa(usuario_logado["login"])
            else:
                print(f"{RED}❌ Faça login antes de concluir tarefas!{RESET}")
        elif opcao == "6":
            if usuario_logado:
                menu_excluir_tarefa(usuario_logado["login"])
            else:
                print(f"{RED}❌ Faça login antes de excluir tarefas!{RESET}")
        elif opcao == "7":
            if usuario_logado:
                relatorios.gerar_relatorio(usuario_logado["login"])
            else:
                print(f"{RED}❌ Faça login para gerar relatórios!{RESET}")
        elif opcao == "0":
            if usuario_logado:
                usuarios.logout_usuario(usuario_logado["login"])
            print(f"{MAGENTA}Saindo... Até logo!{RESET}")
            break
        else:
            print(f"{RED}Opção inválida!{RESET}")

# ---------------- Menus auxiliares ---------------- #
def menu_login():
    print(f"\n{BOLD}{BLUE}=== LOGIN ==={RESET}")
    usuario = usuarios.login_usuario()
    return usuario

def menu_cadastrar_usuario():
    print(f"\n{BOLD}{BLUE}=== CADASTRAR USUÁRIO ==={RESET}")
    nome = input("Nome: ").strip()
    email = input("Email: ").strip()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()
    usuarios.cadastrar_usuario(nome, email, login, senha)

def menu_criar_tarefa(usuario_login):
    print(f"\n{BOLD}{BLUE}=== NOVA TAREFA ==={RESET}")
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    prazo = input("Prazo (dd/mm/aaaa): ").strip()
    tarefas.criar_tarefa(titulo, descricao, usuario_login, prazo)

def menu_listar_tarefas(usuario):
    print(f"\n{BOLD}{BLUE}=== LISTAR TAREFAS ==={RESET}")
    if usuario:
        tarefas.listar_tarefas(usuario["login"])
    else:
        tarefas.listar_tarefas(None)

def menu_concluir_tarefa(usuario_login):
    print(f"\n{BOLD}{BLUE}=== CONCLUIR TAREFA ==={RESET}")
    try:
        id_tarefa = int(input("ID da tarefa: ").strip())
        tarefas.concluir_tarefa(id_tarefa, usuario_login)
    except ValueError:
        print(f"{RED}❌ ID inválido! Digite um número.{RESET}")

def menu_excluir_tarefa(usuario_login):
    print(f"\n{BOLD}{BLUE}=== EXCLUIR TAREFA ==={RESET}")
    try:
        id_tarefa = int(input("ID da tarefa: ").strip())
        tarefas.excluir_tarefa(id_tarefa, usuario_login)
    except ValueError:
        print(f"{RED}❌ ID inválido! Digite um número.{RESET}")

if __name__ == "__main__":
    menu_principal()
