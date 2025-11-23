import json
import os
from datetime import datetime

# ---------------- Cores e estilos ---------------- #
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ---------------- Caminho do arquivo ---------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJETO_DIR, "data")
ARQUIVO_TAREFAS = os.path.join(DATA_DIR, "tarefas.json")

# ---------------- Funções auxiliares ---------------- #
def carregar_tarefas():
    if not os.path.exists(ARQUIVO_TAREFAS):
        return []
    with open(ARQUIVO_TAREFAS, "r") as f:
        return json.load(f)

# ---------------- Relatórios ---------------- #
def gerar_relatorio(usuario=None):
    tarefas = carregar_tarefas()
    if usuario:
        tarefas = [t for t in tarefas if t["responsavel"] == usuario]

    if not tarefas:
        print(f"{YELLOW}⚠️ Nenhuma tarefa encontrada para gerar relatório.{RESET}")
        return

    pendentes = [t for t in tarefas if t["status"] == "pendente"]
    concluidas = [t for t in tarefas if t["status"] == "concluída"]
    atrasadas = [t for t in pendentes if datetime.strptime(t["prazo"], "%d/%m/%Y") < datetime.now()]

    print(f"\n{BOLD}{CYAN}=== RELATÓRIO DE TAREFAS ==={RESET}")
    print(f"{BOLD}Usuário:{RESET} {usuario}\n")

    print(f"{GREEN}✅ Concluídas ({len(concluidas)}):{RESET}")
    if concluidas:
        for t in concluidas:
            print(f"  {t['titulo']} - Prazo: {t['prazo']}")
    else:
        print("  Nenhuma tarefa concluída.")

    print(f"\n{RED}❌ Pendentes ({len(pendentes)}):{RESET}")
    if pendentes:
        for t in pendentes:
            status_emoji = "⏰" if datetime.strptime(t["prazo"], "%d/%m/%Y") < datetime.now() else "📝"
            print(f"  {t['titulo']} - Prazo: {t['prazo']} {status_emoji}")
    else:
        print("  Nenhuma tarefa pendente.")

    print(f"\n{YELLOW}⚠️ Atrasadas ({len(atrasadas)}):{RESET}")
    if atrasadas:
        for t in atrasadas:
            print(f"  {t['titulo']} - Prazo: {t['prazo']}")
    else:
        print("  Nenhuma tarefa atrasada.")

    print(f"\n{MAGENTA}============================{RESET}\n")
