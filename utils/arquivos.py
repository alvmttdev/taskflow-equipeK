import json
import os
from typing import Any

def garantir_diretorio(caminho_arquivo: str) -> None:
    pasta = os.path.dirname(caminho_arquivo)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

def ler_json(caminho: str) -> Any:
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def salvar_json(caminho: str, dados: Any) -> None:
    garantir_diretorio(caminho)
    tmp = caminho + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)
    os.replace(tmp, caminho)

def ler_txt(caminho: str) -> str:
    if not os.path.exists(caminho):
        return ""
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()

def salvar_txt(caminho: str, conteudo: str) -> None:
    garantir_diretorio(caminho)
    with open(caminho, "w", encoding="utf-8") as f:
        f.write(conteudo)

def exportar_relatorio_txt(caminho: str, linhas: list[str]) -> None:
    garantir_diretorio(caminho)
    with open(caminho, "w", encoding="utf-8") as f:
        for linha in linhas:
            f.write(str(linha).rstrip() + "\n")

def carregar_arquivo_json(caminho: str):
    return ler_json(caminho)

def salvar_arquivo_json(caminho: str, dados: Any):
    salvar_json(caminho, dados)
