import json
import os

# Caminho para o arquivo dentro da pasta data
ARQUIVO_USUARIOS = os.path.join("data", "usuarios.json")

def carregar_usuarios():
    """Carrega usuários do JSON"""
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    with open(ARQUIVO_USUARIOS, "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    """Salva usuários no JSON, criando a pasta data se não existir"""
    pasta = os.path.dirname(ARQUIVO_USUARIOS)  # pega "data"
    os.makedirs(pasta, exist_ok=True)          # cria pasta se não existir
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(nome, email, login, senha):
    usuarios = carregar_usuarios()
    if login in usuarios:
        print("❌ Login já existe! Escolha outro.")
        return False
    usuarios[login] = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    salvar_usuarios(usuarios)
    print(f"✅ Usuário '{nome}' cadastrado com sucesso!")
    return True

def login_usuario():
    usuarios = carregar_usuarios()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    if login in usuarios and usuarios[login]["senha"] == senha:
        print(f"\n✅ Login realizado! Bem-vindo {usuarios[login]['nome']}\n")
        return login
    else:
        print("\n❌ Login ou senha incorretos!\n")
        return None
