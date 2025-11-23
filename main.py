from utils import usuarios, tarefas, relatorios

usuario_logado = None  # controla usuário logado

def menu_principal():
    global usuario_logado

    while True:
        print("\n=== TASKFLOW ===")
        print("1 - Login")
        print("2 - Cadastrar usuário")
        print("3 - Criar tarefa")
        print("4 - Listar tarefas")
        print("5 - Concluir tarefa")
        print("6 - Excluir tarefa")
        print("7 - Gerar relatórios")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            usuario_logado = menu_login()
        elif opcao == "2":
            menu_cadastrar_usuario()
        elif opcao == "3":
            if verificar_login():
                menu_criar_tarefa()
        elif opcao == "4":
            if verificar_login():
                tarefas.listar_tarefas(usuario_logado)
        elif opcao == "5":
            if verificar_login():
                menu_concluir_tarefa()
        elif opcao == "6":
            if verificar_login():
                menu_excluir_tarefa()
        elif opcao == "7":
            if verificar_login():
                relatorios.gerar_relatorio(usuario_logado)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def verificar_login():
    """Verifica se há usuário logado antes de permitir ações"""
    if usuario_logado is None:
        print("\n❌ Você precisa fazer login primeiro!\n")
        return False
    return True

def menu_login():
    """Menu de login"""
    print("\n=== LOGIN ===")
    login = usuarios.login_usuario()
    if login:
        return login
    return None

def menu_cadastrar_usuario():
    """Menu de cadastro de usuário"""
    print("\n=== CADASTRAR USUÁRIO ===")
    nome = input("Nome: ")
    email = input("Email: ")
    login = input("Login: ")
    senha = input("Senha: ")
    usuarios.cadastrar_usuario(nome, email, login, senha)

def menu_criar_tarefa():
    """Menu de criação de tarefa"""
    print("\n=== NOVA TAREFA ===")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    responsavel = usuario_logado
    prazo = input("Prazo (dd/mm/aaaa): ")
    tarefas.criar_tarefa(titulo, descricao, responsavel, prazo)

def menu_concluir_tarefa():
    """Menu para concluir tarefa"""
    print("\n=== CONCLUIR TAREFA ===")
    id_tarefa = input("ID da tarefa: ")
    tarefas.concluir_tarefa(int(id_tarefa), usuario_logado)

def menu_excluir_tarefa():
    """Menu para excluir tarefa"""
    print("\n=== EXCLUIR TAREFA ===")
    id_tarefa = input("ID da tarefa: ")
    tarefas.excluir_tarefa(int(id_tarefa), usuario_logado)

if __name__ == "__main__":
    menu_principal()
