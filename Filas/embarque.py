# Função que adiciona um passageiro à fila de embarque
def embarcar(fila: list, nome: str) -> None:
    fila.append(nome)  # Passageiro entra na fila no final

# Função que remove o primeiro passageiro da fila (desembarque)
def desembarcar(fila: list) -> str:
    if len(fila) == 0:
        return "Não há passageiros no ônibus para desembarcar."
    return f"Passageiro desembarcado: {fila.pop(0)}"

# Função que exibe todos os passageiros atualmente no ônibus
def exibir_passageiros(fila: list) -> None:
    if len(fila) == 0:
        print("Ônibus vazio.")
    else:
        print("Passageiros no ônibus:")
        for i in range(len(fila)):
            print(f"{i + 1}º - {fila[i]}")

# Função principal com o menu
def main() -> None:
    fila = []

    while True:
        print("\n--- Menu do Ônibus ---")
        print("1 - Embarcar passageiro")
        print("2 - Desembarcar passageiro")
        print("3 - Mostrar passageiros no ônibus")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do passageiro: ")
            embarcar(fila, nome)
        elif opcao == "2":
            mensagem = desembarcar(fila)
            print(mensagem)
        elif opcao == "3":
            exibir_passageiros(fila)
        elif opcao == "4":
            print("Encerrando o sistema do ônibus.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
