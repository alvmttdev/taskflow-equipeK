import json
import os
from datetime import datetime

# ---------------- Caminho do arquivo ---------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJETO_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
ARQUIVO_TAREFAS = os.path.join(DATA_DIR, "tarefas.json")

# ---------------- Funções auxiliares ---------------- #
def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w") as f:
        json.dump(tarefas, f, indent=4)

# ---------------- Funções principais ---------------- #
def criar_tarefa(titulo, descricao, responsavel, prazo):
    tarefas = carregar_tarefas()
    tarefa_id = len(tarefas) + 1

    # Validação de prazo
    try:
        dt = datetime.strptime(prazo, "%d/%m/%Y")
        if dt < datetime.now():
            print("❌ Prazo não pode ser anterior a hoje!")
            return
    except ValueError:
        print("❌ Formato de prazo inválido! Use dd/mm/aaaa")
        return

    # Validação de título duplicado apenas para o mesmo usuário
    for t in tarefas:
        if t["titulo"].lower() == titulo.lower() and t["responsavel"] == responsavel:
            print(f"❌ Você já tem uma tarefa com o título '{titulo}'!")
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
    tarefas = carregar_tarefas()
    if usuario:
        tarefas = [t for t in tarefas if t["responsavel"] == usuario]
    if not tarefas:
        print("⚠️ Nenhuma tarefa encontrada!")
        return

    print("\n=== LISTA DE TAREFAS ===")
    for t in tarefas:
        status_cor = "\033[92m" if t['status'] == 'concluída' else "\033[91m"
        print(f"ID: {t['id']} | Título: {t['titulo']} | Responsável: {t['responsavel']} | "
              f"Prazo: {t['prazo']} | Status: {status_cor}{t['status']}\033[0m")

def concluir_tarefa(tarefa_id, usuario):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == tarefa_id:
            if t["responsavel"] != usuario:
                print("❌ Você não é responsável por esta tarefa!")
                return
            if t["status"] == "concluída":
                print("❌ Tarefa já está concluída!")
                return
            t["status"] = "concluída"
            salvar_tarefas(tarefas)
            print(f"✅ Tarefa '{t['titulo']}' concluída!")
            return
    print("❌ Tarefa não encontrada!")

def excluir_tarefa(tarefa_id, usuario):
    tarefas = carregar_tarefas()
    for t in tarefas:
        if t["id"] == tarefa_id:
            if t["responsavel"] != usuario:
                print("❌ Você não é responsável por esta tarefa!")
                return
            tarefas.remove(t)
            salvar_tarefas(tarefas)
            print(f"✅ Tarefa '{t['titulo']}' excluída!")
            return
    print("❌ Tarefa não encontrada!")
