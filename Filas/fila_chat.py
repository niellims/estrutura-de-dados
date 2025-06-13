# Função para adicionar uma nova mensagem à fila do chat
def adicionar_mensagem(fila: list, autor: str, conteudo: str) -> None:
    mensagem = {"autor": autor, "conteudo": conteudo}
    fila.append(mensagem)  # Mensagem entra no final da fila

# Função para exibir a próxima mensagem (como se estivesse sendo lida)
def exibir_proxima_mensagem(fila: list) -> str:
    if len(fila) == 0:
        return "Nenhuma mensagem para exibir."
    mensagem = fila.pop(0)
    return f"{mensagem['autor']}: {mensagem['conteudo']}"

# Função para mostrar todas as mensagens na fila sem remover
def visualizar_fila(fila: list) -> None:
    if len(fila) == 0:
        print("Nenhuma mensagem no chat.")
    else:
        print("Mensagens na fila:")
        for i in range(len(fila)):
            print(f"{fila[i]['autor']}: {fila[i]['conteudo']}")

# Função principal com menu
def main() -> None:
    fila = []

    while True:
        print("\n--- Chat - Gerenciador de Mensagens ---")
        print("1 - Enviar nova mensagem")
        print("2 - Exibir próxima mensagem")
        print("3 - Visualizar todas as mensagens na fila")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            autor = input("Autor da mensagem: ")
            conteudo = input("Conteúdo da mensagem: ")
            adicionar_mensagem(fila, autor, conteudo)
        elif opcao == "2":
            mensagem = exibir_proxima_mensagem(fila)
            print(mensagem)
        elif opcao == "3":
            visualizar_fila(fila)
        elif opcao == "4":
            print("Encerrando o chat.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
