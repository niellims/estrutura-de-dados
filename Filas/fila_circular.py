# Função que inicializa a fila circular
def criar_fila(tamanho: int) -> list:
    return [None] * tamanho  # Cria a lista com tamanho fixo

# Função para inserir um elemento na fila circular
def inserir(fila: list, inicio: int, fim: int, tamanho: int, valor: int) -> tuple:
    proximo = (fim + 1) % tamanho

    # Verifica se a fila está cheia
    if proximo == inicio:
        print("Fila cheia! Não é possível inserir.")
        return (inicio, fim)

    fila[fim] = valor
    fim = proximo
    return (inicio, fim)

# Função para remover um elemento da fila circular
def remover(fila: list, inicio: int, fim: int, tamanho: int) -> tuple:
    if inicio == fim:
        print("Fila vazia! Nada a remover.")
        return (inicio, fim)

    removido = fila[inicio]
    fila[inicio] = None  # Limpa a posição (opcional)
    inicio = (inicio + 1) % tamanho
    print(f"Elemento removido: {removido}")
    return (inicio, fim)

# Função para exibir o conteúdo da fila circular
def exibir(fila: list, inicio: int, fim: int, tamanho: int) -> None:
    if inicio == fim:
        print("Fila vazia.")
        return

    print("Fila atual:")
    i = inicio
    while i != fim:
        print(fila[i])
        i = (i + 1) % tamanho

# Função principal com o menu
def main() -> None:
    tamanho = int(input("Informe o tamanho fixo da fila: "))
    fila = criar_fila(tamanho)
    inicio = 0
    fim = 0

    while True:
        print("\n--- Menu da Fila Circular ---")
        print("1 - Inserir elemento")
        print("2 - Remover elemento")
        print("3 - Exibir fila")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = int(input("Digite o valor a inserir: "))
            inicio, fim = inserir(fila, inicio, fim, tamanho, valor)
        elif opcao == "2":
            inicio, fim = remover(fila, inicio, fim, tamanho)
        elif opcao == "3":
            exibir(fila, inicio, fim, tamanho)
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
