def adicionar_tarefa(fila: list, nome: str, prioridade: str):
    tarefa = {"nome": nome, "prioridade": prioridade}
    fila.append(tarefa)  # a tarefa entra no final da fila

def executar_tarefa(fila: list):
    if len(fila) == 0: #verifica se há tarefas na lista
        return "Nenhuma tarefa na fila para executar."
    tarefa = fila.pop(0) #apaga a primeira tarefa da lista
    return f"Tarefa executada: {tarefa['nome']}"

def prox_tarefa(fila: list):
    if len(fila) == 0: #verifica se há tarefas na lista
        print("Fila de tarefas vazia.")
    else:
        print("Próxima tarefa:")
        print(f"{fila[0]['nome']} com prioridade {fila[0]['prioridade']}")


def main():
    fila = []

    while True:
        print("\n--- Sistema de Agendamento de Tarefas ---")
        print("1 - Adicionar tarefa")
        print("2 - Mostrar próxima tarefa")
        print("3 - Executar (remover) tarefa atual")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da tarefa: ")
            prioridade = input("Qual a prioridade? (baixa, média ou alta). ")
            adicionar_tarefa(fila, nome, prioridade)
        elif opcao == "2":
            print('\n')
            prox_tarefa(fila)
            
        elif opcao == "3":
            mensagem = executar_tarefa(fila)
            print(mensagem)
        elif opcao == "4":
            print("Encerrando o sistema de agendamento.")
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
