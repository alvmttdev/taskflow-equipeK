
from utils import arquivos
from datetime import datetime

CAMINHO_TAREFAS = "data/tarefas.json"


def _formatar_relatorio(titulo, tarefas):
    """Gera o texto com layout mais organizado"""

    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    texto = f"""
=====================================================
                 {titulo}
=====================================================
Gerado em: {agora}
Quantidade de tarefas: {len(tarefas)}
=====================================================
"""

    for t in tarefas:
        texto += f"""
-----------------------------------------------------
ID.............: {t['id']}
Título.........: {t['titulo']}
Responsável....: {t['responsavel']}
Prazo..........: {t['prazo']}
Status.........: {t['status']}
-----------------------------------------------------
"""
    return texto


def relatorio_concluidas():
    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)

    if not tarefas:
        print("\n⚠️ Nenhuma tarefa cadastrada.")
        return

    concluidas = [t for t in tarefas if t["status"].lower() == "concluída"]

    print("\n📌 RELATÓRIO DE TAREFAS CONCLUÍDAS")

    if not concluidas:
        print("Nenhuma tarefa concluída.")
        return

    texto = _formatar_relatorio("RELATÓRIO – TAREFAS CONCLUÍDAS", concluidas)

    print(texto)   # Mostra no terminal

    arquivos.exportar_relatorio_txt("relatorio_concluidas.txt", texto)
    print("\n💾 Relatório salvo em: relatorio_concluidas.txt")


def relatorio_pendentes():
    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)

    if not tarefas:
        print("\n⚠️ Nenhuma tarefa cadastrada.")
        return

    pendentes = [t for t in tarefas if t["status"].lower() == "pendente"]

    print("\n📌 RELATÓRIO DE TAREFAS PENDENTES")

    if not pendentes:
        print("Nenhuma tarefa pendente.")
        return

    texto = _formatar_relatorio("RELATÓRIO – TAREFAS PENDENTES", pendentes)

    print(texto)   # Mostra no terminal

    arquivos.exportar_relatorio_txt("relatorio_pendentes.txt", texto)
    print("\n💾 Relatório salvo em: relatorio_pendentes.txt")


def relatorio_geral():
    tarefas = arquivos.ler_json(CAMINHO_TAREFAS)

    if not tarefas:
        print("\n⚠️ Nenhuma tarefa cadastrada.")
        return

    print("\n📊 RELATÓRIO GERAL DE TODAS AS TAREFAS")

    texto = _formatar_relatorio("RELATÓRIO GERAL DE TAREFAS", tarefas)

    print(texto)   # Mostra no terminal

    arquivos.exportar_relatorio_txt("relatorio_geral.txt", texto)
    print("\n💾 Relatório salvo em: relatorio_geral.txt")


def gerar_relatorio():
    print("""
📊 MENU DE RELATÓRIOS

1 – Tarefas Concluídas
2 – Tarefas Pendentes
3 – Todas as Tarefas
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        relatorio_concluidas()
    elif opcao == "2":
        relatorio_pendentes()
    elif opcao == "3":
        relatorio_geral()
    else:
        print("\n⚠️ Opção inválida.")
