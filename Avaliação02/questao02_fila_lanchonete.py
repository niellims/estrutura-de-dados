def adicionar_cliente(fila: list, nome: str):
    fila.append(nome)  # adiciona o cliente no final da fila

def atender_cliente(fila: list):
    if len(fila) > 0:
        return fila.pop(0)  # remove e retorna o cliente da frente
    return "Nenhum cliente na fila."


def exibir_fila(fila: list):
    if len(fila) == 0: 
        print("Fila vazia.")
    else:
        print("Fila atual:")
        for i in range(len(fila)): # um laço percorrendo toda lista e imprimindo os clientes
            print(f"{i + 1}º - {fila[i]}")

def main():
    fila = [] #inicializa com uma lista vazia
    
    while True:
        print("\n1 - Adicioanr cliente")
        print("2 - Atender cliente")
        print("3 - Exibir fila")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            adicionar_cliente(fila, nome)
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

main()
