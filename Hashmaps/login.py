# Simular um sistema de login
# Crie um sistema onde os usuários podem se cadastrar (com nome e senha) e fazer
# login. Use um dicionário para armazenar as credenciais.

usuarios = {
    "joao": "1234",
    "maria": "senha123"
}

def cadastrar(usuarios):
    nome = input("Digite um nome de usuário: ")
    if nome in usuarios:
        print("Usuário já existe.")
    else:
        senha = input("Digite uma senha: ")
        usuarios[nome] = senha
        print("Cadastro realizado com sucesso!")


def login(usuarios):
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if nome in usuarios and usuarios[nome] == senha:
        print("Login bem-sucedido! Bem-vindo,", nome)
    else:
        print("Nome de usuário ou senha incorretos.")


def menu():
    usuarios = {}  # Dicionário que armazena os cadastros

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar")
        print("2. Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar(usuarios)
        elif opcao == "2":
            login(usuarios)
        elif opcao == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()
