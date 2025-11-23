import json
import os
from datetime import datetime

# Define a pasta data absoluta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # utils/
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))  # raiz do projeto
DATA_DIR = os.path.join(PROJETO_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

ARQUIVO_TAREFAS = os.path.join(DATA_DIR, "tarefas.json")

def carregar_tarefas():
    """Carrega todas as tarefas do JSON"""
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    """Salva todas as tarefas no JSON"""
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)

def criar_tarefa(titulo, descricao, responsavel, prazo):
    """Cria uma nova tarefa e salva no JSON"""
    tarefas = carregar_tarefas()
    tarefa_id = len(tarefas) + 1

    # valida formato do prazo
    try:
        datetime.strptime(prazo, "%d/%m/%Y")
    except ValueError:
        print("❌ Formato de prazo inválido! Use dd/mm/aaaa")
        return

    tarefa = {
        "id": tarefa_id,
        "titulo": titulo,
        "descricao": descricao,
        "responsavel": responsavel,
        "prazo": prazo,
        "status": "pendente"
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f"✅ Tarefa '{titulo}' criada com sucesso!")

def listar_tarefas(usuario=None):
    """Lista tarefas, opcionalmente filtrando por usuário"""
    tarefas = carregar_tarefas()
    if usuario:
        tarefas = [t for t in tarefas if t["responsavel"] == usuario]

    if not tarefas:
        print("Nenhuma tarefa encontrada!")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for t in tarefas:
        print(f"ID: {t['id']} | Título: {t['titulo']} | Responsável: {t['responsavel']} | Prazo: {t['prazo']} | Status: {t['status']}")

def concluir_tarefa(tarefa_id, usuario):
    """Marca tarefa como concluída"""
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == tarefa_id and t["responsavel"] == usuario:
            t["status"] = "concluída"
            salvar_tarefas(tarefas)
            print(f"✅ Tarefa '{t['titulo']}' concluída!")
            return
    print("❌ Tarefa não encontrada ou você não é responsável!")

def excluir_tarefa(tarefa_id, usuario):
    """Exclui tarefa"""
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == tarefa_id and t["responsavel"] == usuario:
            tarefas.remove(t)
            salvar_tarefas(tarefas)
            print(f"✅ Tarefa '{t['titulo']}' excluída!")
            return
    print("❌ Tarefa não encontrada ou você não é responsável!")
