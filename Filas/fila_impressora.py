# Função que adiciona um novo arquivo à fila de impressão
def adicionar_arquivo(fila: list, nome: str, paginas: int) -> None:
    # Cada arquivo é representado como um dicionário com nome e páginas
    arquivo = {"nome": nome, "paginas": paginas}
    fila.append(arquivo)

# Função que processa (imprime) o primeiro arquivo da fila
def imprimir_arquivo(fila: list) -> str:
    if len(fila) > 0:
        arquivo = fila.pop(0)  # Remove o primeiro arquivo da fila
        return f"Imprimindo '{arquivo['nome']}' com {arquivo['paginas']} páginas."
    return "Nenhum arquivo na fila para imprimir."

# Função que exibe o estado atual da fila de impressão
def exibir_fila(fila: list) -> None:
    if len(fila) == 0:
        print("Fila de impressão vazia.")
    else:
        print("Arquivos na fila de impressão:")
        for i in range(len(fila)):
            arquivo = fila[i]
            print(f"{i + 1}º - {arquivo['nome']} ({arquivo['paginas']} páginas)")

# Função principal com o menu de operações
def main() -> None:
    fila = []

    while True:
        print("\n--- Menu de Impressão ---")
        print("1 - Enviar arquivo para impressão")
        print("2 - Imprimir próximo arquivo")
        print("3 - Exibir fila de impressão")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do arquivo: ")
            paginas = int(input("Quantidade de páginas: "))
            adicionar_arquivo(fila, nome, paginas)
        elif opcao == "2":
            mensagem = imprimir_arquivo(fila)
            print(mensagem)
        elif opcao == "3":
            exibir_fila(fila)
        elif opcao == "4":
            print("Encerrando o programa de impressão.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
main()
