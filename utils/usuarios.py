from utils import arquivos

CAMINHO_ARQUIVO = "data/usuarios.json"

def cadastrar_usuario(nome: str, email: str, senha: str) -> bool:
    usuarios = arquivos.ler_json(CAMINHO_ARQUIVO)

    # Se o arquivo ainda não existir, inicia uma lista vazia
    if usuarios is None:
        usuarios = []

    # Verifica se o e-mail já existe
    for u in usuarios:
        if u["email"] == email:
            print("\n⚠️ E-mail já cadastrado!")
            return False

    novo_usuario = {
        "nome": nome,
        "email": email,
        "senha": senha  # (versão simples, sem hash)
    }

    usuarios.append(novo_usuario)
    arquivos.salvar_json(CAMINHO_ARQUIVO, usuarios)
    print("\n✔️ Usuário cadastrado com sucesso!")
    return True


def autenticar(email: str, senha: str) -> bool:
    usuarios = arquivos.ler_json(CAMINHO_ARQUIVO)

    if not usuarios:
        print("\n⚠️ Nenhum usuário cadastrado.")
        return False

    for u in usuarios:
        if u["email"] == email and u["senha"] == senha:
            print("\n🔓 Login realizado com sucesso!")
            return True

    print("\n❌ E-mail ou senha incorretos!")
    return False
