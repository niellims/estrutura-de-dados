# Função que adiciona um cliente ao final da fila
def chegada_cliente(fila: list, nome: str) -> None:
    fila.append(nome)  # Adiciona o cliente no final da fila

# Função que atende o primeiro cliente da fila
def atender_cliente(fila: list) -> str:
    if len(fila) > 0:
        return fila.pop(0)  # Remove e retorna o cliente da frente
    return "Nenhum cliente na fila."

# Função que exibe todos os clientes atualmente na fila
def exibir_fila(fila: list) -> None:
    if len(fila) == 0:
        print("Fila vazia.")
    else:
        print("Fila atual:")
        for i in range(len(fila)):
            print(f"{i + 1}º - {fila[i]}")

# Função principal que executa o menu e a simulação da fila
def main() -> None:
    fila = []
    while True:
        print("\n1 - Chegada de cliente")
        print("2 - Atender cliente")
        print("3 - Exibir fila")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            chegada_cliente(fila, nome)
        elif opcao == "2":
            nome_atendido = atender_cliente(fila)
            print(f"Cliente atendido: {nome_atendido}")
        elif opcao == "3":
            exibir_fila(fila)
        elif opcao == "4":
            print("Encerrando o atendimento.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
