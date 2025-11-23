from utils import usuarios, tarefas, relatorios

def menu_principal():
    usuario_logado = None

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
            if usuario_logado:
                menu_criar_tarefa(usuario_logado)
            else:
                print("❌ Faça login antes de criar tarefas!")
        elif opcao == "4":
            tarefas.listar_tarefas(usuario_logado)
        elif opcao == "5":
            if usuario_logado:
                menu_concluir_tarefa(usuario_logado)
            else:
                print("❌ Faça login antes de concluir tarefas!")
        elif opcao == "6":
            if usuario_logado:
                menu_excluir_tarefa(usuario_logado)
            else:
                print("❌ Faça login antes de excluir tarefas!")
        elif opcao == "7":
            relatorios.gerar_relatorio(usuario_logado)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def menu_login():
    print("\n=== LOGIN ===")
    login = usuarios.login_usuario()
    if login:
        return login
    return None

def menu_cadastrar_usuario():
    print("\n=== CADASTRAR USUÁRIO ===")
    nome = input("Nome: ")
    email = input("Email: ")
    login = input("Login: ")
    senha = input("Senha: ")
    usuarios.cadastrar_usuario(nome, email, login, senha)

def menu_criar_tarefa(usuario_logado):
    print("\n=== NOVA TAREFA ===")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    prazo = input("Prazo (dd/mm/aaaa): ")
    tarefas.criar_tarefa(titulo, descricao, usuario_logado, prazo)

def menu_concluir_tarefa(usuario_logado):
    print("\n=== CONCLUIR TAREFA ===")
    id_tarefa = input("ID da tarefa: ")
    if id_tarefa.isdigit():
        tarefas.concluir_tarefa(int(id_tarefa), usuario_logado)
    else:
        print("❌ ID inválido!")

def menu_excluir_tarefa(usuario_logado):
    print("\n=== EXCLUIR TAREFA ===")
    id_tarefa = input("ID da tarefa: ")
    if id_tarefa.isdigit():
        tarefas.excluir_tarefa(int(id_tarefa), usuario_logado)
    else:
        print("❌ ID inválido!")

if __name__ == "__main__":
    menu_principal()
