import os
from datetime import datetime
from utils import arquivos

# Caminho do arquivo de tarefas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJETO_DIR, "data")
CAMINHO_TAREFAS = os.path.join(DATA_DIR, "tarefas.json")


# ---------------- Funções de carregamento/salvamento ---------------- #
def carregar_tarefas():
    return arquivos.ler_json(CAMINHO_TAREFAS)


def salvar_tarefas(tarefas):
    arquivos.salvar_json(CAMINHO_TAREFAS, tarefas)


# ---------------- Criar tarefa ---------------- #
def criar_tarefa(usuario_login, usuario_nome):
    tarefas = carregar_tarefas()

    titulo = input("Título da tarefa: ").strip()
    descricao = input("Descrição: ").strip()
    prazo_str = input("Prazo (dd/mm/aaaa): ").strip()

    # Valida se já existe título igual para o mesmo usuário
    for t in tarefas:
        if t.get("usuario") == usuario_login and t.get("titulo").lower() == titulo.lower():
            print("\n❌ Já existe uma tarefa com esse nome para este usuário!")
            return

    # Valida data
    try:
        prazo = datetime.strptime(prazo_str, "%d/%m/%Y")
        if prazo < datetime.now():
            print("\n❌ A data de prazo não pode ser no passado!")
            return
    except ValueError:
        print("\n❌ Data inválida! Use o formato dd/mm/aaaa.")
        return

    # Gera ID
    novo_id = max([t["id"] for t in tarefas], default=0) + 1

    # Cria tarefa
    nova_tarefa = {
        "id": novo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prazo": prazo_str,
        "concluida": False,
        "usuario": usuario_login,
        "nome_usuario": usuario_nome,  # <<< aqui
        "data_criacao": datetime.now().strftime("%d/%m/%Y %H:%M")
    }

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print(f"\n✅ Tarefa '{titulo}' criada com sucesso!")

    # ---------------- Função de correção para tarefas antigas ---------------- #
def corrigir_tarefas_antigas():
    """
    Adiciona 'usuario' e 'nome_usuario' em tarefas antigas que não têm.
    Retorna True se houve alteração.
    """
    tarefas_list = carregar_tarefas()
    alterado = False
    for t in tarefas_list:
        if "usuario" not in t:
            t["usuario"] = "desconhecido"
            alterado = True
        if "nome_usuario" not in t:
            # Tenta usar o nome real se existir, senão o login
            t["nome_usuario"] = t.get("nome_usuario", t.get("usuario", "Desconhecido"))
            alterado = True
    if alterado:
        salvar_tarefas(tarefas_list)
    return alterado



# ---------------- Listar tarefas ---------------- #
def listar_tarefas(usuario_login=None):
    tarefas = carregar_tarefas()
    if usuario_login:
        return [t for t in tarefas if t.get("usuario") == usuario_login]
    return tarefas


# ---------------- Verificar se usuário tem tarefas ---------------- #
def verificar_tarefas(usuario_login):
    return len(listar_tarefas(usuario_login)) > 0


# ---------------- Excluir tarefa ---------------- #
def excluir_tarefa(id_tarefa, usuario_login):
    tarefas = carregar_tarefas()

    tarefa_encontrada = None
    for t in tarefas:
        if t.get("id") == id_tarefa and t.get("usuario") == usuario_login:
            tarefa_encontrada = t
            break

    if not tarefa_encontrada:
        print(f"❌ Tarefa com ID {id_tarefa} não encontrada para este usuário.")
        return False

    tarefas.remove(tarefa_encontrada)
    salvar_tarefas(tarefas)
    print("✔️ Tarefa excluída com sucesso!")
    return True


# ---------------- Concluir tarefa ---------------- #
def concluir_tarefa(id_tarefa, usuario_login):
    tarefas = carregar_tarefas()

    tarefa_encontrada = None
    for t in tarefas:
        if t.get("id") == id_tarefa and t.get("usuario") == usuario_login:
            tarefa_encontrada = t
            break

    if not tarefa_encontrada:
        print(f"❌ Nenhuma tarefa encontrada com esse ID para este usuário.")
        return False

    if tarefa_encontrada.get("concluida"):
        print(f"⚠️ A tarefa '{tarefa_encontrada['titulo']}' já está concluída.")
        return False

    tarefa_encontrada["concluida"] = True
    tarefa_encontrada["concluida_em"] = datetime.now().strftime("%d/%m/%Y %H:%M")
    salvar_tarefas(tarefas)
    print(f"✔️ Tarefa '{tarefa_encontrada['titulo']}' concluída com sucesso!")
    return True


# ---------------- Corrigir tarefas antigas ---------------- #
def corrigir_tarefas_antigas():
    tarefas_list = carregar_tarefas()
    alterado = False
    for t in tarefas_list:
        if "usuario" not in t:
            t["usuario"] = "desconhecido"
            alterado = True
    if alterado:
        salvar_tarefas(tarefas_list)
    return alterado
