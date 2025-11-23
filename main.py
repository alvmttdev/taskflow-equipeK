from utils import usuarios, tarefas, relatorios

def menu_principal():
    while True:
        print("\n=== TASKFLOW ===")
        print("1 - Cadastrar usuário")
        print("2 - Criar tarefa")
        print("3 - Listar tarefas")
        print("4 - Concluir tarefa")
        print("5 - Excluir tarefa")
        print("6 - Gerar relatórios")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            menu_cadastrar_usuario()
        elif opcao == "2":
            menu_criar_tarefa()
        elif opcao == "3":
            tarefas.listar_tarefas()
        elif opcao == "4":
            menu_concluir_tarefa()
        elif opcao == "5":
            menu_excluir_tarefa()
        elif opcao == "6":
            relatorios.gerar_relatorio()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

def menu_cadastrar_usuario():
    print("\n=== CADASTRAR USUÁRIO ===")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    usuarios.cadastrar_usuario(nome, email, senha)

def menu_criar_tarefa():
    print("\n=== NOVA TAREFA ===")
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    responsavel = input("Responsável: ")
    prazo = input("Prazo (dd/mm/aaaa): ")
    tarefas.criar_tarefa(titulo, descricao, responsavel, prazo)

def menu_concluir_tarefa():
    print("\n=== CONCLUIR TAREFA ===")
    id_tarefa = input("ID da tarefa: ")
    tarefas.concluir_tarefa(int(id_tarefa))

def menu_excluir_tarefa():
    print("\n=== EXCLUIR TAREFA ===")
    id_tarefa = input("ID da tarefa: ")
    tarefas.excluir_tarefa(int(id_tarefa))

if __name__ == "__main__":
    menu_principal()
