# Função para adicionar uma tarefa à fila
def adicionar_tarefa(fila: list, nome: str, tempo: int) -> None:
    tarefa = {"nome": nome, "tempo": tempo}
    fila.append(tarefa)  # A tarefa entra no final da fila

# Função para executar a próxima tarefa da fila
def executar_tarefa(fila: list) -> str:
    if len(fila) == 0:
        return "Nenhuma tarefa na fila para executar."
    tarefa = fila.pop(0)
    return f"Tarefa executada: {tarefa['nome']} (Tempo estimado: {tarefa['tempo']} min)"

# Função para exibir todas as tarefas na fila
def exibir_fila(fila: list) -> None:
    if len(fila) == 0:
        print("Fila de tarefas vazia.")
    else:
        print("Tarefas agendadas:")
        for i in range(len(fila)):
            print(f"{i + 1}º - {fila[i]['nome']} ({fila[i]['tempo']} min)")

# Função principal com menu de opções
def main() -> None:
    fila = []

    while True:
        print("\n--- Sistema de Agendamento de Tarefas ---")
        print("1 - Adicionar nova tarefa")
        print("2 - Executar próxima tarefa")
        print("3 - Exibir fila de tarefas")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            tempo = int(input("Tempo estimado (minutos): "))
            adicionar_tarefa(fila, nome, tempo)
        elif opcao == "2":
            mensagem = executar_tarefa(fila)
            print(mensagem)
        elif opcao == "3":
            exibir_fila(fila)
        elif opcao == "4":
            print("Encerrando o sistema de agendamento.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
