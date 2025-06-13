# Função para adicionar uma nova requisição à fila
def adicionar_requisicao(fila: list, requisicao: str) -> None:
    fila.append(requisicao)  # Adiciona no final da fila

# Função para processar (atender) a próxima requisição
def processar_requisicao(fila: list) -> str:
    if len(fila) == 0:
        return "Nenhuma requisição na fila para processar."
    requisicao = fila.pop(0)
    return f"Requisição processada: {requisicao}"

# Função para exibir o estado atual da fila
def exibir_fila(fila: list) -> None:
    if len(fila) == 0:
        print("Fila de requisições vazia.")
    else:
        print("Requisições na fila:")
        for i in range(len(fila)):
            print(f"{i + 1}º - {fila[i]}")

# Função principal com menu de operações
def main() -> None:
    fila = []

    while True:
        print("\n--- Sistema de Controle de Requisições ---")
        print("1 - Adicionar requisição")
        print("2 - Processar próxima requisição")
        print("3 - Exibir fila de requisições")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            requisicao = input("Digite a descrição da requisição: ")
            adicionar_requisicao(fila, requisicao)
        elif opcao == "2":
            mensagem = processar_requisicao(fila)
            print(mensagem)
        elif opcao == "3":
            exibir_fila(fila)
        elif opcao == "4":
            print("Encerrando o sistema de controle.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
