import os
import json
from datetime import datetime

# ---------------- Cores ---------------- #
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# ---------------- Caminho do arquivo ---------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJETO_DIR, "data")
ARQUIVO_TAREFAS = os.path.join(DATA_DIR, "tarefas.json")

# ---------------- Funções auxiliares ---------------- #
def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------------- Relatório ---------------- #
def gerar_relatorio(usuario_login=None):
    tarefas = carregar_tarefas()

    # Filtra tarefas do usuário, se informado
    if usuario_login:
        tarefas = [t for t in tarefas if t.get("usuario") == usuario_login]

    if not tarefas:
        print(f"{YELLOW}⚠️ Nenhuma tarefa encontrada para gerar relatório.{RESET}")
        return

    pendentes = [t for t in tarefas if not t.get("concluida", False)]
    concluidas = [t for t in tarefas if t.get("concluida", False)]
    atrasadas = [
        t for t in pendentes
        if t.get("prazo") and datetime.strptime(t["prazo"], "%d/%m/%Y") < datetime.now()
    ]

    print(f"\n{BOLD}{CYAN}=== RELATÓRIO DE TAREFAS ==={RESET}")
    if usuario_login:
        print(f"{BOLD}Usuário:{RESET} {usuario_login}\n")

    print(f"{GREEN}✅ Concluídas ({len(concluidas)}):{RESET}")
    if concluidas:
        for t in concluidas:
            nome = t.get("nome_usuario", "Desconhecido")
            print(f"  {t['titulo']} - Prazo: {t['prazo']} | Criado por: {nome}")
    else:
        print("  Nenhuma tarefa concluída.")

    print(f"\n{RED}❌ Pendentes ({len(pendentes)}):{RESET}")
    if pendentes:
        for t in pendentes:
            nome = t.get("nome_usuario", "Desconhecido")
            status_emoji = "⏰" if datetime.strptime(t["prazo"], "%d/%m/%Y") < datetime.now() else "📝"
            print(f"  {t['titulo']} - Prazo: {t['prazo']} | Criado por: {nome} {status_emoji}")
    else:
        print("  Nenhuma tarefa pendente.")

    print(f"\n{YELLOW}⚠️ Atrasadas ({len(atrasadas)}):{RESET}")
    if atrasadas:
        for t in atrasadas:
            nome = t.get("nome_usuario", "Desconhecido")
            print(f"  {t['titulo']} - Prazo: {t['prazo']} | Criado por: {nome}")
    else:
        print("  Nenhuma tarefa atrasada.")

    print(f"\n{CYAN}{BOLD}============================{RESET}\n")
