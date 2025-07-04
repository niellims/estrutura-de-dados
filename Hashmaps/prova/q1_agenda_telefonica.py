def add(contatos):
    nome = input("Digite um nome de contato: ")
    if nome in contatos:
        telefone = input('Digite o novo telefone do contato: ')
        contatos[nome] = telefone
        print("Contato atualizado com sucesso!")
    else:
        telefone = input("Digite o telefone do contato: ")
        contatos[nome] = telefone
        print("Contato cadastrado com sucesso!")

def deletar(contatos):
    nome = input("Digite o nome do contato que você deseja apagar: ")
    if nome in contatos:
        contatos.pop(nome)
        print(f"Contato '{nome}' excluido com sucesso")
    else:
        print('Contato inexistente.')

def tel(contatos):
    nome = input('Digite o nome do contato que você deseja saber o telefone: ')
    if nome in contatos:
        print(f'O telefone de {nome} é {contatos.get(nome)}.')
    else:
        print('Contato inexistente.')

def list(contatos):
    for key, value in contatos.items():
        print('Contato: {} | Telefone: 1{}'.format(key, value))

def menu():
    contatos = {} 

    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar contato")
        print("2. Deletar contato")
        print("3. Verificar numero de telefone")
        print("4. Listar contatos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            add(contatos)
        elif opcao == "2":
            deletar(contatos)
        elif opcao == "3":
            tel(contatos)
            
        elif opcao == "4":
            list(contatos)
        elif opcao == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida.")

menu()