from utils import arquivos

CAMINHO_TAREFAS = "data/tarefas.json"


def criar_tarefa(titulo, descricao, responsavel, prazo):
    """Cria uma nova tarefa e salva no JSON"""

    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)

    if not tarefas:
        tarefas = []

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "responsavel": responsavel,
        "prazo": prazo,
        "status": "pendente"
    }

    tarefas.append(nova_tarefa)
    arquivos.salvar_json(CAMINHO_TAREFAS, tarefas)

    print("\n✅ Tarefa cadastrada com sucesso!")


def listar_tarefas():
    """Lista todas as tarefas"""

    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)

    if not tarefas:
        print("\n⚠️ Nenhuma tarefa encontrada.")
        return

    print("\n📌 LISTA DE TAREFAS")
    for t in tarefas:
        print(f"""
ID: {t['id']}
Título: {t['titulo']}
Responsável: {t['responsavel']}
Prazo: {t['prazo']}
Status: {t['status']}
""")


def concluir_tarefa(id_tarefa):
    """Marca uma tarefa como concluída"""

    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)

    for t in tarefas:
        if t["id"] == id_tarefa:
            t["status"] = "concluída"
            arquivos.salvar_json(CAMINHO_TAREFAS, tarefas)
            print("\n🎉 Tarefa concluída com sucesso!")
            return

    print("\n⚠️ Tarefa não encontrada.")


def excluir_tarefa(id_tarefa):
    """Remove uma tarefa do sistema"""

    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)
    tarefas_novas = [t for t in tarefas if t["id"] != id_tarefa]

    if len(tarefas) == len(tarefas_novas):
        print("\n⚠️ Tarefa não encontrada.")
        return

    arquivos.salvar_json(CAMINHO_TAREFAS, tarefas_novas)

    print("\n🗑️ Tarefa excluída com sucesso!")
