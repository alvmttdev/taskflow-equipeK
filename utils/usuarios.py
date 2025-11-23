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
    with open(ARQUIVO_USUARIOS, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(nome, email, login, senha):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["login"] == login:
            print(f"❌ Login '{login}' já existe!")
            return
    usuarios.append({"nome": nome, "email": email, "login": login, "senha": senha})
    salvar_usuarios(usuarios)
    print(f"✅ Usuário '{login}' cadastrado com sucesso!")

def login_usuario():
    usuarios = carregar_usuarios()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    # Verifica se já está logado
    if login in logins_ativos:
        print(f"❌ Usuário '{login}' já está logado!")
        return None

    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            logins_ativos.add(login)
            print(f"✅ Login realizado com sucesso! Bem-vindo(a) {u['nome']}")
            return u  # <-- Retornando o dicionário completo

    print("❌ Login ou senha incorretos!")
    return None


def logout_usuario(login):
    """Remove o usuário da lista de logins ativos"""
    logins_ativos.discard(login)
    print(f"⚪ Usuário '{login}' deslogado.")
