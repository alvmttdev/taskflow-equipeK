import json, os

# ---------------- Configuração de diretórios ---------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJETO_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))
DATA_DIR = os.path.join(PROJETO_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)
ARQUIVO_USUARIOS = os.path.join(DATA_DIR, "usuarios.json")

# ---------------- Lista de logins ativos ---------------- #
logins_ativos = set()

# ---------------- Funções de usuários ---------------- #
def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return []
    with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(nome, email, login, senha):
    """
    Retorna True se o cadastro foi realizado com sucesso,
    False se o login já existe.
    """
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["login"] == login:
            return False
    usuarios.append({"nome": nome, "email": email, "login": login, "senha": senha})
    salvar_usuarios(usuarios)
    return True

def login_usuario():
    """
    Retorna o usuário (dicionário) se login e senha corretos,
    None se falhou.
    Não imprime nada.
    """
    usuarios = carregar_usuarios()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    if login in logins_ativos:
        return None  # Já está logado

    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            logins_ativos.add(login)
            return u

    return None  # Login ou senha incorretos

def logout_usuario(login):
    """Remove o usuário da lista de logins ativos. Não imprime nada."""
    logins_ativos.discard(login)
    return True
