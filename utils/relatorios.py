import os
import json
from datetime import datetime

# Caminho absoluto para data/tarefas.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJETO_DIR, "data")
ARQUIVO_TAREFAS = os.path.join(DATA_DIR, "tarefas.json")

# garante que a pasta data exista
os.makedirs(DATA_DIR, exist_ok=True)

def carregar_tarefas():
    """Carrega tarefas do arquivo JSON"""
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r") as f:
        return json.load(f)

def gerar_relatorio(usuario=None):
    """
    Gera relatório de tarefas.
    Se 'usuario' for fornecido, filtra apenas tarefas do usuário.
    """
    tarefas = carregar_tarefas()

    if usuario:
        tarefas = [t for t in tarefas if t["responsavel"] == usuario]

    if not tarefas:
        print("Nenhuma tarefa para gerar relatório.")
        return


    # separa tarefas
    concluídas = [t for t in tarefas if t["status"] == "concluída"]
    pendentes = [t for t in tarefas if t["status"] == "pendente"]
    atrasadas = []

    hoje = datetime.today()
    for t in pendentes:
        prazo = datetime.strptime(t["prazo"], "%d/%m/%Y")
        if prazo < hoje:
            atrasadas.append(t)

    print("\n=== RELATÓRIO DE TAREFAS ===")
    print(f"Total de tarefas: {len(tarefas)}")
    print(f"Tarefas concluídas: {len(concluídas)}")
    print(f"Tarefas pendentes: {len(pendentes)}")
    print(f"Tarefas atrasadas: {len(atrasadas)}\n")

    print("--- Tarefas concluídas ---")
    for t in concluídas:
        print(f"{t['id']} - {t['titulo']} (Prazo: {t['prazo']})")

    print("\n--- Tarefas pendentes ---")
    for t in pendentes:
        print(f"{t['id']} - {t['titulo']} (Prazo: {t['prazo']})")

    print("\n--- Tarefas atrasadas ---")
    for t in atrasadas:
        print(f"{t['id']} - {t['titulo']} (Prazo: {t['prazo']})")
